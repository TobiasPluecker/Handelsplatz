#pragma once
#include "/home/odin/Schreibtisch/poose3/include/artikel.hpp"


std::string Handelsplatz::Artikel::get_name_() {
    return name;
}


double Handelsplatz::Artikel::get_wert_() {
    return wert;
}

void Handelsplatz::Artikel::set_name(std::string name_) {
    name = name_;
}


void Handelsplatz::Artikel::set_wert(double wert_) {
    wert = wert_;
}


std::string Handelsplatz::Angebot::get_ersteller() {
    return ersteller;
}


std::string Handelsplatz::Angebot::get_obj() {
    return obj;
}


double Handelsplatz::Angebot::get_wert() {
    return wert;
}


std::vector<double> Handelsplatz::Artikel::kursverlauf(double tendenz, double streuung, double dt, double start, int anzahl) {
    std::vector<double> kurs(anzahl);
    kurs[0] = start;
    
    std::random_device rd;
    std::mt19937 gen(rd());
    std::normal_distribution<double> dist(0.0, 1.0);
    
    double sqdt = std::sqrt(dt);
    
    for (int i = 0; i < anzahl - 1; i++) {
        double Y = dist(gen);
        kurs[i + 1] = kurs[i] * (1 + tendenz * dt + streuung * sqdt * Y);
        set_wert(kurs[i + 1]);
    }
    
    return kurs;
}


void Handelsplatz::Artikel::aktualisiere_kurs() {
    kursverlauf(0.3, 0.2, 0.001, wert, 2);
}

