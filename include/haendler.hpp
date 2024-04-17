#pragma once
#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>


namespace Handelsplatz {
    /**
     * @brief Eine Klasse, die einen Händler repräsentiert.
     */
    class Haendler {
    public:
        /**
         * @brief Konstruktor für die Haendlerklasse.
         * @param haendlername Der Benutzername des Händlers.
         */
        Haendler(const std::string& haendlername) : benutzername(haendlername) {}

        /**
         * @brief Führt eine Einzahlung von Geld in die Poose-Coins des Händlers durch.
         * @param poose_coins_ Der Betrag, der eingezahlt werden soll.
         * @return Der aktualisierte Poose-Coin-Betrag des Händlers.
         */
        double geld_einzahlen(double poose_coins_);

        /**
         * @brief Führt eine Auszahlung von Geld aus den Poose-Coins des Händlers durch.
         * @param poose_coins_ Der Betrag, der ausgezahlt werden soll.
         * @return Der aktualisierte Poose-Coin-Betrag des Händlers.
         */
        void geld_auszahlen(double poose_coins_);

        /**
         * @brief Gibt den aktuellen Poose-Coin-Betrag des Händlers zurück.
         * @return Der Poose-Coin-Betrag des Händlers.
         */
        double get_poose_coins();

        /**
         * @brief Gibt eine Liste der Artikel zurück, die der Händler besitzt.
         * @return Ein Vektor mit den Namen der Artikel.
         */
        std::vector<std::string> artikel_return();

        /**
         * @brief Gibt den Benutzernamen des Händlers zurück.
         * @return Der Benutzername des Händlers.
         */
        std::string retrun_benutzername();

        /**
         * @brief Entfernt einen bestimmten Gegenstand aus dem Besitz des Händlers.
         * @param gegenstand Der zu entfernende Gegenstand.
         */
        void entferne_gegenstand(std::string gegenstand);

        /**
         * @brief Fügt dem Besitz des Händlers einen Gegenstand hinzu.
         * @param gegenstand Der hinzuzufügende Gegenstand.
         */
        void gegenstand_erhalten(std::string gegenstand);

        /**
         * @brief Erhält einen Gewinn in Form von Poose-Coins.
         * @param poose_coins_ Der gewonnene Betrag.
         */
        void gewinn_erhalten(double poose_coins_);

        /**
         * @brief Zieht einen Betrag von Poose-Coins vom Händler ab.
         * @param poose_coins_ Der abzuziehende Betrag.
         */
        void geld_abziehen(double poose_coins_);

        /**
         * @brief Überprüft, ob der Händler einen bestimmten Gegenstand besitzt.
         * @param gegenstand Der zu überprüfende Gegenstand.
         * @return True, wenn der Händler den Gegenstand besitzt, sonst False.
         */
        bool hat_gegenstand(std::string gegenstand);

    private:
        double poose_coins = 0; /**< Der Betrag der Poose-Coins des Händlers. */
        std::vector<std::string> artikel; /**< Ein Vektor mit den Namen der Artikel, die der Händler besitzt. */
        std::string benutzername; /**< Der Benutzername des Händlers. */
    };
}
