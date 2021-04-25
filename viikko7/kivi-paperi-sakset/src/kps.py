from tuomari import Tuomari

class KPS:

    def __init__(self):
        self._tuomari = Tuomari()

    def pelaa(self):
      

        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            self._tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(self._tuomari)

            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(ekan_siirto)


        print("Kiitos!")
        print(self._tuomari)

    def _ensimmaisen_siirto(self):
      return input("Ensimmäisen pelaajan siirto: ")

    # tämän metodin toteutus vaihtelee eri pelityypeissä
    def _toisen_siirto(self, ensimmaisen_siirto):
        # metodin oletustoteutus
        return "k"

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"


class KPSTekoaly(KPS):

    def __init__(self, tekoaly):
        super().__init__()
        self._tekoaly = tekoaly
        self._siirtoja = 0
        

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self._tekoaly.anna_siirto()
        self._siirtoja += 1
        if self._siirtoja > 1:
            self._tekoaly.aseta_siirto(ensimmaisen_siirto)

        print(f"Tietokone valitsi: {tokan_siirto}")
        return tokan_siirto



class KPSPelaajaVsPelaaja(KPS):

    def _toisen_siirto(self, ensimmaisen_siirto):
        return input("Toisen pelaajan siirto: ")
    

    