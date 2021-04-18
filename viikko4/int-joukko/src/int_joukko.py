KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):

        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D

        self.kapasiteetti = kapasiteetti

        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("kapasiteetti2")  # heitin vaan jotain :D
        
        self.kasvatuskoko = kasvatuskoko

        self.lukujono = [None] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.lukujono

    def lisaa(self, n):

        if n in self.lukujono:
            return False

        for i in range(len(self.lukujono)):
            if self.lukujono[i] == None:
                self.lukujono[i] = n
                self.alkioiden_lkm += 1
                return True

        self.lukujono = self.lukujono + [None] * self.kasvatuskoko
        return self.lisaa(n)


    def poista(self, n):


        alkuperainen_maara = self.alkioiden_lkm

        for i in range(len(self.lukujono)-1):
            if self.lukujono[i] == n:
                self.lukujono[i] = None
                self.alkioiden_lkm -= 1
            if self.lukujono[i] == None:
                self.lukujono[i] = self.lukujono[i+1]
                self.lukujono[i+1] = None

        if self.lukujono[:-1] == n:
            self.lukujono[:-1] = None

        return alkuperainen_maara != self.alkioiden_lkm


    def kopioi_taulukko(self, a, b):
        b = a[:]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):

        return [luku for luku in self.lukujono if luku != None]


    @staticmethod
    def yhdiste(a, b):


        

        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.lukujono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.lukujono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.lukujono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
