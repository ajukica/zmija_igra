
from math import e
from typing import Text
import pygame, sys,random
from pygame.constants import KEYUP, K_DOWN, K_LEFT, K_RIGHT, K_UP
from pygame.event import set_blocked
from pygame.math import Vector2

class VOCE:
    def __init__(self):
        self.randomize()

    def stavi_voce(self):
        voce_pr = pygame.Rect(self.pos.x * velicina_bloka,self.pos.y * velicina_bloka,velicina_bloka,velicina_bloka)
        prikaz.blit(hrana,voce_pr)
       

    def randomize(self):
        self.x = random.randint(0,broj_blokova -1)
        self.y = random.randint(0,broj_blokova -1)
        self.pos = Vector2(self.x,self.y)


class ZMIJA:
    def __init__(self):
        self.tijelo =[Vector2 (5,10),Vector2(4,10),Vector2(3,10)]  # tijelo zmije pocetak
        self.smjer = Vector2 (0,0)
        self.novi_blok = False

        self.head_up = pygame.image.load(r'c:\Users\Korisnik\Desktop\Zmija\Grafika\head_up.png').convert_alpha()
        self.head_down = pygame.image.load(r'c:\Users\Korisnik\Desktop\Zmija\Grafika\head_down.png').convert_alpha()
        self.head_right = pygame.image.load(r'c:\Users\Korisnik\Desktop\Zmija\Grafika\head_right.png').convert_alpha()
        self.head_left = pygame.image.load(r'c:\Users\Korisnik\Desktop\Zmija\Grafika\head_left.png').convert_alpha()
		
        self.tail_up = pygame.image.load(r'c:\Users\Korisnik\Desktop\Zmija\Grafika\tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load(r'c:\Users\Korisnik\Desktop\Zmija\Grafika\tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load(r'c:\Users\Korisnik\Desktop\Zmija\Grafika\tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load(r'c:\Users\Korisnik\Desktop\Zmija\Grafika\tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load(r'c:\Users\Korisnik\Desktop\Zmija\Grafika\body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load(r'c:\Users\Korisnik\Desktop\Zmija\Grafika\body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load(r'c:\Users\Korisnik\Desktop\Zmija\Grafika\body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load(r'c:\Users\Korisnik\Desktop\Zmija\Grafika\body_tl.png').convert_alpha()
        self.body_br = pygame.image.load(r'c:\Users\Korisnik\Desktop\Zmija\Grafika\body_br.png').convert_alpha()
        self.body_bl = pygame.image.load(r'c:\Users\Korisnik\Desktop\Zmija\Grafika\body_bl.png').convert_alpha()
        
        self.zvuk_ugriza = pygame.mixer.Sound(r'c:\Users\Korisnik\Desktop\Zmija\Zvuk\ugriz.wav')

    def postavi_zmiju(self):
        self.azuriraj_glavu()
        self.azuriraj_rep()

        for index,blok in enumerate (self.tijelo):
            x_pos = (blok.x * velicina_bloka)
            y_pos = (blok.y * velicina_bloka)
            blok_pr = pygame.Rect(x_pos,y_pos,velicina_bloka,velicina_bloka) 

            if index == 0:
                prikaz.blit(self.head,blok_pr)
            
            elif index == len(self.tijelo) - 1:
                prikaz.blit(self.tail,blok_pr)
            
            else:
                prethodni_blok = self.tijelo[index + 1] - blok
                sljedeci_blok = self.tijelo[index -1] - blok
                if prethodni_blok.x == sljedeci_blok.x:            
                    prikaz.blit(self.body_vertical,blok_pr)                                     #zmija vertikalno punjenje
                elif prethodni_blok.y == sljedeci_blok.y:
                    prikaz.blit(self.body_horizontal,blok_pr)                                   #zmija horizontalno punjenje
                else:
                        # zakrivljenost zmije
                    if prethodni_blok.x  == -1 and sljedeci_blok.y == -1 or prethodni_blok.y == -1 and sljedeci_blok.x == -1:
                        prikaz.blit(self.body_tl,blok_pr)
                    if prethodni_blok.x  == -1 and sljedeci_blok.y == 1 or prethodni_blok.y == 1 and sljedeci_blok.x == -1:
                        prikaz.blit(self.body_bl,blok_pr)
                    if prethodni_blok.x  == 1 and sljedeci_blok.y == -1 or prethodni_blok.y == -1 and sljedeci_blok.x == 1:
                        prikaz.blit(self.body_tr,blok_pr)
                    if prethodni_blok.x  == 1 and sljedeci_blok.y == 1 or prethodni_blok.y == 1 and sljedeci_blok.x == 1:
                        prikaz.blit(self.body_br,blok_pr)



    def azuriraj_glavu(self):

        glava = self.tijelo[1] - self.tijelo[0]  #odnos glave i tijela
        if glava == Vector2 (1,0):
            self.head = self.head_left
        elif glava == Vector2 (-1,0):
            self.head = self.head_right
        elif glava == Vector2 (0,1):
            self.head = self.head_up
        elif glava == Vector2 (0,-1):
            self.head = self.head_down

    def azuriraj_rep(self):
        rep = self.tijelo[-2] - self.tijelo[-1]  #odnos repa i tijela
        if rep == Vector2 (1,0):
            self.tail = self.tail_left
        elif rep == Vector2 (-1,0):
            self.tail = self.tail_right
        elif rep == Vector2 (0,1):
            self.tail = self.tail_up
        elif rep == Vector2 (0,-1):
            self.tail = self.tail_down




    def pokreni_zmiju(self):
        if self.novi_blok == True:
            kopija_tijela = self.tijelo [:]                          #rep zmije
            kopija_tijela.insert (0,kopija_tijela[0] + self.smjer)   #glava zmije
            self.tijelo = kopija_tijela[:]
            self.novi_blok = False
        else:
            kopija_tijela = self.tijelo [:-1]                          #rep zmije
            kopija_tijela.insert (0,kopija_tijela[0] + self.smjer)   #glava zmije
            self.tijelo = kopija_tijela[:]

    def dodaj_blok(self):
        self.novi_blok = True
    
    def zvuk (self):
        self.zvuk_ugriza.play()

    def reset(self):
        self.tijelo =[Vector2 (5,10),Vector2(4,10),Vector2(3,10)]
        self.smjer = Vector2 (0,0)


        
class MAIN:
    def __init__(self):
        self.zmija = ZMIJA()
        self.voce = VOCE()

    def osvjezi(self):
        self.zmija.pokreni_zmiju()
        self.sudar()
        self.provjeri_igru()
        
    def nacrtaj(self):
        
        self.trava()
        self.voce.stavi_voce()
        self.zmija.postavi_zmiju()
        self.rezultat()
        

    def sudar(self):
        if self.voce.pos == self.zmija.tijelo[0]:
            self.voce.randomize()
            self.zmija.dodaj_blok()
            self.zmija.zvuk()

        for blok in self.zmija.tijelo[1:]:
            if blok == self.voce.pos:
                self.voce.randomize()

    def provjeri_igru(self):
        if not 0 <= self.zmija.tijelo[0].x  < broj_blokova or not 0 <= self.zmija.tijelo[0].y  < broj_blokova:            #provjera udara u granice
            self.game_over()

        for blok in self.zmija.tijelo [1:]:
            if blok == self.zmija.tijelo[0]:
                self.game_over()

    def game_over(self):
       self.zmija.reset()


    def trava(self):
        trava_boja =(167,209,61)
        for row in range(broj_blokova):
            if row % 2 == 0:
                for col in range(broj_blokova):
                    if col % 2 == 0:
                        trava_pr = pygame.Rect(col * velicina_bloka,row * velicina_bloka,velicina_bloka,velicina_bloka)
                        pygame.draw.rect(prikaz,trava_boja,trava_pr)
            else:
                for col in range(broj_blokova):
                    if col % 2 != 0:
                        trava_pr = pygame.Rect(col * velicina_bloka,row * velicina_bloka,velicina_bloka,velicina_bloka)
                        pygame.draw.rect(prikaz,trava_boja,trava_pr)

    def rezultat(self):

        rezultat_text = str(len(self.zmija.tijelo) - 3)
        rezultat = font.render(rezultat_text,True,(56,74,12))
        rezultat_x = (velicina_bloka * broj_blokova - 60)
        rezultat_y = (velicina_bloka * broj_blokova - 30)
        rezultat_pr = rezultat.get_rect(center = (rezultat_x,rezultat_y))
        hrana_pr = hrana.get_rect(midright = (rezultat_pr.left,rezultat_pr.centery))

        prikaz.blit(rezultat,rezultat_pr)
        prikaz.blit(hrana,hrana_pr)


pygame.init()
velicina_bloka = 40
broj_blokova = 20
prikaz = pygame.display.set_mode((velicina_bloka * broj_blokova,velicina_bloka * broj_blokova)) 
timer = pygame.time.Clock()
hrana = pygame.image.load(r'c:\Users\Korisnik\Desktop\Zmija\Grafika\apple.png').convert_alpha()
font = pygame.font.Font(r'c:\Users\Korisnik\Desktop\Zmija\Font\ADELIA.otf',25)


OSVJEZI_PRIKAZ = pygame.USEREVENT
pygame.time.set_timer(OSVJEZI_PRIKAZ,150)

main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == OSVJEZI_PRIKAZ:
            main_game.osvjezi()
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if main_game.zmija.smjer.y != 1:
                        main_game.zmija.smjer = Vector2 (0,-1)
                if event.key == pygame.K_DOWN:
                    if main_game.zmija.smjer.y != -1:
                     main_game.zmija.smjer = Vector2 (0,1)
                if event.key == pygame.K_LEFT:
                    if main_game.zmija.smjer.x != 1:
                        main_game.zmija.smjer = Vector2 (-1,0)
                if event.key == pygame.K_RIGHT:
                    if main_game.zmija.smjer.x != -1:
                        main_game.zmija.smjer = Vector2 (1,0)

    prikaz.fill((175,215,70))
    main_game.nacrtaj()
    pygame.display.update()
    timer.tick(60)

    