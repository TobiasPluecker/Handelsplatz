#include "/home/odin/Schreibtisch/poose3/include/haendler.hpp"


/**
 * @brief Gibt den Benutzernamen des Händlers zurück.
 * @return Der Benutzername des Händlers.
 */
std::string Handelsplatz::Haendler::retrun_benutzername() {
    return benutzername;
}

/**
 * @brief Gibt den aktuellen Poose-Coin-Betrag des Händlers zurück.
 * @return Der Poose-Coin-Betrag des Händlers.
 */
double Handelsplatz::Haendler::get_poose_coins() {
    return poose_coins;
}

/**
 * @brief Führt eine Einzahlung von Geld in die Poose-Coins des Händlers durch.
 * @param poose_coins_ Der Betrag, der eingezahlt werden soll.
 * @return Der aktualisierte Poose-Coin-Betrag des Händlers.
 */
double Handelsplatz::Haendler::geld_einzahlen(double poose_coins_) {
    if(poose_coins_ >= 0){ // da man nichts negatives einzahlen darf
        poose_coins = poose_coins + poose_coins_;
        return poose_coins; //damit man seinen neuen Kontostand direkt bekommt
    }
    return 1;
}

/**
 * @brief Führt eine Auszahlung von Geld aus den Poose-Coins des Händlers durch.
 * @param poose_coins_ Der Betrag, der ausgezahlt werden soll.
 * @return Der aktualisierte Poose-Coin-Betrag des Händlers.
 */
void Handelsplatz::Haendler::geld_auszahlen(double poose_coins_) {
    poose_coins -= poose_coins_;
}

/**
 * @brief Gibt eine Liste der Artikel des Händlers zurück.
 * @return Ein Vektor mit den Namen der Artikel.
 */
std::vector<std::string> Handelsplatz::Haendler::artikel_return(){
    return artikel;
}

/**
 * @brief Entfernt einen bestimmten Gegenstand aus dem Besitz des Händlers.
 * @param gegenstand Der zu entfernende Gegenstand.
 */
void Handelsplatz::Haendler::entferne_gegenstand(std::string gegenstand) {
    for (int i = 0; i < gegenstand.size(); i++) {
        if (artikel[i] == gegenstand) {
            std::string last = artikel[artikel.size()-1];
            std::string temp =  artikel[i];
            artikel[i] = last; 
            artikel[artikel.size()-1] = temp;
            artikel.pop_back();
            return;
        }
        std::cout << "Objekt ist nicht vorhanden" << std::endl;
    }
}

/**
 * @brief Fügt dem Besitz des Händlers einen Gegenstand hinzu.
 * @param gegenstand Der hinzuzufügende Gegenstand.
 */
void Handelsplatz::Haendler::gegenstand_erhalten(std::string gegenstand) {
    artikel.push_back(gegenstand);
}

/**
 * @brief Zieht einen Betrag von Poose-Coins vom Händler ab.
 * @param poose_coins_ Der abzuziehende Betrag.
 */
void Handelsplatz::Haendler::geld_abziehen(double poose_coins_) {
    poose_coins -= poose_coins_;
}

/**
 * @brief Erhält einen Gewinn in Form von Poose-Coins.
 * @param poose_coins_ Der gewonnene Betrag.
 */
void Handelsplatz::Haendler::gewinn_erhalten(double poose_coins_) {
    poose_coins += poose_coins_;
}

/**
 * @brief Überprüft, ob der Händler einen bestimmten Gegenstand besitzt.
 * @param gegenstand Der zu überprüfende Gegenstand.
 * @return True, wenn der Händler den Gegenstand besitzt, sonst False.
 */
bool Handelsplatz::Haendler::hat_gegenstand(std::string gegenstand) {
    bool ret = false;
    for (int i = 0; i < artikel.size(); i++) {
        if (artikel[i] == gegenstand) {
            ret = true;
        }
    }
    return ret;
}
