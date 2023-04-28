import pygame


class Kissapeli:
    def __init__(self, korkeus, leveys) -> None:
        pygame.init()

        self.lataa_kuvat()
        
        self.kissa_x = 0
        self.kissa_y = leveys-self.kuvat[0].get_height()
        self.kissan_nopeus = 3

        self.oikealle = False
        self.vasemmalle = False

        self.korkeus = korkeus
        self.leveys = leveys
        self.naytto = pygame.display.set_mode((self.korkeus, self.leveys))

        pygame.display.set_caption("Kissapeli")
    
        self.run()



    #lataa peliin kuvat
    def lataa_kuvat(self):      
        self.kuvat = []
        for kuva in ["kissa1", "kissa1_puna", "kissa1_puna_miau", "kolmio"]:
            self.kuvat.append(pygame.image.load("images/"+ kuva +".png"))


    

        


    #silmukka mikä pitää pelin käynnissä
    def run(self):      
        while True:
            self.tapahtumat()
            self.piirra_naytto()

    #metodi mikä havannoi mitä painetaan
    def tapahtumat(self):   
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_LEFT:
                     self.vasemmalle = True
                if tapahtuma.key == pygame.K_RIGHT:
                     self.oikealle = True
            if tapahtuma.type == pygame.KEYUP:
                if tapahtuma.key == pygame.K_LEFT:
                     self.vasemmalle = False
                if tapahtuma.key == pygame.K_RIGHT:
                     self.oikealle = False
            if tapahtuma.type == pygame.QUIT:
                exit()
        #liikuttaa kissaa oikealle tai vasemmalle
        if self.oikealle:
            self.kissa_x += self.kissan_nopeus
        if self.vasemmalle:
            self.kissa_x -= self.kissan_nopeus


    #piirtää itse pelin ja kaiken sisällön siihen
    def piirra_naytto(self):        
        self.naytto.fill((255,255,255))
        self.naytto.blit(self.kuvat[0], (self.kissa_x, self.kissa_y))

        pygame.display.flip()

#käynnistää pelin sillä resoluutiolla mikä arvoksi annetaan
Kissapeli(1024,768) 