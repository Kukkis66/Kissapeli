import pygame
import random


class Kissapeli:
    def __init__(self) -> None:
        pygame.init()

        self.lataa_kuvat()
        self.leveys = 10 * self.kuvat[0].get_height()
        self.korkeus = 6 * self.kuvat[0].get_height()
        self.naytto = pygame.display.set_mode((self.leveys, self.korkeus))
        self.fontti = pygame.font.SysFont("Comic Sans", 24)
        self.fontti1 = pygame.font.SysFont("Comic Sans", 50)


        self.kissa_x = 0
        self.kissa_y = self.korkeus-self.kuvat[0].get_height()
        
        
        self.vaikeus_aste = 1
        
        self.kissan_nopeus = 6
        self.tavaroiden_maara = 7
        self.tavaroiden_nopeus = 5
        
        
        self.pisteet = 0
        self.hiparit = 100


        self.tavaroiden_nopeus = 5
        
        self.ankat = []
        for x in range(self.tavaroiden_maara):
            self.ankat.append([random.randint(1000, 10000),self.korkeus-self.kuvat[3].get_height()])

        
        self.kultaraheet = []
        for x in range(self.tavaroiden_maara):
            self.kultaraheet.append([random.randint(1000, 10000),self.korkeus-self.kuvat[4].get_height()])
    
        self.oikealle = False
        self.vasemmalle = False

        self.hyppy = False
        self.hyppyaika = 13

        
        self.pelilapi = False
        self.kuolema = False
        



        self.kello = pygame.time.Clock()
       
        pygame.display.set_caption("Kissapeli")
    
        self.run()



    #lataa peliin kuvat
    def lataa_kuvat(self):      
        self.kuvat = []
        for kuva in ["kissa1", "kissa1_puna", "kissa1_puna_miau", "ankka", "kultarahe"]:
            self.kuvat.append(pygame.image.load("images/"+ kuva +".png"))

    
    #vaihtaa kissan väriä jos ottaa dmg tai miukuu jos saa rahea
    def kissa(self, puna, musta):

        if puna == 0 and musta == 1:
            self.naytto.blit(self.kuvat[0], (self.kissa_x, self.kissa_y))
        elif puna == 1 and musta == 1:
            self.naytto.blit(self.kuvat[2], (self.kissa_x, self.kissa_y))
        else:
            self.naytto.blit(self.kuvat[1], (self.kissa_x, self.kissa_y))

    #tekee vihulaisia ankkoja
    def ankka(self):

            for ankka in self.ankat:
                self.naytto.blit(self.kuvat[3], (ankka[0], ankka[1]))


                ankka[0] -= self.tavaroiden_nopeus
                
                if ankka[0] <= -100:
                    ankka[0] = random.randint(1500, 10000)
                
                if self.kissa_y+self.kuvat[0].get_height() >= ankka[1]+self.kuvat[4].get_height():
                    if self.kissa_x+self.kuvat[0].get_width() >= ankka[0] and self.kissa_x <= ankka[0]+self.kuvat[4].get_width():
                        self.kissa(1,0)
                        if self.hiparit > 0:
                            self.hiparit -= 1
                        
    
    #kuuntelee vähän tilannetta että missä mennään
    def tilanne(self):
        
        if self.pisteet >= 50:
            self.pelilapi = True
        if self.hiparit == 0:
            self.kuolema = True
    
    #piirtää tietoa                    
    def statistiikka(self):
        raha = self.fontti.render(f"Rahea: {self.pisteet}", True, (0,0,0))
        self.naytto.blit(raha,(10, 10))
        hiparit = self.fontti.render(f"Hiparit: {self.hiparit}", True, (0,0,0))
        self.naytto.blit(hiparit,(10, 30))
        vaikeus = self.fontti.render(f"Vaikeus: {self.vaikeus_aste}", True, (0,0,0))
        self.naytto.blit(vaikeus,(10, 50))
        ohjeet = self.fontti.render(f"F2: uusi peli     F5: nosta vaikeustasoa     F6: laskee vaikeustasoa", True, (0,0,0))
        self.naytto.blit(ohjeet,(400, 10))



    #aloittaa alusta. Ottaa parametriksi sen hetkisen vaikeusasteen ja vähentään saman verran ankkoja listalta
    def alusta(self, vaikeus):
        self.vaikeus_aste = 1
        
        self.kissan_nopeus = 6
        self.tavaroiden_maara = 7
        self.tavaroiden_nopeus = 5
        
        
        self.pisteet = 0
        self.hiparit = 100
        if len(self.ankat) >= 7:
            for x in range(vaikeus):
                self.ankat.pop()

        

    #nostaa/laskee vaikeustasoa
    def vaikeustaso(self, ylos, alas):
        
        
        if ylos == 1 and alas == 0:
            if self.vaikeus_aste <= 8:
                self.vaikeus_aste += 1
                self.kissan_nopeus += 1
                self.tavaroiden_nopeus += 1
                self.ankat.append([random.randint(1000, 10000),self.korkeus-self.kuvat[3].get_height()])


        if ylos == 0 and alas == 1:
            if self.vaikeus_aste > 1 and len(self.ankat) >= 7:
                self.vaikeus_aste -= 1
                self.kissan_nopeus -= 1
                self.tavaroiden_nopeus -= 1
                self.ankat.pop()

        
    #tekee rahea
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
                if tapahtuma.key == pygame.K_F5:
                    self.vaikeustaso(1,0)
                if tapahtuma.key == pygame.K_F6:
                    self.vaikeustaso(0,1)   
                if tapahtuma.key == pygame.K_F2:
                    self.pelilapi = False
                    self.kuolema = False
                    self.alusta(self.vaikeus_aste)
            if tapahtuma.type == pygame.KEYUP:
                if tapahtuma.key == pygame.K_LEFT:
                     self.vasemmalle = False
                if tapahtuma.key == pygame.K_RIGHT:
                     self.oikealle = False
        
                
            if tapahtuma.type == pygame.QUIT:
                exit()
        #liikuttaa kissaa oikealle tai vasemmalle ja rajoittaa ettei kisu mene ruudun ulkopuolelle
        if self.oikealle and self.kissa_x+self.kuvat[0].get_width() < self.leveys:
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
        self.tilanne()
        if self.pelilapi == False and self.kuolema == False:
            self.statistiikka()
        if self.pelilapi == True:
            pelilapi = self.fontti1.render(f"PELI LÄPI! Pelaa uudelleen(F2)", True, (0,0,0))
            self.naytto.blit(pelilapi,(self.leveys/3, self.korkeus/2))
        if self.kuolema == True:
            peliloppu = self.fontti1.render(f"MI-AUTS! Pelaa uudelleen(F2)", True, (0,0,0))
            self.naytto.blit(peliloppu,(self.leveys/3, self.korkeus/2))
        pygame.display.flip()
        self.kello.tick(69)

#käynnistää pelin
Kissapeli()