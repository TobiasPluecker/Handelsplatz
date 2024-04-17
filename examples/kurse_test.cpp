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
    std::vector<std::string> t = m.artikel_print();
    print_array(t);
    for (int j = 0; j < 10000; j++) {
        m.preise_aktualisieren(3);
        std::vector<std::string> b = m.artikel_print();
        print_array(b);
        std::cout << " " << std::endl;
    }
}