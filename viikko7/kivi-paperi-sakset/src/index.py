from pelitehdas import Pelitehdas

def main():

    pelit = {"a": Pelitehdas.luo_pelaaja_vs_pelaaja_peli,
    "b": Pelitehdas.luo_pelaaja_vs_tekoaly_peli,
    "c": Pelitehdas.luo_pelaaja_vs_hyva_tekoaly_peli}

    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        for key, value in pelit.items():
            if vastaus.endswith(key):
                peli = value()
                break
        else:
            break
    
        print(
            "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
        )
        
        peli.pelaa()



if __name__ == "__main__":
    main()
