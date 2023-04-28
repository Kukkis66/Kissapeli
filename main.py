import pygame
import random


class Kissapeli:
    def __init__(self, korkeus, leveys) -> None:
        pygame.init()

        self.lataa_kuvat()
        self.korkeus = korkeus
        self.leveys = leveys
        self.naytto = pygame.display.set_mode((self.korkeus, self.leveys))

        self.kissa_x = 0
        self.kissa_y = leveys-self.kuvat[0].get_height()
        self.kissan_nopeus = 5

        self.vaikeustaso = 10

        self.pisteet = 0
        self.elamat = 9


        self.tavaroiden_nopeus = 5
        
        self.viholliset = []
        for x in range(self.vaikeustaso):
            self.viholliset.append([random.randint(1000, 10000),self.leveys-self.kuvat[3].get_height()])

        
        self.kultaraheet = []
        for x in range(self.vaikeustaso):
            self.kultaraheet.append([random.randint(1000, 10000),self.leveys-self.kuvat[4].get_height()])
    
        self.oikealle = False
        self.vasemmalle = False

        self.hyppy = False
        self.hyppyaika = 13

        
        



        self.kello = pygame.time.Clock()
       
        pygame.display.set_caption("Kissapeli")
    
        self.run()



    #lataa peliin kuvat
    def lataa_kuvat(self):      
        self.kuvat = []
        for kuva in ["kissa1", "kissa1_puna", "kissa1_puna_miau", "ankka", "kultarahe"]:
            self.kuvat.append(pygame.image.load("images/"+ kuva +".png"))

    def kissa(self, puna, musta):

        if puna == 0 and musta == 1:
            self.naytto.blit(self.kuvat[0], (self.kissa_x, self.kissa_y))
        elif puna == 1 and musta == 1:
            self.naytto.blit(self.kuvat[2], (self.kissa_x, self.kissa_y))
        else:
            self.naytto.blit(self.kuvat[1], (self.kissa_x, self.kissa_y))

    #tekee kolmioita
    def ankka(self):

            for self.pahis in self.viholliset:
                self.naytto.blit(self.kuvat[3], (self.pahis[0], self.pahis[1]))


                self.pahis[0] -= self.tavaroiden_nopeus

                if self.kissa_y+self.kuvat[0].get_height() >= self.pahis[1]+self.kuvat[4].get_height():
                    if self.kissa_x+self.kuvat[0].get_width() >= self.pahis[0] and self.kissa_x <= self.pahis[0]+self.kuvat[4].get_width():
                        self.elamat -= 1
                        self.kissa(1,0)
                        

        
        
    def kultarahe(self):

            for rahe in self.kultaraheet:
                self.naytto.blit(self.kuvat[4], (rahe[0], rahe[1]))


                rahe[0] -= self.tavaroiden_nopeus
                if self.kissa_y+self.kuvat[0].get_height() >= rahe[1]+self.kuvat[4].get_height():
                    if self.kissa_x+self.kuvat[0].get_width() >= rahe[0] and self.kissa_x <= rahe[0]+self.kuvat[4].get_width():
                        rahe[0] = random.randint(2000, 10000)
                        self.pisteet += 1
                        self.kissa(1,1)
        


    #silmukka mikä pitää pelin käynnissä
    def run(self):      
        while True:
            self.tapahtumat()
            self.piirra_naytto()
            
            

    #määrää mitä milloinkin tapahtuu
    def tapahtumat(self):
        
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_LEFT:
                     self.vasemmalle = True
                if tapahtuma.key == pygame.K_RIGHT:
                     self.oikealle = True
                if tapahtuma.key == pygame.K_SPACE:
                    self.hyppy = True
            if tapahtuma.type == pygame.KEYUP:
                if tapahtuma.key == pygame.K_LEFT:
                     self.vasemmalle = False
                if tapahtuma.key == pygame.K_RIGHT:
                     self.oikealle = False
        
                
            if tapahtuma.type == pygame.QUIT:
                exit()
        #liikuttaa kissaa oikealle tai vasemmalle ja rajoittaa ettei kisu mene ruudun ulkopuolelle
        if self.oikealle and self.kissa_x < self.leveys+self.kuvat[0].get_width():
            self.kissa_x += self.kissan_nopeus
        if self.vasemmalle and self.kissa_x > 0:
            self.kissa_x -= self.kissan_nopeus
        
        #hyppy
        if self.hyppy:        
            if self.hyppyaika >= -13:
                self.kissa_y -= (self.hyppyaika * abs(self.hyppyaika)) * 0.5
                self.hyppyaika -= 1
            else: 
                self.hyppyaika = 13
                self.hyppy = False
        


        
        


    #piirtää itse pelin ja kaiken sisällön siihen
    def piirra_naytto(self):        
        self.naytto.fill((255,255,255))
        
        self.kissa(0,1)
        self.ankka()
        self.kultarahe()
        pygame.display.flip()
        self.kello.tick(69)

#käynnistää pelin sillä resoluutiolla mikä arvoksi annetaan
Kissapeli(1024,768)