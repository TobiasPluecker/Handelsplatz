#include <gtest/gtest.h>
#include "/home/odin/Schreibtisch/poose3/src/artikel.cpp"
#include "/home/odin/Schreibtisch/poose3/src/haendler.cpp"
#include "/home/odin/Schreibtisch/poose3/src/handelsplatz.cpp"




// Testet die Funktion haendler_erstellen, um sicherzustellen, dass sie einen neuen Händler mit dem angegebenen Benutzernamen erstellt
TEST(HandelsplatzMarktTest, HaendlerErstellen)
{
    Handelsplatz::Markt markt;
    markt.haendler_erstellen("Benutzer1");

    // Überprüfe, ob der Händler erfolgreich erstellt wurde
    EXPECT_EQ(markt.get_index_person("Benutzer1"), 0);
}

// Testet die Funktion angebot_erstellen, um sicherzustellen, dass ein neues Angebot erstellt wird
TEST(HandelsplatzMarktTest, AngebotErstellen)
{
    Handelsplatz::Markt markt;
    markt.haendler_erstellen("Verkaeufer");
    markt.angebot_erstellen("Verkaeufer", "Gegenstand", 10.0);

    // Angebot darf nicht erstellt werden, da die Person den Gegenstand nicht an.
    //EXPECT_DEATH(markt.angebot_erstellen("Verkaeufer", "Gegenstand", 10.0), std::runtime_error);
}

// Testet die Funktion verkaufen, um sicherzustellen, dass ein Gegenstand erfolgreich verkauft wird
TEST(HandelsplatzMarktTest, Verkaufen)
{
    Handelsplatz::Markt markt;
    markt.haendler_erstellen("Verkaeufer");
    markt.geld_hinzufuegen("Verkaeufer", 1000000);
    markt.gegenstaende_holen("Verkaeufer", "Haus");
    markt.haendler_erstellen("Kaeufer");
    int angebotsnummer = markt.angebot_erstellen("Verkaeufer", "Haus", 0);
    markt.verkaufen("Kaeufer", angebotsnummer);

    // Überprüfe, ob der Gegenstand erfolgreich verkauft wurde
    EXPECT_EQ(markt.gegenstaende_einer_person("Verkaefer").size(), 0);
    EXPECT_EQ(markt.gegenstaende_einer_person("Kaefer").size(), 1);
}

// Testet die Funktion gegenstaende_holen, um sicherzustellen, dass ein Gegenstand erfolgreich geholt wird
TEST(HandelsplatzMarktTest, GegenstaendeHolen)
{
    Handelsplatz::Markt markt;
    markt.haendler_erstellen("Kaeufer");
    markt.geld_hinzufuegen("Kaeufer", 1000000.0);
    markt.gegenstaende_holen("kaeufer", "Haus");
    std::vector<std::string> a = markt.gegenstaende_einer_person("Kaefer");
    // Überprüfe, ob der Gegenstand erfolgreich geholt wurde
    ASSERT_EQ(a.size(), 1);

}

// Testet die Funktion geld_hinzufuegen, um sicherzustellen, dass das Guthaben einer Person erfolgreich erhöht wird
TEST(HandelsplatzMarktTest, GeldHinzufuegen)
{
    Handelsplatz::Markt markt;
    markt.haendler_erstellen("Benutzer");
    markt.geld_hinzufuegen("Benutzer", 50.0);

    // Überprüfe, ob das Guthaben erfolgreich erhöht wurde
    ASSERT_EQ(markt.guthaben_einer_person("Benutzer"), 50.0);
}

// Testet die Funktion guthaben_einer_person, um sicherzustellen, dass das korrekte Guthaben einer Person zurückgegeben wird
TEST(HandelsplatzMarktTest, GuthabenEinerPerson)
{
    Handelsplatz::Markt markt;
    markt.haendler_erstellen("Benutzer");
    markt.geld_hinzufuegen("Benutzer", 50.0);

    // Überprüfe das Guthaben der Person
    ASSERT_EQ(markt.guthaben_einer_person("Benutzer"), 50.0);
}

// Testet die Funktion angebot_loeschen, um sicherzustellen, dass ein Angebot erfolgreich gelöscht wird
TEST(HandelsplatzMarktTest, AngebotLoeschen)
{
    Handelsplatz::Markt markt;
    markt.haendler_erstellen("Verkaeufer");
    markt.geld_hinzufuegen("Verkaeufer", 1000000);
    markt.gegenstaende_holen("Verkaeufer", "Haus");
    int nummer = markt.angebot_erstellen("Verkaeufer", "Haus", 100);
    std::vector<std::string> a = markt.angebote_print();
    ASSERT_EQ(a.size(), 1);
    markt.angebot_zurueckziehen(nummer, "Verkaefer");
    std::vector<std::string> b = markt.angebote_print();
    ASSERT_EQ(b.size(), 1);
}

// Testet die Funktion gegenstaende_einer_person, um sicherzustellen, dass die Liste der Gegenstände einer Person korrekt zurückgegeben wird
TEST(HandelsplatzMarktTest, GegenstaendeEinerPerson)
{
    Handelsplatz::Markt markt;
    markt.haendler_erstellen("Benutzer");
    markt.geld_hinzufuegen("Benutzer", 100000000);
    markt.angebot_erstellen("Benutzer", "Haus", 10.0);
    markt.angebot_erstellen("Benutzer", "Haus", 20.0);
    std::vector<std::string> gegenstaende = markt.gegenstaende_einer_person("Benutzer");

    // Überprüfe die Liste der Gegenstände der Person
    ASSERT_EQ(gegenstaende.size(), 2);
}


