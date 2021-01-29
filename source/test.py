#Käynnistetään pelimoottori
import pygame 
pygame.init()

#Asetetaan värit
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (220, 220, 220)

#Avataan uusi ikkuna
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("FGJPeli")

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

    ##

    ##
    #Ruutu valkoiseksi
    screen.fill(WHITE)
    #Piirretään background
    pygame.draw.rect(screen, GREEN, [600, 0, 500, 500], 0)
    pygame.draw.rect(screen, GREEN, [0, 0, 100, 500], 0)
    pygame.draw.rect(screen, GREY, [100, 0, 500, 500], 0)
    pygame.draw.line(screen, GREEN, [0, 0], [0, 0], 5)
    pygame.draw.line(screen, GREEN, [250, 0], [0, 0], 5)
    pygame.draw.line(screen, GREEN, [0, 0], [0, 0], 5)

    #
    pygame.display.flip()

    #Framerate limit = 60
    clock.tick(60)

#
pygame.quit()