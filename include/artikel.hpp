#pragma once
#include <iostream>
#include <vector>
#include <random>
#include <cmath>


/**
 * @namespace Handelsplatz
 * @brief Ein Namespace, der Klassen für den Handelsplatz enthält.
 */
namespace Handelsplatz {

    /**
     * @brief Eine Klasse, die einen Artikel repräsentiert.
     */
    class Artikel {
    public:
        /**
         * @brief Konstruktor für die Artikelklasse.
         * @param name_ Der Name des Artikels.
         * @param wert_ Der Wert des Artikels.
         */
        Artikel(std::string name_, double wert_) : name(name_), wert(wert_) {}

        /**
         * @brief Gibt den Namen des Artikels zurück.
         * @return Der Name des Artikels.
         */
        std::string get_name_();

        /**
         * @brief Setzt den Namen des Artikels.
         * @param name_ Der Name des Artikels.
         */
        void set_name(std::string name_);

        /**
         * @brief Gibt den Wert des Artikels zurück.
         * @return Der Wert des Artikels.
         */
        double get_wert_();

        /**
         * @brief Setzt den Wert des Artikels.
         * @param wert_ Der Wert des Artikels.
         */
        void set_wert(double wert_);

        /**
         * @brief Gibt die Streuung des Artikels zurück.
         * @return Die Streuung des Artikels.
         */
        double get_streuung() {
            return streuung;
        }

        /**
         * @brief Gibt die Tendenz des Artikels zurück.
         * @return Die Tendenz des Artikels.
         */
        double get_tendenz() {
            return tendenz;
        }

        /**
         * @brief Berechnet den Kursverlauf des Artikels.
         * @param tendenz Die Tendenz des Kursverlaufs.
         * @param streuung Die Streuung des Kursverlaufs.
         * @param dt Der Zeitintervall für die Kursberechnung.
         * @param start Der Startwert des Kurses.
         * @param anzahl Die Anzahl der Kurswerte.
         * @return Ein Vektor mit den Kurswerten.
         */
        std::vector<double> kursverlauf(double tendenz, double streuung, double dt, double start, int anzahl);

        /**
         * @brief Aktualisiert den Kurs des Artikels.
         */
        void aktualisiere_kurs();

        /**
         * @brief Gibt den aktuellen Kurs des Artikels zurück.
         * @return Der aktuelle Kurs des Artikels.
         */
        double aktueller_kurs() {
            wert = kurs[kurs.size()-1];
            return kurs[kurs.size()-1];
        }

        /**
         * @brief Verringert die Anzahl des Artikels um eins.
         */
        void anz_minus_eins() {
            anz--;
        }

        /**
         * @brief Gibt die Anzahl des Artikels zurück.
         * @return Die Anzahl des Artikels.
         */
        int get_anz() {
            return anz;
        }

    private:
        std::string name; /**< Der Name des Artikels. */
        double wert = 0; /**< Der Wert des Artikels. */
        double tendenz = 0.3 * (2 * static_cast<double>(rand()) / RAND_MAX - 1.0); /**< Die Tendenz des Artikels. */
        double streuung = 0.8; /**< Die Streuung des Artikels. */
        double dt = 0.001; /**< Das Zeitintervall für die Kursberechnung. */
        std::vector<double> kurs; /**< Ein Vektor mit den Kurswerten des Artikels. */
        int anz = 10; /**< Die Anzahl des Artikels. */

    };

    /**
     * @brief Eine Klasse, die ein Angebot repräsentiert.
     */
    class Angebot {
    public:
        /**
         * @brief Konstruktor für die Angebotklasse.
         * @param ersteller_ Der Ersteller des Angebots.
         * @param objekt_ Der Name des Objekts.
         * @param wert_ Der Wert des Objekts.
         * @param art_num_ Die Artikelnummer des Angebots.
         */
        Angebot(std::string ersteller_, std::string objekt_, double wert_, int art_num_) : ersteller(ersteller_), obj(objekt_), wert(wert_), art_num(art_num_) {}

        /**
         * @brief Gibt den Ersteller des Angebots zurück.
         * @return Der Ersteller des Angebots.
         */
        std::string get_ersteller();

        /**
         * @brief Gibt den Namen des Objekts zurück.
         * @return Der Name des Objekts.
         */
        std::string get_obj();

        /**
         * @brief Gibt den Wert des Objekts zurück.
         * @return Der Wert des Objekts.
         */
        double get_wert();

        /**
         * @brief Gibt die Artikelnummer des Angebots zurück.
         * @return Die Artikelnummer des Angebots.
         */
        int get_art_num() {
            return art_num;
        }

    private:
        std::string ersteller; /**< Der Ersteller des Angebots. */
        std::string obj; /**< Der Name des Objekts. */
        double wert; /**< Der Wert des Objekts. */
        int art_num; /**< Die Artikelnummer des Angebots. */
    };

}
