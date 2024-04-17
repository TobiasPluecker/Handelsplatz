#pragma once
#include "/home/odin/Schreibtisch/poose3/include/handelsplatz.hpp"


/**
 * @brief Erstellt einen neuen Händler mit dem angegebenen Benutzernamen.
 * 
 * @param benutzername Der Benutzername des neuen Händlers.
 * @throws std::runtime_error Wenn der angegebene Benutzername bereits existiert.
 */
void Handelsplatz::Markt::haendler_erstellen(std::string benutzername) {
    try {
        for (int i = 0; i < haendler_liste.size(); i++) {
            if (haendler_liste[i].retrun_benutzername() == benutzername) {
                throw std::runtime_error("Benutzername existiert bereits.");
            }
        }
        
        Haendler temp = Haendler(benutzername);
        neuer_handler(temp);
    } catch (const std::exception& e) {
        std::cerr << "Fehler: " << e.what() << std::endl;
    }
}


/**
 * @brief Fügt einen neuen Händler zur Händlerliste hinzu.
 * @param neuer_handler Der neue Händler, der hinzugefügt werden soll.
 */
void Handelsplatz::Markt::neuer_handler(Handelsplatz::Haendler neuer_handler) {
    haendler_liste.push_back(neuer_handler);
}

/**
 * @brief Gibt ein Array mit allen Artikeln und deren aktuellen Preisen zurück.
 * @return Das Array.
 */
std::vector<Handelsplatz::Artikel> Handelsplatz::Markt::get_artikel_list() {
    return artikel_liste;
}

/**
 * @brief Gibt ein Array mit allen Angeboten, welche von Händlern erstellt wurden zurück.
 * @return Das Array.
 */
std::vector<Handelsplatz::Angebot> Handelsplatz::Markt::return_angebote() {
    return angebote;
}


/**
 * Erstellt ein neues Angebot auf dem Markt.
 * @param verkaefer Der Benutzername des Verkäufers.
 * @param gegenstand Der Name des angebotenen Gegenstands.
 * @param preis Der Preis des Angebots.
 * @return Die generierte Angebotsnummer.
 * @throws std::runtime_error Wenn keine eindeutige Angebotsnummer generiert werden kann oder wenn der Verkäufer den Gegenstand nicht besitzt.
 */
int Handelsplatz::Markt::angebot_erstellen(std::string verkaefer, std::string gegenstand, double preis) {
    try {
        // Angebotnummer erzeugen
        static bool temp1 = false;
        if (!temp1) {
            std::srand(static_cast<unsigned int>(std::time(nullptr)));
            temp1 = true;
        }

        const int maxVersuche = 100000; // Maximale Anzahl von Versuchen zur Generierung einer eindeutigen Angebotsnummer
        int versuche = 0;
        int zahl;
        bool eindeutig = false;

        while (!eindeutig && versuche < maxVersuche) {
            zahl = std::rand() % 100000;

            // Überprüfen, ob die generierte Zahl bereits als Angebotsnummer existiert
            bool bereitsVorhanden = false;
            for (int i = 0; i < angebote.size(); i++) {
                if (angebote[i].get_art_num() == zahl) {
                    bereitsVorhanden = true;
                    break;
                }
            }

            if (!bereitsVorhanden) {
                eindeutig = true;
            }

            versuche++;
        }

        if (!eindeutig) {
            // Fehler: Es konnte keine eindeutige Angebotsnummer generiert werden
            throw std::runtime_error("Konnte keine eindeutige Angebotsnummer generieren.");
        }

        // Überprüfen, ob die Person den Gegenstand besitzt
        bool besitztGegenstand = false;
        for (int i = 0; i < haendler_liste.size(); i++) {
            if (haendler_liste[i].retrun_benutzername() == verkaefer) {
                if (haendler_liste[i].hat_gegenstand(gegenstand)) {
                    besitztGegenstand = true;
                    break;
                }
            }
        }

        if (!besitztGegenstand) {
            // Fehler: Die Person besitzt den Gegenstand nicht
            throw std::runtime_error("Die Person besitzt den Gegenstand nicht.");
        }

        Angebot temp = Angebot(verkaefer, gegenstand, preis, zahl);
        angebote.push_back(temp);

        for (int i = 0; i < haendler_liste.size(); i++) {
            if (haendler_liste[i].retrun_benutzername() == verkaefer) {
                haendler_liste[i].entferne_gegenstand(gegenstand);
            }
        }

        return zahl;
    } catch (const std::exception& e) {
        
        std::cerr << "Fehler: " << e.what() << std::endl;
        throw; // Weiterwerfen der Ausnahme an die aufrufende Funktion
    }
}



