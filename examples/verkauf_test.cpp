#include "/home/odin/Schreibtisch/poose3/src/artikel.cpp"
#include "/home/odin/Schreibtisch/poose3/src/haendler.cpp"
#include "/home/odin/Schreibtisch/poose3/src/handelsplatz.cpp"



void print_array(std::vector<std::string> a) {
    for (int i = 0; i < a.size(); i++) {
        std::cout << a[i] << std::endl;
    }
}


int main() {
    Handelsplatz::Markt m;
    m.preise_aktualisieren(10);
    m.haendler_erstellen("Tobias");
    m.haendler_erstellen("Jawad");
    
    m.geld_hinzufuegen("Tobias", 1000);
    m.geld_hinzufuegen("Jawad", 1000);
    
    m.gegenstaende_holen("Tobias", "Haus");
    std::cout << "Tobias hat: " <<  m.guthaben_einer_person("Tobias") << std::endl; 
    std::cout << "Jawad hat: " <<  m.guthaben_einer_person("Jawad") << std::endl;
    int a = m.angebot_erstellen("Tobias", "Haus", 50);
    std::vector<std::string> b = m.angebote_print();
    //print_array(b);
    m.verkaufen("Jawad", a);
    std::cout << "Tobias hat: " <<  m.guthaben_einer_person("Tobias") << std::endl; 
    std::cout << "Jawad hat: " <<  m.guthaben_einer_person("Jawad") << std::endl;
    
    return 0;
}