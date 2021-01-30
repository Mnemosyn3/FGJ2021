import pygame, webbrowser, sys
WHITE = (255, 255, 255)

#TAUSTA
map_image = pygame.image.load("map.jpg")

class Kyykka(pygame.sprite.Sprite):
    #Kyykän sprite

    def __init__(self, color, width, height, speed):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        self.width=width
        self.height=height
        self.color =color
        self.speed =speed

        #Kyykän piirto
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()

    def moveRigth(self, pixels):
        self.rect.x += pixels
        
    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveUp(self, pixels):
        self.rect.y -= pixels

    def moveDown(self, pixels):
        self.rect.y += pixels

    def changeSpeed(self, speed):
        self.speed = speed

    def repaint(self, color):
        self.color = color
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])

#Käynnistetään pelimoottori
import pygame, random
pygame.init()

#Asetetaan värit
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)
YELLOW = (255, 255, 0)

speed = 4

#Avataan uusi ikkuna
SCREENWIDTH = 1000
SCREENHEIGHT = 900
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("FGJMiniGame")

#sprite lista
all_sprites_list = pygame.sprite.Group()

player = Kyykka(CYAN, 60, 80, 70)
player.rect.x = 450
player.rect.y = SCREENHEIGHT - 100

kyykka1 = Kyykka(YELLOW, 50, 70, random.randint(50,400))
kyykka1.rect.x = random.randint(5, 948)
kyykka1.rect.y = random.randint(-1100, -100)
 
kyykka2 = Kyykka(YELLOW, 50, 70, random.randint(50,400))
kyykka2.rect.x = random.randint(5, 948)
kyykka2.rect.y = random.randint(-1100, -100)
 
kyykka3 = Kyykka(YELLOW, 50, 70, random.randint(50,400))
kyykka3.rect.x = random.randint(5, 948)
kyykka3.rect.y = random.randint(-1100, -100)
 
kyykka4 = Kyykka(YELLOW, 50, 70, random.randint(50,400))
kyykka4.rect.x = random.randint(5, 948)
kyykka4.rect.y = random.randint(-1100, -100)

kyykka5 = Kyykka(YELLOW, 50, 70, random.randint(50,400))
kyykka5.rect.x = random.randint(5, 948)
kyykka5.rect.y = random.randint(-1100, -100)

kyykka6 = Kyykka(YELLOW, 50, 70, random.randint(50,400))
kyykka6.rect.x = random.randint(5, 948)
kyykka6.rect.y = random.randint(-1100, -100)

kyykka6 = Kyykka(YELLOW, 50, 70, random.randint(50,400))
kyykka6.rect.x = random.randint(5, 948)
kyykka6.rect.y = random.randint(-1100, -100)

kyykka7 = Kyykka(YELLOW, 50, 70, random.randint(50,400))
kyykka7.rect.x = random.randint(5, 948)
kyykka7.rect.y = random.randint(-1100, -100)

all_sprites_list.add(player)
all_sprites_list.add(kyykka1)
all_sprites_list.add(kyykka2)
all_sprites_list.add(kyykka3)
all_sprites_list.add(kyykka4)
all_sprites_list.add(kyykka5)
all_sprites_list.add(kyykka6)
all_sprites_list.add(kyykka7)

all_coming_kyykka = pygame.sprite.Group()
all_coming_kyykka.add(kyykka1)
all_coming_kyykka.add(kyykka2)
all_coming_kyykka.add(kyykka3)
all_coming_kyykka.add(kyykka4)
all_coming_kyykka.add(kyykka5)
all_coming_kyykka.add(kyykka6)
all_coming_kyykka.add(kyykka7)
#Loop pyörittää peliä, kunnes käyttäjä sammuttaa sen
carryOn = True

#Kello määrittää, kuinka usein näyttö päivittyy
clock = pygame.time.Clock()

#Pääohjelma loop
while carryOn:
    #Päätapahtuma loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                caryyOn = False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    carryOn = False
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.moveLeft(10)
        if keys[pygame.K_RIGHT]:
            player.moveRigth(10)
        #if keys[pygame.K_UP]:
            #player.moveUp(5)
        #if keys[pygame.K_DOWN]:
            #player.moveDown(5)

        ##GAME LOGIC
        for kyykka in all_coming_kyykka:
            speed+=0.001
            kyykka.moveDown(speed)
            if kyykka.rect.y > SCREENWIDTH:
                kyykka.changeSpeed(random.randint(10,50))
                kyykka.repaint(YELLOW)
                kyykka.rect.x = random.randint(5, 948)
                kyykka.rect.y = random.randint(-1100, -100)
        kyykka_collision_list = pygame.sprite.spritecollide(player,all_coming_kyykka,False)
        for kyykka in kyykka_collision_list:
            print("Ny ossui saatana!")
            webbrowser.open('https://www.youtube.com/watch?v=NUYvbT6vTPs')
            #End Of Game
            carryOn=False
        all_sprites_list.update()

        ##
        #Ruutu valkoiseksi
        KENTTÄ = (245, 245, 245)
        screen.fill(BLACK)
        dest = (50, 100)
        screen.blit(map_image, dest)
        #Piirretään background
        #pygame.draw.rect(screen, WHITE, [600, 0, 500, 500], 0)
        #pygame.draw.rect(screen, WHITE, [0, 0, 100, 500], 0)
        #pygame.draw.rect(screen, WHITE, [100, 0, 500, 500], 0)
        left_line = pygame.draw.line(screen, RED, [5, 0], [5, 1000], 15)
        right_line = pygame.draw.line(screen, RED, [995, 0], [995, 1000], 15)
        #pygame.draw.line(screen, WHITE, [300, 0], [300, 500], 5)
        #pygame.draw.line(screen, WHITE, [500, 0], [500, 500], 5)

        all_sprites_list.draw(screen)

        #
        pygame.display.flip()

        #Framerate limit = 60
        clock.tick(60)

#
pygame.quit()