std::vector<std::string> Handelsplatz::Markt::artikel_print() {
    std::vector<std::string> print;
    for (int i = 0; i < artikel_liste.size(); i++) {
        std::string temp = artikel_liste[i].get_name_() + " (verfügbar: " + std::to_string(artikel_liste[i].get_anz()) + ")" + " kostet gerade " + std::to_string(artikel_liste[i].get_wert_());
        print.push_back(temp);
    }
    return print;
}

/**
 * @brief Gibt ein Array mit allen Angeboten, welche von Händlern erstellt wurden zurück.
 * @return Das Array, welches vorgefertigte strings auf deutsch enthält (zum Testen)
 */
std::vector<std::string> Handelsplatz::Markt::angebote_print() {
    std::vector<std::string> print;
    for (int i = 0; i < angebote.size(); i++) {
        std::string temp = "Der Händler " + angebote[i].get_ersteller() + " verkauft " + angebote[i].get_obj() + " (" + std::to_string(angebote[i].get_art_num())+ ") " + " für " + std::to_string(angebote[i].get_wert());
        print.push_back(temp);
        std::cout << temp << std::endl;
    }
    
    if (print.size() > 0) {
        return print;
    } else {
        std::cout << "Zur Zeit existieren keine Angebote." << std::endl;
        return print;
    }
}

/**
 * @brief Verkauft einen Gegenstand an einen Käufer.
 * 
 * @param kaeufer Der Name des Käufers.
 * @param nummer Die Nummer des Angebots, das verkauft werden soll.
 * @throws std::runtime_error Wenn das Angebot nicht gefunden wird oder der Käufer nicht genügend Geld hat.
 */
void Handelsplatz::Markt::verkaufen(std::string kaeufer, int nummer) {
    try {
        int idx = -1;
        for (int i = 0; i < angebote.size(); i++) {
            if (angebote[i].get_art_num() == nummer) {
                idx = i;
                break;
            }
        }
        if (idx == -1) {
            // Fehler: Angebot nicht gefunden
            throw std::runtime_error("Angebot nicht gefunden");
        }
        Angebot gegenstand = angebote[idx];
        double preis = gegenstand.get_wert();
        int idx_kaeufer = get_index_person(kaeufer);
        if (haendler_liste[idx_kaeufer].get_poose_coins() < preis) {
            // Fehler: Käufer hat zu wenig Geld
            throw std::runtime_error("Käufer hat zu wenig Geld");
        }

        std::string verkaefer = angebote[idx].get_ersteller();
        int idx_verkaeufer = get_index_person(verkaefer);
        haendler_liste[idx_kaeufer].gegenstand_erhalten(gegenstand.get_obj());
        haendler_liste[idx_kaeufer].geld_abziehen(preis);
        haendler_liste[idx_verkaeufer].gewinn_erhalten(preis);
        angebot_loeschen(nummer);
    } catch (const std::exception& e) {
        std::cerr << "Fehler: " << e.what() << std::endl;
        throw;
    }
}

/**
 * @brief Gibt den Index der Person in der Händlerliste zurück.
 * 
 * @param person Der Name der Person.
 * @return Der Index der Person in der Händlerliste.
 * @note Falls die Person nicht gefunden wird, wird der Index 0 zurückgegeben und eine Meldung ausgegeben.
 */
int Handelsplatz::Markt::get_index_person(std::string person) {
    for (int i = 0; i < haendler_liste.size(); i++) {
        if (haendler_liste[i].retrun_benutzername() == person) {
            return i;
        }
    }
    std::cout << "Person nicht gefunden!" << std::endl;
        return 0;
}

/**
 * Holt einen Gegenstand für eine bestimmte Person.
 * @param name Der Name der Person.
 * @param gegenstand Der Name des zu holenden Gegenstands.
 */
void Handelsplatz::Markt::gegenstaende_holen(std::string name, std::string gegenstand) {
    double preis = 0;
    int verfuegbareAnzahl = 0;
    for (int i = 0; i < artikel_liste.size(); i++) {
        if (artikel_liste[i].get_name_() == gegenstand) {
            preis = artikel_liste[i].get_wert_();
            verfuegbareAnzahl = artikel_liste[i].get_anz();
            if (verfuegbareAnzahl > 0) {
                artikel_liste[i].anz_minus_eins();
            }
            break;
        }
    }

    if (verfuegbareAnzahl <= 0) {
        // Fehler: Keine verfügbaren Artikel mehr vorhanden
        throw std::runtime_error("Keine verfügbaren Artikel mehr vorhanden.");
    }

    int idx_name = get_index_person(name);
    double pooseCoins = haendler_liste[idx_name].get_poose_coins();
    if (pooseCoins >= preis) {
        haendler_liste[idx_name].geld_abziehen(preis);
        haendler_liste[idx_name].gegenstand_erhalten(gegenstand);
    } else {
        // Fehler: Die Person hat nicht genug Geld, um den Gegenstand zu kaufen
        throw std::runtime_error("Die Person hat nicht genug Geld, um den Gegenstand zu kaufen.");
    }
}

