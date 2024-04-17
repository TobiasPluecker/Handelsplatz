import numpy as np
from fastapi import FastAPI, Depends, HTTPException, status 
from fastapi.responses import JSONResponse
from auth import AuthHandler
from schemas import AuthDetails
import uvicorn
from typing import Optional
import os
from pydantic import BaseModel
from typing import List
import markt
from markt import Markt
import matplotlib.pyplot as plt
import time

# uvicorn server:app --port 8000 --reload

class Angebot(BaseModel):
    token_haendler: str 
    artikel: str 
    preis: int


class Kauf(BaseModel):
   token_kaeufer: str
   artikel: str


class Einzahlung(BaseModel):
   token_haendler: str
   betrag: float


class Kaufvorgang(BaseModel):
   token_kaeufer: str
   nummer: int


class Ausloggen(BaseModel):
    token_haendler: str


class Auszahlung(BaseModel):
    token_haendler: str
    betrag: float



token_name = {}
   

app = FastAPI()

handels_platz = Markt()
auth_handler = AuthHandler()
users = []
artikel = []


zeit_add = 0


startzeit = None

@app.on_event("startup")
async def startup_event():
    global startzeit
    startzeit = time.time()
    print("Server gestartet")


def kurs():
    handels_platz.preise_aktualisieren()



@app.post('/register', status_code=201)
def register(auth_details: AuthDetails):
    if any(x['username'] == auth_details.username for x in users):
        raise HTTPException(status_code=405, detail='Username is taken')
    hashed_password = auth_handler.get_password_hash(auth_details.password)
    users.append({
        'username': auth_details.username,
        'password': hashed_password    
    })
    temp = auth_details.username
    handels_platz.haendler_erstellen(temp)
    return


@app.post('/login')
def login(auth_details: AuthDetails):
    user = None
    for x in users:
        if x['username'] == auth_details.username:
            user = x
            break
    
    if (user is None) or (not auth_handler.verify_password(auth_details.password, user['password'])):
        raise HTTPException(status_code=405, detail= "Ungültiger Benutzername und/oder Passwort")
    

    token = auth_handler.encode_token(user['username'])
    token_name[token] = auth_details.username # test
    return { 'token': token }


@app.get('/get_artikel_list')
async def get_artikel_list():
    global startzeit
    endzeit = time.time() 
    gesamtzeit = endzeit - startzeit
    handels_platz.preise_aktualisieren(int(gesamtzeit))
    startzeit = time.time()
    artikel = handels_platz.artikel_print()
    return {"message": artikel} 


@app.post('/angebot_erstellen')
async def angebot_erstellen(angebot: Angebot):
    haendler_token = angebot.token_haendler
    haendler = token_name[haendler_token]
    artikel = angebot.artikel
    preis = angebot.preis

    try:
        angebot_neu = handels_platz.angebot_erstellen(haendler, artikel, preis)
        return {"angebot": angebot_neu}
    except RuntimeError as e:
        return JSONResponse(status_code=404, content={"error": str(e)})


@app.post('/logout')
def logout(ausloggen: Ausloggen):
    token = ausloggen.token_haendler
    if token in token_name:
        del token_name[token]
    else:
        raise HTTPException(status_code=401, detail="Ungültiger Token oder Benutzer bereits abgemeldet")
    return {"message": "Erfolgreich abgemeldet"}


@app.post('/geld_hinzufuegen')
async def geld_hinzufuegen(einzahlung: Einzahlung):
    name_token = einzahlung.token_haendler
    name = token_name.get(name_token)
    betrag = einzahlung.betrag
    
    if not name:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Name nicht gefunden")
    
    if not isinstance(betrag, (int, float)) or betrag <= 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Ungültiger Wert für 'betrag'")
    
    handels_platz.geld_hinzufuegen(name, betrag)
    return status.HTTP_200_OK


@app.post('/gegenstaende_holen')
async def gegenstaende_holen(kauf: Kauf):
    kaeufer_token = kauf.token_kaeufer
    kaeufer = token_name.get(kaeufer_token)
    artikel = kauf.artikel
    try:
        handels_platz.gegenstaende_holen(kaeufer, artikel)
        return {"kauf": artikel}
    except RuntimeError as e:
        return JSONResponse(status_code=404, content={"error": str(e)})

 
@app.get('/guthaben_einer_person/{token}')
async def guthaben_einer_person(token: str):
    name = token_name.get(token)
    
    if not name:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Name nicht gefunden")
    
    guthaben = handels_platz.guthaben_einer_person(name)
    return {"guthaben": guthaben}


@app.get('/gegenstaende_einer_person/{token}')    
async def gegenstaende_einer_person(token: str):
  name = token_name[token]

  if not name:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Name nicht gefunden")
  

  array = []
  array = handels_platz.gegenstaende_einer_person(name)
  return {"gegenstaende": array}


@app.get('/angebote_print')    
async def angebote_print():
  array = []
  array = handels_platz.angebote_print()
  return {"gegenstaende": array}


@app.get('/artikel_print')    
async def artikel_print():
    temp = zeit_add
    endzeit = time.time() - startzeit
    gesamtzeit = endzeit - zeit_add
    handels_platz.preise_aktualisieren(int(endzeit))
    zeit_add + endzeit
    array = []
    array = handels_platz.artikel_print()

    return {"gegenstaende": array}


@app.post('/verkaufen')    
async def verkaufen(kaufvorgang: Kaufvorgang):
    kaeufer_token = kaufvorgang.token_kaeufer
    kaeufer = token_name[kaeufer_token]
    nummer = kaufvorgang.nummer
    try:
        handels_platz.verkaufen(kaeufer, nummer)
        return
    except RuntimeError as e:
        return JSONResponse(status_code=404, content={"error": str(e)})


@app.post('/auszahlen')
async def auszahlen(auszahlung: Auszahlung):
    haendler_token = auszahlung.token_haendler
    haendler = token_name[haendler_token]
    betrag = auszahlung.betrag
    try:
        handels_platz.geld_auszahlen(haendler, betrag)
        return
    except RuntimeError as e:
        return JSONResponse(status_code=404, content={"error": str(e)})


@app.delete('/user/{username}')
def delete_user(username: str, password: str):
    user_found = False
    user_to_remove = None
    for user in users:
        if user['username'] == username:
            if auth_handler.verify_password(password, user['password']):
                user_to_remove = user
                user_found = True
            break
    if not user_found:
        raise HTTPException(status_code=404, detail="Benutzer nicht gefunden oder ungültiges Passwort")
    
    users.remove(user_to_remove)
    
    # Lösche auch alle zugehörigen Tokens des Benutzers
    tokens_to_remove = [token for token, name in token_name.items() if name == username]
    for token in tokens_to_remove:
        del token_name[token]
    
    return {"message": "Benutzer erfolgreich gelöscht"}




if __name__ == "__main__":
    this_python_file = os.path.basename(__file__)[:-3]
    instance = uvicorn.run(f"{this_python_file}:app", host = "127.0.0.1", port = 8000, log_level = "info", reload = True)
