import tkinter as tk
from tkinter import messagebox
import threading
import time
from logic import AuctionHouseLogic


class AuctionHouseGUI:
    def __init__(self):
        #erstellt das Grundliegende fenster
        self.logic = AuctionHouseLogic()
        self.window = tk.Tk()
        self.window.title("Auktionshaus")
        self.window.geometry("700x800")

        #hier werden die Buttons erstellt und den wird übergeben was sie anzeigen sollen und was sie machen sollen
        #wenn man sie klickt

        #Knopf fürs registrieren
        self.register_button = tk.Button(self.window, text='Registrieren', command=self.register_button_clicked)
        self.register_button.pack()

        #Knopf für login
        self.login_button = tk.Button(self.window, text='Login', command=self.login_button_clicked)
        self.login_button.pack()

        #Eingabefenster für Username und Passwort
        self.username_label = tk.Label(self.window, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.window)
        self.username_entry.pack()

        self.password_label = tk.Label(self.window, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.window, show="*")
        self.password_entry.pack()

        #Knopf um Artikel und der momentane Kurs zu zeigen
        self.show_artikel_button = tk.Button(self.window, text='Artikelliste anzeigen',
                                             command=self.show_artikel_button_clicked)

        #Knopf um ein Angebot zu erstellen
        self.angebot_erstellen_button = tk.Button(self.window, text='Angebot erstellen',
                                                  command=self.show_angebot_erstellen_form)

        #Knopf um Geld hinzuzufügen
        self.geld_hinzufuegen_button = tk.Button(self.window, text='Geld hinzufügen',
                                                 command=self.geld_hinzufuegen_button_clicked)

        #Knopf um Geld abzuheben
        self.geld_abheben_button = tk.Button(self.window, text='Geld abheben',
                                                 command=self.geld_abheben_button_clicked)

        #Knopf um sich auszuloggen
        self.logout_button = tk.Button(self.window, text='Logout', command=self.logout)

        #Alle Zurück Knöpfe
        self.back_button_angebot = tk.Button(self.window, text='Zurück', command=self.back_angebot)
        self.back_button_geld = tk.Button(self.window, text='Zurück', command=self.back_geld)
        self.back_button_gegenstand_holen = tk.Button(self.window, text='Zurück', command=self.back_gegenstand_holen)
        self.back_button_angebot_kaufen = tk.Button(self.window, text='Zurück', command=self.back_angebot_kaufen)
        self.back_button_geld_abheben = tk.Button(self.window, text='Zurück', command=self.back_geld_abheben)

        #Knop um eigene Gegenstände anzuzeigen
        self.show_gegenstaende_button = tk.Button(self.window, text='Eigene Gegenstände anzeigen',
                                                  command=self.show_gegenstaende_button_clicked)

        #Knopf um alle Angebote anzuzeigen
        self.show_angebote_button = tk.Button(self.window, text='Angebote anzeigen',
                                               command=self.show_angebote_button_clicked)

        #Knopf um sich einen Gegenstand vom Server zu kaufen
        self.gegenstand_holen_button = tk.Button(self.window, text='Gegenstände vom Server kaufen',
                                                  command=self.show_gegenstand_holen_button_clicked)

        #Knopf um sich ein Angebot von einem anderen User zu kaufen
        self.angebot_kaufen_button = tk.Button(self.window, text='Angebote kaufen',
                                                  command=self.show_angebot_kaufen_button_clicked)

        self.textbox = tk.Text(self.window)
        self.textbox.pack()
        self.textbox.config(state=tk.DISABLED)

        #Aktuelles Guthaben wird mittels thread angezeigt
        self.guthaben_label = tk.Label(self.window, text="Aktuelles Guthaben: 0 €")
        self.guthaben_label.pack()

        self.guthaben_thread = None

    def run(self):
        self.window.mainloop()

    #führt die register funktion aus logic aus und übergibt Eingabe für Username und Passwort und gibt die Message aus
    def register_button_clicked(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        message = self.logic.register(username, password)
        self.add_message(message)

    #führt login funktion aus logic aus mit Username und Passwort welche hier übergeben werden
    def login_button_clicked(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        message = self.logic.login(username, password)
        if message == 'Login fehlgeschlagen':
            # Fehlermeldung anzeigen
            messagebox.showerror("Fehler", "Anmeldung fehlgeschlagen. Bitte überprüfen Sie Ihre Anmeldedaten.")
        #gibt die Nachricht aus der logic Funktion aus und entfernt die Knöpfe Login und Register und die Eingabefelder 
        #und lässt alle anderen Knöpfe anzeigen
        else:
            self.add_message(message)
            self.register_button.pack_forget()
            self.login_button.pack_forget()
            self.username_label.pack_forget()
            self.username_entry.pack_forget()
            self.password_label.pack_forget()
            self.password_entry.pack_forget()
            self.show_artikel_button.pack()
            self.geld_hinzufuegen_button.pack()
            self.geld_abheben_button.pack()
            self.show_gegenstaende_button.pack()
            self.gegenstand_holen_button.pack()
            self.show_angebote_button.pack()
            self.angebot_erstellen_button.pack()
            self.angebot_kaufen_button.pack()
            self.logout_button.pack()

    #gibt das Array welches in der logic Funktion vom Server bekommen wird aus
    def show_artikel_button_clicked(self):
        artikel = self.logic.get_artikel_list()
        if artikel:
            message = "Artikelliste:\n"
            for a in artikel:
                message += f"- {a}\n"
            self.add_message(message)
        else:
            self.add_message("Keine Artikel verfügbar.")

    #Entfernt alle Knöpfe des Menüs und fügt Zurück Knopf Eingabefelder(für Artikelname und Preis) 
    # und einen Bestätigungsknopf hinuz und zeigt alle Gegenstände die man besitzt nochmal an
    def show_angebot_erstellen_form(self):
        self.show_artikel_button.pack_forget()
        self.angebot_erstellen_button.pack_forget()
        self.geld_hinzufuegen_button.pack_forget()
        self.logout_button.pack_forget()
        self.show_gegenstaende_button.pack_forget()
        self.show_angebote_button.pack_forget()
        self.gegenstand_holen_button.pack_forget()
        self.angebot_kaufen_button.pack_forget()
        self.geld_abheben_button.pack_forget()

        self.show_gegenstaende_button_clicked()

        self.angebot_erstellen_label = tk.Label(self.window, text="Angebot erstellen")
        self.angebot_erstellen_label.pack()

        self.artikelname_label = tk.Label(self.window, text="Artikelname:")
        self.artikelname_label.pack()
        self.artikelname_entry = tk.Entry(self.window)
        self.artikelname_entry.pack()

        self.preis_label = tk.Label(self.window, text="Preis:")
        self.preis_label.pack()
        self.preis_entry = tk.Entry(self.window)
        self.preis_entry.pack()

        self.angebot_erstellen_submit_button = tk.Button(self.window, text='Angebot erstellen',
                                                         command=self.angebot_erstellen_submit_button_clicked)
        self.angebot_erstellen_submit_button.pack()
        self.back_button_angebot.pack()

    #fügt die Funktion um ein Angebot zu erstellen aus der logic aus und löscht die Einträge der 
    # Eingabefelder für Artikelnamen und Preis
    def angebot_erstellen_submit_button_clicked(self):
        artikelname = self.artikelname_entry.get()
        preis = self.preis_entry.get()
        message = self.logic.angebot_erstellen(artikelname, preis)
        if message == 'Angebot erstellt':
            self.add_message("Angebot erstellt")

        elif message == 'Gegenstand nicht im Besitz':
            self.add_message("Gegenstand nicht im Besitz")
            
        elif message == 'Fehler beim erstellen des Angebots':
            self.add_message("Fehler beim erstellen des Angebots")

        self.artikelname_entry.delete(0, tk.END)
        self.preis_entry.delete(0, tk.END)

    #Entfernt alle Knöpfe des Hauptmenüs und fügt die Knöpfe und Eingabefelder für Username, Passwort, register 
    # und login hinzu und löscht den Text der im Ausgabefeld steht und löscht die Eingaben von den Eingabefeldern 
    # von Username und Passwort
    def logout(self):
        self.textbox.config(state=tk.NORMAL)  # Aktiviere das Textfeld für Bearbeitung
        self.textbox.delete("1.0", tk.END)  # Löscht den Inhalt des Textfelds
        self.textbox.config(state=tk.DISABLED)  # Deaktiviere das Textfeld
        message = self.logic.logout()
        self.add_message(message)
        self.logout_button.pack_forget()
        self.show_artikel_button.pack_forget()
        self.gegenstand_holen_button.pack_forget()
        self.angebot_erstellen_button.pack_forget()
        self.geld_hinzufuegen_button.pack_forget()
        self.show_gegenstaende_button.pack_forget()
        self.show_angebote_button.pack_forget()
        self.angebot_kaufen_button.pack_forget()
        self.geld_abheben_button.pack_forget()
        self.register_button.pack()
        self.login_button.pack()
        self.username_label.pack()
        self.username_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)


    #Entfernt alle Knöpfe des Menüs und fügt das Eingabefeld und den Bestätigungsknopf für Betrag hinzu 
    # und eine Zurück Knopf um wieder ins Hauptmenü zu kommen
    def geld_hinzufuegen_button_clicked(self):
        self.logout_button.pack_forget()
        self.show_artikel_button.pack_forget()
        self.angebot_erstellen_button.pack_forget()
        self.geld_hinzufuegen_button.pack_forget()
        self.show_gegenstaende_button.pack_forget()
        self.show_angebote_button.pack_forget()
        self.gegenstand_holen_button.pack_forget()
        self.angebot_kaufen_button.pack_forget()
        self.geld_abheben_button.pack_forget()

        self.geld_hinzufuegen_label = tk.Label(self.window, text="Geld hinzufügen")
        self.geld_hinzufuegen_label.pack()

        self.betrag_label = tk.Label(self.window, text="Betrag:")
        self.betrag_label.pack()
        self.betrag_entry = tk.Entry(self.window)
        self.betrag_entry.pack()

        self.geld_hinzufuegen_submit_button = tk.Button(self.window, text='Geld hinzufügen',
                                                        command=self.validate_and_hinzufuegen)
        self.geld_hinzufuegen_submit_button.pack()
        self.back_button_geld.pack()

    #Prüft ob die Eingabe die bei Betrag hinzufügen eingegeben wird Gültig ist also Positiv und eine Zahl, sonst wird eine 
    # Fehlermeldung als Pop-up angezeigt und löscht den Inhalt des Eingabefelds
    def validate_and_hinzufuegen(self):
        betrag = self.betrag_entry.get()
        try:
            betrag = float(betrag)
            if betrag > 0:
                self.logic.geld_hinzufuegen(betrag)
                self.add_message(f"Guthaben in Höhe von {betrag}€ zum Konto hinzugefügt.")
            else:
                messagebox.showerror("Fehler", "Bitte geben Sie einen positiven Betrag ein.")
        except ValueError:
            messagebox.showerror("Fehler", "Bitte geben Sie eine gültige Zahl ein.")

        self.betrag_entry.delete(0, tk.END)

    #Prüft ob die Eingabe die bei Betrag auszahlen eingegeben wird Gültig ist also Positiv, eine Zahl und nicht 
    # größer als da momentane Guthaben, sonst wird eine Fehlermeldung als Pop-up angezeigt und löscht den Inhalt 
    # des Eingabefelds
    def validate_and_hinzufuegen2(self):
        betrag = self.betrag_abheben_entry.get()
        try:
            betrag = float(betrag)
            if betrag > 0:
                if self.logic.get_guthaben() >= betrag:
                    self.logic.geld_abheben(betrag)
                    self.add_message(f"Guthaben in Höhe von {betrag}€ ausgezahlt")
                else:
                    messagebox.showerror("Fehler", "Nicht genug Geld auf dem Konto.")
            else:
                messagebox.showerror("Fehler", "Bitte geben Sie einen positiven Betrag ein.")
        except ValueError:
            messagebox.showerror("Fehler", "Bitte geben Sie eine gültige Zahl ein.")

        self.betrag_abheben_entry.delete(0, tk.END)

    #Entfernt alle Knöpfe des Menüs und fügt ein Eingabefeld für Betrag, einen Bestätigungsknopf und 
    # eine Zurückknopf hinzu
    def geld_abheben_button_clicked(self):
        self.logout_button.pack_forget()
        self.show_artikel_button.pack_forget()
        self.angebot_erstellen_button.pack_forget()
        self.geld_hinzufuegen_button.pack_forget()
        self.show_gegenstaende_button.pack_forget()
        self.show_angebote_button.pack_forget()
        self.gegenstand_holen_button.pack_forget()
        self.angebot_kaufen_button.pack_forget()
        self.geld_abheben_button.pack_forget()

        self.geld_abheben_label = tk.Label(self.window, text="Geld abheben")
        self.geld_abheben_label.pack()

        self.betrag_abheben_label = tk.Label(self.window, text="Betrag:")
        self.betrag_abheben_label.pack()
        self.betrag_abheben_entry = tk.Entry(self.window)
        self.betrag_abheben_entry.pack()

        self.geld_abheben_submit_button = tk.Button(self.window, text='Geld abheben',
                                                        command=self.validate_and_hinzufuegen2)
        self.geld_abheben_submit_button.pack()
        self.back_button_geld_abheben.pack()

    #Entfernt alle Knöpfe und Eingabefelder die von der Funktion geld_abheben hinzugefügt werden und stellt das Menü 
    # wieder her indem alle relevanten Knöpfe angezeigt werden
    def back_geld_abheben(self):
        self.back_button_geld_abheben.pack_forget()
        self.show_artikel_button.pack()
        self.geld_hinzufuegen_button.pack()
        self.geld_abheben_button.pack()
        self.show_gegenstaende_button.pack()
        self.gegenstand_holen_button.pack()
        self.show_angebote_button.pack()
        self.angebot_erstellen_button.pack()
        self.angebot_kaufen_button.pack()
        self.logout_button.pack()

        # Ausblenden der zusätzlichen Elemente
        self.geld_abheben_submit_button.pack_forget()
        self.betrag_abheben_entry.pack_forget()
        self.geld_abheben_label.pack_forget()
        self.betrag_abheben_label.pack_forget()

    #Entfernt alle Knöpfe und Eingabefelder die von der Funktion geld_hinzufügen hinzugefügt werden und stellt das Menü 
    # wieder her indem alle relevanten Knöpfe angezeigt werden
    def back_geld(self):
        self.back_button_geld.pack_forget()
        self.show_artikel_button.pack()
        self.geld_hinzufuegen_button.pack()
        self.geld_abheben_button.pack()
        self.show_gegenstaende_button.pack()
        self.gegenstand_holen_button.pack()
        self.show_angebote_button.pack()
        self.angebot_erstellen_button.pack()
        self.angebot_kaufen_button.pack()
        self.logout_button.pack()

        # Ausblenden der zusätzlichen Elemente
        self.geld_hinzufuegen_submit_button.pack_forget()
        self.betrag_entry.pack_forget()
        self.geld_hinzufuegen_label.pack_forget()
        self.betrag_label.pack_forget()

    #Entfernt alle Knöpfe und Eingabefelder die von der Funktion angebot_erstellen hinzugefügt werden und stellt das Menü 
    # wieder her indem alle relevanten Knöpfe angezeigt werden
    def back_angebot(self):
        self.back_button_angebot.pack_forget()
        self.show_artikel_button.pack()
        self.geld_hinzufuegen_button.pack()
        self.geld_abheben_button.pack()
        self.show_gegenstaende_button.pack()
        self.gegenstand_holen_button.pack()
        self.show_angebote_button.pack()
        self.angebot_erstellen_button.pack()
        self.angebot_kaufen_button.pack()
        self.logout_button.pack()

        # Ausblenden der zusätzlichen Elemente
        self.angebot_erstellen_label.pack_forget()
        self.artikelname_label.pack_forget()
        self.artikelname_entry.pack_forget()
        self.preis_label.pack_forget()
        self.preis_entry.pack_forget()
        self.angebot_erstellen_submit_button.pack_forget()

    #Entfernt alle Knöpfe und Eingabefelder die von der Funktion gegenstand_holen hinzugefügt werden und stellt das Menü 
    # wieder her indem alle relevanten Knöpfe angezeigt werden
    def back_gegenstand_holen(self):
        self.show_artikel_button.pack()
        self.geld_hinzufuegen_button.pack()
        self.geld_abheben_button.pack()
        self.show_gegenstaende_button.pack()
        self.gegenstand_holen_button.pack()
        self.show_angebote_button.pack()
        self.angebot_erstellen_button.pack()
        self.angebot_kaufen_button.pack()
        self.logout_button.pack()

        # Ausblenden der zusätzlichen Elemente
        self.gegenstand_holen_label.pack_forget()
        self.gegenstand_label.pack_forget()
        self.gegenstand_entry.pack_forget()
        self.gegenstand_holen_submit_button.pack_forget()
        self.back_button_gegenstand_holen.pack_forget()

    #Entfernt alle Knöpfe und Eingabefelder die von der Funktion angebot_kaufen hinzugefügt werden und stellt das Menü 
    # wieder her indem alle relevanten Knöpfe angezeigt werden
    def back_angebot_kaufen(self):
        self.show_artikel_button.pack()
        self.geld_hinzufuegen_button.pack()
        self.geld_abheben_button.pack()
        self.show_gegenstaende_button.pack()
        self.gegenstand_holen_button.pack()
        self.show_angebote_button.pack()
        self.angebot_erstellen_button.pack()
        self.angebot_kaufen_button.pack()
        self.logout_button.pack()

        # Ausblenden der zusätzlichen Elemente
        self.angebot_kaufen_label.pack_forget()
        self.angebot_label.pack_forget()
        self.angebot_entry.pack_forget()
        self.angebot_kaufen_submit_button.pack_forget()
        self.back_button_angebot_kaufen.pack_forget()

    #Gibt den Inhalt des Array an welches alle Gegenstände die man besitzt beinhaltet
    def show_gegenstaende_button_clicked(self):
        gegenstaende = self.logic.get_gegenstaende_einer_person()
        if gegenstaende:
            message = "Eigene Gegenstände:\n"
            for g in gegenstaende:
                message += f"- {g}\n"
            self.add_message(message)
        else:
            self.add_message("Keine eigenen Gegenstände vorhanden.")

    #Gibt den Inhalt des Array wieder welches man in der logic bekommt und dieses Array beinhaltet alle Angebote
    def show_angebote_button_clicked(self):
        angebote = self.logic.get_angebote_print()
        if angebote:
            message = "Momentane Angebote:\n"
            for a in angebote:
                message += f"- {a}\n"
            self.add_message(message)
        else:
            self.add_message("Keine Angebote vorhanden.")

    #hier werden die Einstellungen für die Anzeigebox eingestellt(automatisches Scrollen, Text wird unten eingefügt)
    def add_message(self, message):
        self.textbox.config(state=tk.NORMAL)
        if message is not None:
            self.textbox.insert(tk.END, message + "\n")
            self.textbox.see(tk.END)  # Scrollt zum Ende des Textfelds
        self.textbox.config(state=tk.DISABLED)

    #Hier wird das aktuelle Guthaben immer wieder in 5 Sekunden abständen abgefragt und im Client angezeigt
    def update_guthaben(self):
        while True:
            guthaben = self.logic.get_guthaben()
            if guthaben is not None:
                self.guthaben_label.config(text="Aktuelles Guthaben: {} €".format(guthaben))
            else:
                self.guthaben_label.config(text="")
            time.sleep(3)  # Guthaben alle 5 Sekunden aktualisieren

    #hier wird der thread gestartet für die Funktion Guthaben update
    def start_guthaben_thread(self):
        self.guthaben_thread = threading.Thread(target=self.update_guthaben)
        self.guthaben_thread.start()

    #alle Knöpfe vom Menü werden vergessen und es wird ein Eingabefeld für den Gegenstand den man vom Server kaufen will 
    # erstellt, einen Bestätigungsknopf und einen Zurückknopf mit dem man wieder das Menü wiederherstellt
    def show_gegenstand_holen_button_clicked(self):
        self.logout_button.pack_forget()
        self.show_artikel_button.pack_forget()
        self.angebot_erstellen_button.pack_forget()
        self.geld_hinzufuegen_button.pack_forget()
        self.show_gegenstaende_button.pack_forget()
        self.show_angebote_button.pack_forget()
        self.gegenstand_holen_button.pack_forget()
        self.angebot_kaufen_button.pack_forget()
        self.geld_abheben_button.pack_forget()

        self.show_artikel_button_clicked()

        self.gegenstand_holen_label = tk.Label(self.window, text="Gegenstand vom Server kaufen")
        self.gegenstand_holen_label.pack()

        self.gegenstand_label = tk.Label(self.window, text="Gegenstand:")
        self.gegenstand_label.pack()
        self.gegenstand_entry = tk.Entry(self.window)
        self.gegenstand_entry.pack()

        self.gegenstand_holen_submit_button = tk.Button(self.window, text='Gegenstand kaufen',
                                                        command=self.gegenstand_holen_submit_button_clicked)
        self.gegenstand_holen_submit_button.pack()
        self.back_button_gegenstand_holen.pack()

    #es werden erst alle Gegenstände, die Verfügbarkeit und der Peis angezeigt und dann mit der Eingabe für Gegenstand die 
    # Funktion aus der logic aufgerufen und für die verschiedenen Response Codes eine Ausgabe ausgegeben
    # und der Inhalt des Eingabefelds wird gelöscht
    def gegenstand_holen_submit_button_clicked(self):
        artikelname = self.gegenstand_entry.get()
        message = self.logic.gegenstand_holen(artikelname)
        if message == 'Gegenstand erfolgreich gekauft':

            self.add_message("Gegenstand erfolgreich gekauft")

        elif message == 'Gegenstand nicht vorrätig oder unzureichendes Guthaben':

            self.add_message("Gegenstand nicht vorrätig oder unzureichendes Guthaben")

        elif message == 'Fehler beim Holen des Gegenstands':

            self.add_message("Fehler beim Holen des Gegenstands")
        self.gegenstand_entry.delete(0, tk.END)

    #alle Knöpfe vom Menü werden vergessen und es wird ein Eingabefeld für die Angebotsnummer erstellt welches man kaufen 
    # will , einen Bestätigungsknopf und einen Zurückknopf mit dem man wieder das Menü wiederherstellt und es werden 
    #alle Angebote angezeigt die existieren
    def show_angebot_kaufen_button_clicked(self):
        self.logout_button.pack_forget()
        self.show_artikel_button.pack_forget()
        self.angebot_erstellen_button.pack_forget()
        self.geld_hinzufuegen_button.pack_forget()
        self.show_gegenstaende_button.pack_forget()
        self.show_angebote_button.pack_forget()
        self.gegenstand_holen_button.pack_forget()
        self.angebot_kaufen_button.pack_forget()
        self.geld_abheben_button.pack_forget()

        self.show_angebote_button_clicked()

        self.angebot_kaufen_label = tk.Label(self.window, text="Angebot kaufen")
        self.angebot_kaufen_label.pack()

        self.angebot_label = tk.Label(self.window, text="Angebotsnummer:")
        self.angebot_label.pack()
        self.angebot_entry = tk.Entry(self.window)
        self.angebot_entry.pack()

        self.angebot_kaufen_submit_button = tk.Button(self.window, text='Gegenstand kaufen',
                                                        command=self.angebot_kaufen_submit_button_clicked)

        self.angebot_kaufen_submit_button.pack()
        self.back_button_angebot_kaufen.pack()

    #es werden erst alle Angebote angezeigt und dann mit der Eingabe für Angebot die 
    # Funktion aus der logic aufgerufen und für die verschiedenen Response Codes eine Ausgabe ausgegeben 
    # und der Inhalt des Eingabefelds wird gelöscht
    def angebot_kaufen_submit_button_clicked(self):
        nummer = self.angebot_entry.get()
        message = self.logic.angebot_kaufen(nummer)
        if message == 'Kauf erfolgreich':

            self.add_message("Angebot erfolgreich gekauft")

        elif message == 'Fehler beim kaufen':

            self.add_message("Angebot bereits verkauft oder Angebot nicht vorhanden")

        elif message == 'Unbekannter Fehler beim kaufen eines Angebotes':


            self.add_message("Fehler beim Kaufen des Angebotes")
        self.angebot_entry.delete(0, tk.END)

        




if __name__ == '__main__':
    auction_house_gui = AuctionHouseGUI()
    auction_house_gui.start_guthaben_thread()
    auction_house_gui.run()

