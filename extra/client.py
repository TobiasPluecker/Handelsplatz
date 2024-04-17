import requests
import tkinter as tk
import threading
import time
from tkinter import messagebox



token = ""
player_name = ""
geld_hinzufuegen_submit_button = None
betrag_entry = None
geld_hinzufuegen_labe = None
betrag_label = None
angebot_erstellen_label = None
artikelname_label = None 
artikelname_entry = None 
preis_label = None 
preis_entry = None 
angebot_erstellen_submit_button = None

def main():
    base_url = "http://127.0.0.1:8000"

    def register(username, password):
        if len(username) < 3 or len(password) < 3:
            add_message('Benutzername und Passwort müssen mindestens 3 Zeichen lang sein.')
            return

        url = f"{base_url}/register"
        data = {
            'username': username,
            'password': password
        }
        response = requests.post(url, json=data)
        if response.status_code == 201:
            add_message('Registrierung Erfolgreich')
        else:
            add_message('Registrierung Fehlgeschlagen: ' + response.json()['detail'])

    def login(username, password):
        global player_name
        player_name = username
        url = f"{base_url}/login"
        data = {
            'username': username,
            'password': password
        }
        response = requests.post(url, json=data)
        if response.status_code == 200:
            global token
            token = response.json()['token']
            add_message('Login Erfolgreich')
            #add_message('Token: ' + token)
            register_button.pack_forget()
            login_button.pack_forget()
            username_label.pack_forget()
            username_entry.pack_forget()
            password_label.pack_forget()
            password_entry.pack_forget()
            show_artikel_button.pack()
            angebot_erstellen_button.pack()
            geld_hinzufuegen_button.pack()
            show_gegenstaende_button.pack()
            show_angebote_button.pack()  
            logout_button.pack()
        else:
            add_message('Login fehlgeschlagen: ' + response.json()['detail'])


    def get_artikel_list():
        url = f"{base_url}/get_artikel_list"
        headers = {
            'Authorization': f'Bearer {token}'
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            artikel = response.json()["message"]
            add_message("Artikel:")
            for a in artikel:
                add_message(a)
        else:
            add_message("Aufrufen der Artikelliste Fehlgeschlagen.")

    def angebot_erstellen(artikelname, preis):
        angebot = {
            'token_haendler': token,
            'artikel': artikelname,
            'preis': preis
        }
        url = f"{base_url}/angebot_erstellen"
        
        response = requests.post(url, json=angebot)
        if response.status_code == 200:
            angebot_neu = response.json()["angebot"]
            add_message("Angebot erstellt:")
            add_message(f"Haendler: {angebot_neu['haendler']}")
            add_message(f"Artikel: {angebot_neu['artikel']}")
            add_message(f"Preis: {angebot_neu['preis']}")
            show_artikel_button.pack()
            angebot_erstellen_button.pack()
            geld_hinzufuegen_button.pack()
            show_gegenstaende_button.pack()
            logout_button.pack()
        elif response.status_code == 404:
            add_message("Du besitzt den Artikel nicht")
        else:
            add_message("Angebot erstellen fehlgeschlagen.")

    def logout():
        global token
        url = f"{base_url}/logout"
        ausloggen = {
            "token_haendler" : token
        }
        response = requests.post(url, json=ausloggen)

        if response.status_code == 200:
            add_message("Erfolgreich abgemeldet")
            logout_button.pack_forget()
            show_artikel_button.pack_forget()
            angebot_erstellen_button.pack_forget()
            geld_hinzufuegen_button.pack_forget()
            show_gegenstaende_button.pack_forget()
            show_angebote_button.pack_forget()
            register_button.pack()
            login_button.pack()
            username_label.pack()
            username_entry.pack()
            password_label.pack()
            password_entry.pack()
            token = ""
        else:
            add_message("Abmeldung fehlgeschlagen.")

    def geld_hinzufuegen(betrag):
        url = f"{base_url}/geld_hinzufuegen"
        
        einzahlung = {"token_haendler": token, "betrag": betrag}
    
        # Senden der Anfrage an den Server
        response = requests.post(url, json=einzahlung)
    
        # Überprüfen des Statuscodes der Antwort
        if response.status_code == 200:
            add_message("Geld erfolgreich hinzugefügt")
            back_button_geld.pack()
        elif response.status_code == 400:
            add_message("Ungültiger Wert für 'betrag'")
        elif response.status_code == 404:
            add_message("Name nicht gefunden")
        else:
            add_message("Fehler beim Hinzufügen des Geldes")

    def get_guthaben(token):
        url = f"{base_url}/guthaben_einer_person/{token}"

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            guthaben = data["guthaben"]
            return guthaben
        elif response.status_code == 404:
            print("User nicht gefunden")
        else:
            add_message("Fehler beim Abrufen des Guthabens")
            return None

    def update_guthaben():
        while True:
            guthaben = get_guthaben(token)
            if guthaben is not None:
                guthaben_label.config(text="Aktuelles Guthaben: {} €".format(guthaben))
            else:
                guthaben_label.config(text="")
            time.sleep(5)  # Guthaben alle 5 Sekunden aktualisieren
    
    def get_gegenstaende_einer_person():
        response = requests.get(f"{base_url}/gegenstaende_einer_person/{token}")
        if response.status_code == 200:
            data = response.json()
            gegenstaende_liste = data["gegenstaende"]
            add_message("Deine Gegenstände:")
            for gegenstaende in gegenstaende_liste:
                add_message(f"- {gegenstaende}")
        elif response.status_code == 404:
            add_message("User nicht gefunden")
        else:
            print("Fehler beim Abrufen der Spielerliste.")

    
    def get_angebote_print():
    
        response = requests.get(f"{base_url}/angebote_print")

        if response.status_code == 200:
            data = response.json()
            angebote = data["gegenstaende"]
            add_message("Momentane Angebote:")
            for a in angebote:
                add_message(f"- {a}")
        else:
            add_message("Fehler beim Abrufen der Angebote:", response.text)

    def gegenstaende_holen(artikel):
    
        # Erstellen des Kaufobjekts
        kauf = {"token_kaeufer": token, "artikel": artikel}
    
        # Senden der Anfrage an den Server
        response = requests.post(f"{base_url}/gegenstaende_holen", json=kauf)
    
        # Überprüfen des Statuscodes der Antwort
        if response.status_code == 200:
            add_message("Gegenstand erfolgreich gekauft")
        elif response.status_code == 400:
            add_message("Gegenstand nicht vorrätig oder unzureichendes Guthaben")
        else:
            ("Fehler beim Holen des Gegenstands")
        


    def add_message(message):
        textbox.config(state=tk.NORMAL)
        textbox.insert(tk.END, message + "\n")
        textbox.config(state=tk.DISABLED)

    def register_button_clicked():
        username = username_entry.get()
        password = password_entry.get()
        register(username, password)

    def login_button_clicked():
        username = username_entry.get()
        password = password_entry.get()
        login(username, password)

    def show_artikel_button_clicked():
        get_artikel_list()

    def show_angebot_erstellen_form():
        global angebot_erstellen_label, artikelname_label, artikelname_entry, preis_label, preis_entry, angebot_erstellen_submit_button
        show_artikel_button.pack_forget()
        angebot_erstellen_button.pack_forget()
        geld_hinzufuegen_button.pack_forget()
        logout_button.pack_forget()
        show_gegenstaende_button.pack_forget()
        show_angebote_button.pack_forget()

        angebot_erstellen_label = tk.Label(window, text="Angebot erstellen")
        angebot_erstellen_label.pack()

        artikelname_label = tk.Label(window, text="Artikelname:")
        artikelname_label.pack()
        artikelname_entry = tk.Entry(window)
        artikelname_entry.pack()

        preis_label = tk.Label(window, text="Preis:")
        preis_label.pack()
        preis_entry = tk.Entry(window)
        preis_entry.pack()

        angebot_erstellen_submit_button = tk.Button(window, text='Angebot erstellen',
                                                   command=lambda: angebot_erstellen(
                                                       artikelname_entry.get(),
                                                       preis_entry.get()
                                                   ))
        angebot_erstellen_submit_button.pack()
        back_button_angebot.pack()

    def angebot_erstellen_submit_button_clicked():
        show_angebot_erstellen_form()

    def geld_hinzufuegen_button_clicked():
        global geld_hinzufuegen_submit_button, betrag_entry, geld_hinzufuegen_label, betrag_label

        logout_button.pack_forget()
        show_artikel_button.pack_forget()
        angebot_erstellen_button.pack_forget()
        geld_hinzufuegen_button.pack_forget()
        show_gegenstaende_button.pack_forget()
        show_angebote_button.pack_forget()

        geld_hinzufuegen_label = tk.Label(window, text="Geld hinzufügen")
        geld_hinzufuegen_label.pack()

        betrag_label = tk.Label(window, text="Betrag:")
        betrag_label.pack()
        betrag_entry = tk.Entry(window)
        betrag_entry.pack()

        geld_hinzufuegen_submit_button = tk.Button(window, text='Geld hinzufügen', command=validate_and_hinzufuegen)
        geld_hinzufuegen_submit_button.pack()
        back_button_geld.pack()

    def validate_and_hinzufuegen():
        betrag = betrag_entry.get()
        try:
            betrag = float(betrag)
            if betrag > 0:
                geld_hinzufuegen(betrag)
            else:
                messagebox.showerror("Fehler", "Bitte geben Sie einen positiven Betrag ein.")
        except ValueError:
            messagebox.showerror("Fehler", "Bitte geben Sie eine gültige Zahl ein.")

    def back_geld():
        back_button_geld.pack_forget()
        show_artikel_button.pack()
        angebot_erstellen_button.pack()
        geld_hinzufuegen_button.pack()
        show_gegenstaende_button.pack()
        show_angebote_button.pack()
        logout_button.pack()
    
        # Ausblenden der zusätzlichen Elemente
        geld_hinzufuegen_submit_button.pack_forget()
        betrag_entry.pack_forget()
        geld_hinzufuegen_label.pack_forget()
        betrag_label.pack_forget()

    def back_angebot():
        back_button_angebot.pack_forget()
        show_artikel_button.pack()
        angebot_erstellen_button.pack()
        geld_hinzufuegen_button.pack()
        show_gegenstaende_button.pack()
        show_angebote_button.pack()
        logout_button.pack()
    
        # Ausblenden der zusätzlichen Elemente
        angebot_erstellen_label.pack_forget()
        artikelname_label.pack_forget()
        artikelname_entry.pack_forget()
        preis_label.pack_forget()
        preis_entry.pack_forget()
        angebot_erstellen_submit_button.pack_forget()

    def show_gegenstaende_button_clicked():
        get_gegenstaende_einer_person()

    def show_angebote_button_clicked():
        get_angebote_print()



    window = tk.Tk()
    window.title("Auktionshaus")
    window.geometry("700x800")

    register_button = tk.Button(window, text='Registrieren', command=register_button_clicked)
    register_button.pack()

    login_button = tk.Button(window, text='Login', command=login_button_clicked)
    login_button.pack()

    username_label = tk.Label(window, text="Username:")
    username_label.pack()
    username_entry = tk.Entry(window)
    username_entry.pack()

    password_label = tk.Label(window, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(window, show="*")
    password_entry.pack()

    show_artikel_button = tk.Button(window, text='Artikelliste anzeigen', command=show_artikel_button_clicked)

    angebot_erstellen_button = tk.Button(window, text='Angebot erstellen', command=angebot_erstellen_submit_button_clicked)

    geld_hinzufuegen_button = tk.Button(window, text='Geld hinzufügen', command=geld_hinzufuegen_button_clicked)

    logout_button = tk.Button(window, text='Logout', command=logout)

    back_button_angebot = tk.Button(window, text='Zurück', command=back_angebot)

    back_button_geld = tk.Button(window, text='Zurück', command=back_geld)

    show_gegenstaende_button = tk.Button(window, text='Eigene Gegenstände anzeigen', command=show_gegenstaende_button_clicked)

    show_angebote_button = tk.Button(window, text='Angebote anzeigen', command=show_angebote_button_clicked)


    textbox = tk.Text(window)
    textbox.pack()
    textbox.config(state=tk.DISABLED)

    guthaben_label = tk.Label(window, text="Aktuelles Guthaben: 0 €")
    guthaben_label.pack()

    # Starten des Threads zur Aktualisierung des Guthabens
    guthaben_thread = threading.Thread(target=update_guthaben)
    guthaben_thread.start()

    window.mainloop()

if __name__ == '__main__':
    main()
