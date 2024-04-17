#pragma once

#include <iostream>
#include <vector>
#include <random>
#include "/home/odin/Schreibtisch/poose3/include/artikel.hpp"
#include "/home/odin/Schreibtisch/poose3/include/haendler.hpp"

/**
 * @namespace Handelsplatz
 * @brief Ein Namespace, der Klassen für den Handelsplatz enthält.
 */
namespace Handelsplatz {
    /**
     * @brief Eine Klasse, die den Markt repräsentiert.
     */
    class Markt {
    public:
        /**
         * @brief Gibt eine Liste der verfügbaren Artikel zurück.
         * @return Ein Vektor mit den Artikeln.
         */
        std::vector<Artikel> get_artikel_list();

        /**
         * @brief Erstellt einen neuen Händler mit dem angegebenen Benutzernamen.
         * @param benutzernamen Der Benutzername des neuen Händlers.
         */
        void haendler_erstellen(std::string benutzernamen);


        /**
         * @brief Gibt eine Liste der aktuellen Angebote zurück.
         * @return Ein Vektor mit den Angeboten.
         */
        std::vector<Angebot> return_angebote();

        /**
         * @brief Erstellt ein neues Angebot.
         * @param verkaefer Der Verkäufer des Angebots.
         * @param gegenstand Der Name des Gegenstands im Angebot.
         * @param preis Der Preis des Angebots.
         * @return Die Nummer des erstellten Angebots.
         */
        int angebot_erstellen(std::string verkaefer, std::string gegenstand, double preis);

        /**
         * @brief Gibt eine Liste der Artikelnamen zurück.
         * @return Ein Vektor mit den Namen der Artikel.
         */
        std::vector<std::string> artikel_print();

        /**
         * @brief Gibt eine Liste der Angebotdetails zurück.
         * @return Ein Vektor mit den Angebotdetails.
         */
        std::vector<std::string> angebote_print();

        /**
         * @brief Verkauft einen Artikel an einen Käufer.
         * @param kaeufer Der Käufer des Artikels.
         * @param nummer Die Nummer des Angebots.
         */
        void verkaufen(std::string kaeufer, int nummer);

        /**
         * @brief Gibt den Index einer Person in der Händlerliste zurück.
         * @param person Der Name der Person.
         * @return Der Index der Person oder -1, wenn die Person nicht gefunden wurde.
         */
        int get_index_person(std::string person);

        /**
         * @brief Holt einen Gegenstand von einer Person.
         * @param name Der Name der Person.
         * @param gegenstand Der Name des Gegenstands.
         */
        void gegenstaende_holen(std::string name, std::string gegenstand);

        /**
         * @brief Fügt einer Person Geld hinzu.
         * @param person Der Name der Person.
         * @param betrag Der Betrag, der hinzugefügt werden soll.
         */
        void geld_hinzufuegen(std::string person, double betrag);

        /**
         * @brief Gibt das Guthaben einer Person zurück.
         * @param name Der Name der Person.
         * @return Das Guthaben der Person.
         */
        double guthaben_einer_person(std::string name);



        /**
         * @brief Zieht ein Angebot zurück.
         * @param nummer Die Nummer des Angebots.
         * @return True, wenn das Angebot erfolgreich zurückgezogen wurde, sonst False.
         */
        void angebot_zurueckziehen(int nummer, std::string ersteller);

        /**
         * @brief Gibt die Anzahl der verfügbaren Gegenstände mit einem bestimmten Namen zurück.
         * @param a Der Name des Gegenstands.
         * @return Die Anzahl der verfügbaren Gegenstände.
         */
        int anz_gegenstand(std::string a);

        /**
         * @brief Gibt eine Liste der Gegenstände einer Person zurück.
         * @param person Der Name der Person.
         * @return Ein Vektor mit den Namen der Gegenstände.
         */
        std::vector<std::string> gegenstaende_einer_person(std::string person);

        /**
         * @brief Aktualisiert die Preise der Artikel.
         * @param zeit Die vergangene Zeit.
         */
        void preise_aktualisieren(int zeit);

        /**
         * @brief Gibt den Preis eines bestimmten Angebots zurück.
         * @param nummer Die Nummer des Angebots.
         * @return Der Preis des Angebots.
         */
        double return_angebot_preis(int nummer);

        /**
         * @brief Gibt den Preis eines bestimmten Gegenstands zurück.
         * @param gegenstand Der Name des Gegenstands.
         * @return Der Preis des Gegenstands.
         */
        int preis_von_gegenstand(std::string gegenstand);

        /**
         * @brief Überprüft, ob eine Person einen bestimmten Gegenstand besitzt.
         * @param name Der Name der Person.
         * @param gegenstand Der Name des Gegenstands.
         * @return True, wenn die Person den Gegenstand besitzt, sonst False.
         */
        bool besitzt_person_gegenstand(std::string name, std::string gegenstand);


        void geld_auszahlen(std::string name, double betrag);

        std::vector<Artikel> get_artikel_array() {
            return artikel_liste;
        }

        std::vector<Angebot> get_angebote_array() {
            return angebote;
        }
        
    private:
        /**
         * @brief Fügt einen neuen Händler zur Händlerliste hinzu.
         * @param neuer_handler Der neue Händler.
         */
        void neuer_handler(Handelsplatz::Haendler neuer_handler);

        /**
         * @brief Löscht ein Angebot.
         * @param nummer Die Nummer des Angebots.
         */
        void angebot_loeschen(int nummer);


        std::vector<Artikel> artikel_liste { /**< Die Liste der verfügbaren Artikel. */
            Artikel("Haus", 40000),
            Artikel("Auto", 200),
            Artikel("Uhr", 500),
            Artikel("Fahrrad", 500),
            Artikel("Bild", 1000),
            Artikel("Zug", 6000),
            Artikel("Computer", 900),
            Artikel("Ball", 7000)
        };

        std::vector<Haendler> haendler_liste; /**< Die Liste der Händler. */
        std::vector<Angebot> angebote; /**< Die Liste der Angebote. */
        
    };
}
