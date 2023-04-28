import pygame


class Kissapeli:
    def __init__(self, korkeus, leveys) -> None:
        pygame.init()

        #self.lataa_kuvat()
        self.korkeus = korkeus
        self.leveys = leveys
        self.naytto = pygame.display.set_mode((self.korkeus, self.leveys))

        pygame.display.set_caption("Kissapeli")
    
        self.run()

    def lataa_kuvat(self):      #lataa peliin kuvat
        self.kuvat = []
        for kuva in []:
            self.kuvat.append(pygame.image.load(kuva +".png"))


    def uusi_peli(self):
        pass



    def run(self):      #silmukka mikä pitää pelin käynnissä
        while True:
            self.tapahtumat()
            self.piirra_naytto()


    def tapahtumat(self):   #metodi mikä havannoi mitä painetaan
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                exit()


    def piirra_naytto(self):        #piirtää itse pelin ja kaiken sisällön siihen
        self.naytto.fill((0,0,0))
        pygame.display.flip()


Kissapeli(1024,768) #käynnistää pelin sillä resoluutiolla mikä arvoksi annetaan