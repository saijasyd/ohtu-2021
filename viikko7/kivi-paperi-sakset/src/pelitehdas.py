

import kps
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu

class Pelitehdas:


    @staticmethod
    def luo_pelaaja_vs_pelaaja_peli():
        return kps.KPSPelaajaVsPelaaja()

    @staticmethod
    def luo_pelaaja_vs_tekoaly_peli():
        return kps.KPSTekoaly(Tekoaly())

    @staticmethod
    def luo_pelaaja_vs_hyva_tekoaly_peli():
        return kps.KPSTekoaly(TekoalyParannettu(10))