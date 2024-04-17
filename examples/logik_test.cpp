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
    m.angebot_zurueckziehen(100, "Tobias");
    m.verkaufen("Tobias", 1000);
    std::cout << "test" << std::endl;
    m.angebot_zurueckziehen(101, "Test");
    m.haendler_erstellen("Jawad");
    m.haendler_erstellen("Jawad");
    std::cout << "test" << std::endl;
    m.gegenstaende_holen("Jawad", "Haus");
    std::cout << "test1" << std::endl;
    



    return 0;
}