/**
 * @brief Fügt einer Person Geld hinzu.
 * 
 * @param person Der Name der Person.
 * @param betrag Der Betrag, der hinzugefügt werden soll.
 * @throws std::runtime_error Wenn der übergebene Betrag kleiner oder gleich 0 ist.
 * @note Die Funktion ruft die interne Funktion `get_index_person` auf, um den Index der Person in der Händlerliste zu erhalten.
 */
void Handelsplatz::Markt::geld_hinzufuegen(std::string person, double betrag) {
    try {
        if (betrag <= 0) {
            // Fehler: Ungültiger Betrag
            throw std::runtime_error("Ungültiger Betrag. Der Betrag muss größer als 0 sein.");
        }
        
        int idx_name = get_index_person(person);
        haendler_liste[idx_name].geld_einzahlen(betrag);
    } catch (const std::exception& e) {
        std::cerr << "Fehler: " << e.what() << std::endl;
        throw;
    }
}

/**
 * @brief Ruft das Guthaben einer Person ab.
 * 
 * @param name Der Name der Person.
 * @return Das Guthaben der Person.
 * @note Die Funktion ruft die interne Funktion `get_index_person` auf, um den Index der Person in der Händlerliste zu erhalten.
 */
double Handelsplatz::Markt::guthaben_einer_person(std::string name) {
    int idx_name = get_index_person(name);
    return haendler_liste[idx_name].get_poose_coins();
}

/**
 * @brief Löscht ein Angebot anhand seiner Nummer.
 * @param nummer Die Nummer des Angebots, das gelöscht werden soll.
 * @note Die Funktion durchsucht das Angebot-Array nach dem Angebot mit der angegebenen Nummer und tauscht es mit dem letzten Angebot im Array aus.
 * Anschließend wird das letzte Angebot entfernt, um das Array zu verkleinern.
 */
void Handelsplatz::Markt::angebot_loeschen(int nummer) {
    int idx = 0;
    for (int i = 0; i < angebote.size(); i++) {
        if (angebote[i].get_art_num() == nummer) {
            idx = i;
            break;
        }
    }

    Angebot temp = angebote[idx];
    angebote[idx] = angebote[angebote.size()-1];
    angebote.pop_back();    
}

/**
 * @brief Gibt die Liste der Gegenstände zurück, die eine bestimmte Person besitzt.
 * 
 * @param person Der Name der Person.
 * @return Eine Liste der Gegenstände, die die Person besitzt.
 * @note Die Funktion ruft die Methode `artikel_return()` der entsprechenden Person auf, um die Liste der Gegenstände abzurufen.
 * Wenn die Liste nicht leer ist, wird sie zurückgegeben. Andernfalls wird eine Meldung ausgegeben und eine leere Liste zurückgegeben.
 */
std::vector<std::string> Handelsplatz::Markt::gegenstaende_einer_person(std::string person) {
    int idx = get_index_person(person);
    std::vector<std::string> temp = haendler_liste[idx].artikel_return();
    if (temp.size() > 0) {
        return temp;
    } else {
        std::cout << haendler_liste[idx].retrun_benutzername() + " besitzt keine Objekte." << std::endl;
        return temp;
    }
}

/**
 * @brief Zieht ein Angebot zurück, das von einer bestimmten Person erstellt wurde.
 * 
 * @param nummer Die Nummer des Angebots.
 * @param ersteller Der Name des Erstellers des Angebots.
 * @throws std::runtime_error Wenn das Angebot nicht gefunden wurde.
 * @note Die Funktion sucht das Angebot mit der angegebenen Nummer und dem angegebenen Ersteller und zieht es zurück.
 * Der Gegenstand des Angebots wird an den Ersteller zurückgegeben und das Angebot wird aus der Liste der Angebote gelöscht.
 */
