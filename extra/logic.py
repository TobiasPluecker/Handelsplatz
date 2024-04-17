import requests
import threading
import time



class AuctionHouseLogic:
    def __init__(self):
        #jeder Client speichert seinen Token
        self.base_url =  "http://127.0.0.1:8000"
        self.token = ""
        self.player_name = ""

    #man muss ein Passwort und ein Benutzernamen angeben und sich damit registrieren und die müssen min. 3 Zeichen lang sein
    def register(self, username, password):
        if len(username) < 3 or len(password) < 3:
            return 'Benutzername und Passwort müssen mindestens 3 Zeichen lang sein.'

        url = f"{self.base_url}/register"
        data = {
            'username': username,
            'password': password
        }
        response = requests.post(url, json=data)
        if response.status_code == 201:
            return 'Registrierung Erfolgreich'
        else:
            return 'Registrierung Fehlgeschlagen: ' + response.json()['detail']

    #hiermit loggt man sich ein mit einem bereits registrierten Account und man speichert sich seinen Token ab
    def login(self, username, password):
        self.player_name = username
        url = f"{self.base_url}/login"
        data = {
            'username': username,
            'password': password
        }
        response = requests.post(url, json=data)
        if response.status_code == 200:
            self.token = response.json()['token']
        else:
            return 'Login fehlgeschlagen'


    #es wird vom Server die Artikelliste an den Client gegeben und der Client gibt diese aus(mit den aktuellen Kursen)
    def get_artikel_list(self):
        url = f"{self.base_url}/get_artikel_list"
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            artikel = response.json()["message"]
            return artikel
        else:
            return []

    #es werden erst alle Gegenstände die man besitzt abgefragt und diese angezeigt, und dann kann man einen Artikelnamen 
    # und eine Preis angeben(ein Angebot erstellen) und der Server prüft ob man eine gültige Eingabe für Preis und 
    # Artikel angegeben hat(ob man den Artikel besitzt) und dies wird dann mittels response code ermittelt
    def angebot_erstellen(self, artikelname, preis):
        self.get_gegenstaende_einer_person()
        angebot = {
            'token_haendler': self.token,
            'artikel': artikelname,
            'preis': preis
        }
        url = f"{self.base_url}/angebot_erstellen"
        response = requests.post(url, json=angebot)
        if response.status_code == 200:
            return 'Angebot erstellt'
        elif response.status_code == 404:
            return 'Gegenstand nicht im Besitz'
        else:
            return 'Fehler beim erstellen des Angebots'

    #bei der funktion löscht man den abgespeicherten Token da man einen neuen Token wieder beim einloggen 
    # bekommt(man beendet seine eigene Sitzung)
    def logout(self):
        url = f"{self.base_url}/logout"
        ausloggen = {
            "token_haendler": self.token
        }
        response = requests.post(url, json=ausloggen)

        if response.status_code == 200:
            self.token = ""
            return "Erfolgreich abgemeldet"
        else:
            return "Abmeldung fehlgeschlagen."

    # Man kann sich mit der Funktion Geld zu seinem Konto hinzufügen, wobei man Code 200 bekommt wenn es funktioniert hat
    # den Code 400 wenn man einen ungültigen Wert für Geld übergeben hat, den Code 404 falls der Benutzer nicht auf 
    # dem Server existiert.
    def geld_hinzufuegen(self, betrag):
        url = f"{self.base_url}/geld_hinzufuegen"
        einzahlung = {"token_haendler": self.token, "betrag": betrag}
        response = requests.post(url, json=einzahlung)

        if response.status_code == 200:
            return "Geld erfolgreich hinzugefügt"
        elif response.status_code == 400:
            return "Ungültiger Wert für 'betrag'"
        elif response.status_code == 404:
            return "Name nicht gefunden"
        else:
            return "Fehler beim Hinzufügen des Geldes"

    #gibt das aktuelle Guthaben einer Person wieder(von sich selbst da Token in Client lokal gespeichert wurde) dann 
    # bekommt man Code 200 und wenn die Person nicht existiert dann bekommt man 404
    def get_guthaben(self):
        url = f"{self.base_url}/guthaben_einer_person/{self.token}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            guthaben = data["guthaben"]
            return guthaben
        elif response.status_code == 404:
            return None
        else:
            return None

    #die Funktion fragt immer das aktuelle Guthaben ab
    #def update_guthaben():
    #    while True:
    #       guthaben = get_guthaben(token)
    #        if guthaben is not None:
    #            guthaben_label.config(text="Aktuelles Guthaben: {} €".format(guthaben))
    #        else:
    #            guthaben_label.config(text="")
    #       time.sleep(5)  # Guthaben alle 5 Sekunden aktualisieren
    

    #man fragt damit ab welche Objekte man besitzt und man bekommt diese als array übergeben
    def get_gegenstaende_einer_person(self):
        response = requests.get(f"{self.base_url}/gegenstaende_einer_person/{self.token}")
        if response.status_code == 200:
            data = response.json()
            gegenstaende_liste = data["gegenstaende"]
            return gegenstaende_liste
        elif response.status_code == 404:
            return []
        else:
            return []

    #fragt die Angebote ab welche momentan existieren und diese werden dann ausgegeben
    def get_angebote(self):
        response = requests.get(f"{self.base_url}/angebote_print")
        if response.status_code == 200:
            data = response.json()
            angebote = data["gegenstaende"]
            return angebote
        else:
            return []

    #Damit kann man sich Gegenstände vom Server zum momentanen Martkpreis holen
    #Code 200 hat funktioniert
    #Code 404 Gegenstand nicht vorrätig oder nicht genug Geld
    def gegenstand_holen(self, artikel):
        self.get_artikel_list()
        kauf = {"token_kaeufer": self.token, "artikel": artikel}
        response = requests.post(f"{self.base_url}/gegenstaende_holen", json=kauf)
        if response.status_code == 200:
            return 'Gegenstand erfolgreich gekauft'
        elif response.status_code == 404:
            return 'Gegenstand nicht vorrätig oder unzureichendes Guthaben'
        else:
            return 'Fehler beim Holen des Gegenstands'

    #Fragt ab welche Angebote es gibt und bekommt Array mit allen Angeboten
    def get_angebote_print(self):
        url = f"{self.base_url}/angebote_print"
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            angebote = response.json()["gegenstaende"]
            return angebote
        else:
            return []

    #Damit kann man ein Angebot kaufen wobei erstmal abgefragt werden welche Angebote existieren
    #man kauft ein Angebot indem man die dazugehörige Angebotsnummer übergibt und wenn das Angebot noch existiert und
    #man genug Geld hat kauft man dieses
    def angebot_kaufen(self, nummer):
        self.get_angebote_print()
        url = f"{self.base_url}/verkaufen"
        data = {
            "token_kaeufer": self.token,
            "nummer": nummer
        }
        response = requests.post(url, json=data)
    
        if response.status_code == 200:
            return 'Kauf erfolgreich'
        elif response.status_code == 404:
            error = response.json()["error"]
            return 'Fehler beim kaufen'
        else:
            return 'Unbekannter Fehler beim kaufen eines Angebotes'

    #Damit kann man von seinem Konto einen gewünschte Geldbetrag sich wieder auszahlen lassen wenn dieser gültig ist
    def geld_abheben(self, betrag):
        url = f"{self.base_url}/auszahlen"
        data = {
            "token_haendler": self.token,
            "betrag": betrag
        }
        response = requests.post(url, json=data)
    
        if response.status_code == 200:
            return 'Auszahlung erfolgreich'
        elif response.status_code == 404:
            error = response.json()["error"]
            return 'Fehler bei der Auszahlung'
        else:
            return 'Unbekannter Fehler bei der Auszahlung'



