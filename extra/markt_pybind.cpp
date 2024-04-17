#include "/home/odin/Schreibtisch/poose3/include/handelsplatz.hpp"
#include "/home/odin/Schreibtisch/poose3/include/haendler.hpp"
#include "/home/odin/Schreibtisch/poose3/include/artikel.hpp"


#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/complex.h>
#include <pybind11/functional.h>

namespace py = pybind11;
using namespace Handelsplatz;

PYBIND11_MODULE(markt, m) {
    py::class_<Handelsplatz::Markt>(m, "Markt")
        .def(py::init<>())
        .def("get_artikel_list", &Handelsplatz::Markt::get_artikel_list)
        .def("haendler_erstellen", &Handelsplatz::Markt::haendler_erstellen)
        .def("return_angebote", &Handelsplatz::Markt::return_angebote)
        .def("angebot_erstellen", &Handelsplatz::Markt::angebot_erstellen)
        .def("artikel_print", &Handelsplatz::Markt::artikel_print)
        .def("angebote_print", &Handelsplatz::Markt::angebote_print)
        .def("verkaufen", &Handelsplatz::Markt::verkaufen)
        .def("get_index_person", &Handelsplatz::Markt::get_index_person)
        .def("gegenstaende_holen", &Handelsplatz::Markt::gegenstaende_holen)
        .def("geld_hinzufuegen", &Handelsplatz::Markt::geld_hinzufuegen)
        .def("guthaben_einer_person", &Handelsplatz::Markt::guthaben_einer_person)
        .def("angebot_zurueckziehen", &Handelsplatz::Markt::angebot_zurueckziehen)
        .def("preise_aktualisieren", &Handelsplatz::Markt::preise_aktualisieren)
        .def("return_angebot_preis", &Handelsplatz::Markt::return_angebot_preis)
        .def("anz_gegenstand", &Handelsplatz::Markt::anz_gegenstand)
        .def("preis_von_gegenstand", &Handelsplatz::Markt::preis_von_gegenstand)
        .def("besitzt_person_gegenstand", &Handelsplatz::Markt::besitzt_person_gegenstand)
        .def("get_artikel_array", &Handelsplatz::Markt::get_angebote_array)
        .def("get_angebote_array", &Handelsplatz::Markt::get_artikel_array)
        .def("geld_auszahlen", &Handelsplatz::Markt::geld_auszahlen)
        .def("gegenstaende_einer_person", &Handelsplatz::Markt::gegenstaende_einer_person);
}