void Handelsplatz::Markt::angebot_zurueckziehen(int nummer, std::string ersteller) {
    try {
        int idx = -1;
        for (int i = 0; i < angebote.size(); i++) {
            if (angebote[i].get_art_num() == nummer && angebote[i].get_ersteller() == ersteller) {
                idx = i;
                break;
            }
        }

        if (idx == -1) {
            // Fehler: Das Angebot mit der angegebenen Nummer und dem angegebenen Ersteller wurde nicht gefunden
            throw std::runtime_error("Das Angebot wurde nicht gefunden.");
        }

        std::string besitzer = angebote[idx].get_ersteller();
        double betrag = angebote[idx].get_wert();
        int idx_person = get_index_person(besitzer);
        std::string a = angebote[idx].get_obj();
        haendler_liste[idx_person].gegenstand_erhalten(a);
        angebot_loeschen(nummer);
    } catch (const std::exception& e) {
        std::cerr << "Fehler: " << e.what() << std::endl;
        throw;
    }
}

/**
 * @brief Aktualisiert die Preise der Artikel über eine bestimmte Zeitperiode.
 * 
 * @param zeit Die Anzahl der Zeitschritte, um die die Preise aktualisiert werden sollen.
 * @note Die Funktion aktualisiert die Preise der Artikel über die angegebene Anzahl von Zeitschritten.
 * Die Preise werden mit einer Streuung von 0.8 und einem Zeitschritt von 0.001 aktualisiert.
 */
void Handelsplatz::Markt::preise_aktualisieren(int zeit) {
    int i = 0;
    double streuung = 0.8;
    double dt = 0.001;
    while (i != zeit) {
        for (int j = 0; j < artikel_liste.size(); j++) {
            artikel_liste[j].aktualisiere_kurs();
        }
        i++;
    }
}


double Handelsplatz::Markt::return_angebot_preis(int nummer) {
    int idx = 0;
    for (int i = 0; i < angebote.size(); i++) {
        if (angebote[i].get_art_num() == nummer) {
            idx = i;
            break;
        }
    }
    double preis = angebote[idx].get_wert();
    return preis;
}

/**
 * @brief Gibt den Preis eines bestimmten Angebots zurück.
 * 
 * @param nummer Die Nummer des Angebots.
 * @return Der Preis des Angebots.
 * @note Die Funktion sucht nach dem Angebot mit der angegebenen Nummer und gibt den Preis zurück.
 */
int Handelsplatz::Markt::anz_gegenstand(std::string a) {
    int idx = 0;
    for (int i = 0; i < artikel_liste.size(); i++) {
        if (artikel_liste[i].get_name_() == a) {
            idx = i;
            break;
        }
    }
    int anz = artikel_liste[idx].get_anz();
    return anz;
}

/**
 * @brief Gibt den Preis eines bestimmten Gegenstands zurück.
 * 
 * @param gegenstand Der Name des Gegenstands.
 * @return Der Preis des Gegenstands.
 * @note Die Funktion sucht nach dem Gegenstand mit dem angegebenen Namen und gibt den Preis zurück.
 */
int Handelsplatz::Markt::preis_von_gegenstand(std::string gegenstand) {
    int idx = 0;
    for (int i = 0; i < artikel_liste.size(); i++) {
        if (artikel_liste[i].get_name_() == gegenstand) {
            idx = i;
            break;
        }
    }
    int preis = artikel_liste[idx].get_wert_();
    return preis;
}

/**
 * @brief Überprüft, ob eine Person einen bestimmten Gegenstand besitzt.
 * 
 * @param name Der Name der Person.
 * @param gegenstand Der Name des Gegenstands.
 * @return True, wenn die Person den Gegenstand besitzt, andernfalls False.
 * @note Die Funktion überprüft, ob die Person mit dem angegebenen Namen den angegebenen Gegenstand besitzt.
 */
bool Handelsplatz::Markt::besitzt_person_gegenstand(std::string name, std::string gegenstand) {
    int idx = get_index_person(name);
    return haendler_liste[idx].hat_gegenstand(gegenstand);
}

/**
 * @brief Zahlt einen bestimmten Geldbetrag an einen Händler aus.
 * 
 * @param name Der Name des Händlers, dem das Geld ausgezahlt werden soll.
 * @param betrag Der auszuzahlende Geldbetrag.
 */
void Handelsplatz::Markt::geld_auszahlen(std::string name, double betrag) {
    try {
        int idx_person = get_index_person(name);
        Haendler haendler = haendler_liste[idx_person];
        double guthaben_temp = haendler.get_poose_coins();
        if (guthaben_temp >= betrag) {
            haendler_liste[idx_person].geld_abziehen(betrag);
        } else {
            // Fehler: Der Händler hat nicht ausreichend Guthaben
            throw std::runtime_error("Der Händler hat nicht ausreichend Guthaben.");
        }
    } catch (const std::exception& e) {
        std::cerr << "Fehler: " << e.what() << std::endl;
        throw;
    }
}

