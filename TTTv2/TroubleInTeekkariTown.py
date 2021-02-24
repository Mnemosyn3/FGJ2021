import pygame, sys, os, random
import data.engine as e
import keychoice
import gardenmg
import Muisti_Peli
clock = pygame.time.Clock()

from pygame.locals import *
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init() # initiates pygame
pygame.mixer.set_num_channels(64)
WINDOW_SIZE = (600,400)

screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiate the window

display = pygame.Surface((300,200)) # used as the surface for rendering, which is scaled


sysfont = pygame.font.get_default_font()
font = pygame.font.SysFont(None, 48)
kyykkafont = pygame.font.SysFont(None, 30)


def load_map(path):
    f = open(path + '.txt','r')
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))
        
    return game_map

class button_obj():
    def __init__(self, loc):
        self.loc = loc
        self.time = 0
    def render(self, surf, scroll):
        surf.blit(jumper_img, (self.loc[0] - scroll[0], self.loc[1] - scroll[1]))

    def get_rect(self):
        return pygame.Rect(self.loc[0], self.loc[1], 8, 9)

    def collision_test(self, rect):
        button_rect = self.get_rect()
        return button_rect.colliderect(rect)
jumper_img = pygame.image.load("data/images/nappi.png")
game_map = load_map('data/map/MAPV1')
map_image = pygame.image.load("data/map/MAPv1.png")
e.load_animations('data/images/entities/')

grass_sounds = [pygame.mixer.Sound('data/audio/grass_0.wav'),pygame.mixer.Sound('data/audio/grass_1.wav')]
grass_sounds[0].set_volume(0.2)
grass_sounds[1].set_volume(0.2)



player = e.entity(475,1115,26,22,'player')

#nappeja
teksti = button_obj((475,1115))


sauna = button_obj((3755,45))
etkot = button_obj((110,235))
etkotnappi = button_obj((170,235))
garden1 = button_obj((2675,1325))
garden2 = button_obj((2675,1300))
garden3 = button_obj((2675,1350))
strippiklubi = button_obj((3660, 1750))
metsa = button_obj((490, 1750))
koti = button_obj((2470, 1070))
jatkot = button_obj((2225, 107))
saunateksti = button_obj((3745, 115))
kyykkateksti = button_obj((2850, 1300))
endingtext = button_obj((475, 1115))
def main():
    FirstTime = True
    Beentokyykka = False
    FirstTimesauna = True
    Beentosauna = False
    AVAIN = 0
    KYYKKAWIN = False
    PUHELIN = False
    
    grass_sound_timer = 0
    pygame.display.set_caption('Trouble in Teekkari Town')

    WINDOW_SIZE = (1000,900)

    screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiate the window

    display = pygame.Surface((300,200)) # used as the surface for rendering, which is scaled

    moving_right = False
    moving_left = False
    moving_up = False
    moving_down = False

    true_scroll = [0,0]
    TILE_SIZE = 32

    pygame.mixer.music.load('data/audio/music.wav')
    #pygame.mixer.music.play(-1)



    player = e.entity(475,1115,22,26,'player')

    while True: # game loop
        display.fill((0,0,0)) # clear screen by filling it with black

        if grass_sound_timer > 0:
            grass_sound_timer -= 1

        true_scroll[0] += (player.x-true_scroll[0]-152)/20
        true_scroll[1] += (player.y-true_scroll[1]-106)/20
        scroll = true_scroll.copy()
        scroll[0] = int(scroll[0])
        scroll[1] = int(scroll[1])
        
        

        
        tile_rects = []
        y = 0
        for row in game_map:
            x = 0
            for tile in row:
                
                x += 1
                if tile == "W":
                    
                    pygame.draw.rect(display, (0,0,0), pygame.Rect(x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1], TILE_SIZE,TILE_SIZE))
                
                if tile == "W":
                    tile_rects.append(pygame.Rect(x * TILE_SIZE,y * TILE_SIZE,TILE_SIZE, TILE_SIZE))
            
            y +=1
        display.blit((map_image), (32-scroll[0],0-scroll[1]))
        

        


        player_movement = [0,0]
        if moving_right == True:
            player_movement[0] += 4
        if moving_left == True:
            player_movement[0] -= 4
        if moving_up:
            player_movement[1]-=4
        if moving_down:
            player_movement[1]+=4
        
        

        if player_movement[0] == 0:
            player.set_action('idle')
        if player_movement[0] > 0:
            player.set_flip(False)
            player.set_action('run')
        if player_movement[0] < 0:
            player.set_flip(True)
            player.set_action('run')
        if player_movement[1] > 0:
            player.set_flip(False)
            player.set_action('run')
        if player_movement[1] < 0:
            player.set_flip(True)
            player.set_action('run')

        collision_types = player.move(player_movement,tile_rects)

        if player_movement[0] != 0 or player_movement[1] != 0:
            if grass_sound_timer == 0:
                grass_sound_timer = 30
                random.choice(grass_sounds).play()

        player.change_frame(1)
        player.display(display,scroll)

        koti.render(display,scroll)
        if koti.collision_test(player.obj.rect):
            if AVAIN == 1 and KYYKKAWIN == True and PUHELIN == True:
                endingtext.time = 300
            else:
                koti.time = 400
            if koti.time > 0:
                imgfont = pygame.font.SysFont(None, 15)
                img = imgfont.render("You don't have all of your things yet!", True, (255, 255, 255))
                rect = img.get_rect()
                pygame.draw.rect(img, (0,0,255), rect, 1)
                display.blit(img,(20,20))
                koti.time -= 1
        kyykkafont = pygame.font.SysFont(None, 20)
        if endingtext.time > 0:
            imgending = kyykkafont.render("You Won!", True, (255,255,255))
            rectkyykka = imgending.get_rect()
            pygame.draw.rect(imgending, (0,0,255), rectkyykka, 1)
            display.blit(imgending,(20,20))
            endingtext.time -= 1
            if endingtext.time == 1:
                sys.exit()

        metsa.render(display,scroll)
        if metsa.collision_test(player.obj.rect):
            player.set_pos(75,2050)
            metsa.time = 400
        if metsa.time > 0:
            imgfont = pygame.font.SysFont(None, 15)
            img = imgfont.render("You got lost in the forest, try to find your way out!", True, (255, 255, 255))
            rect = img.get_rect()
            pygame.draw.rect(img, (0,0,255), rect, 1)
            display.blit(img,(20,20))
            metsa.time -= 1
        jatkot.render(display,scroll)
        if jatkot.collision_test(player.obj.rect):
            player.set_pos(475,1170)
            jatkot.time = 400
        if jatkot.time > 0:
            imgfont = pygame.font.SysFont(None, 13)
            img = imgfont.render("You went to another party and drank so much that you woke up at the bar!", True, (255, 255, 255))
            rect = img.get_rect()
            pygame.draw.rect(img, (0,0,255), rect, 1)
            display.blit(img,(20,20))
            jatkot.time -= 1           
        strippiklubi.render(display,scroll)
        if strippiklubi.collision_test(player.obj.rect):
            player.set_pos(475,1170)
            strippiklubi.time = 400
        if strippiklubi.time > 0:
            imgfont = pygame.font.SysFont(None, 15)
            img = imgfont.render("You went to a strip-club and after that woke up at the bar!", True, (255, 255, 255))
            rect = img.get_rect()
            pygame.draw.rect(img, (0,0,255), rect, 1)
            display.blit(img,(20,20))
            strippiklubi.time -= 1
        teksti.render(display,scroll)
        if teksti.collision_test(player.obj.rect):
            
            
            teksti.time = 300
        if teksti.time > 0:
            imgfont = pygame.font.SysFont(None, 15)  
            img = imgfont.render("You are drunk, try to find your stuff and go home!", True, (255, 255, 255))
            rect = img.get_rect()
            pygame.draw.rect(img, (0,0,255), rect, 1)

            display.blit(img,(20,20))
            teksti.time -= 1
        etkot.render(display,scroll)
        if etkot.collision_test(player.obj.rect):
            player.set_pos(130, 235)
            moving_right = False
            moving_left = False
            moving_up = False
            moving_down = False
            print("Mennaan etkoille!")
            PUHELIN = Muisti_Peli.muistipelimg()
            if PUHELIN == True:
                print("SAit puhelimen")
        etkotnappi.render(display,scroll)
        if etkotnappi.collision_test(player.obj.rect) and PUHELIN == False:
            etkotnappi.time = 300
        if etkotnappi.time > 0:
            imgfont = pygame.font.SysFont(None, 15)
            img = imgfont.render("You have a faint memory of leaving your phone here...", True, (255, 255, 255))
            rect = img.get_rect()
            pygame.draw.rect(img, (0,0,255), rect, 1)
            display.blit(img,(20,20))
            etkotnappi.time -= 1
        sauna.render(display,scroll)
        saunateksti.render(display,scroll)
        if sauna.collision_test(player.obj.rect):
            player.set_pos(3745, 115)
            moving_right = False
            moving_left = False
            moving_up = False
            moving_down = False
            print("Mennaan saunaan")
            AVAIN = keychoice.minigame_key()
            print(AVAIN)
            Beentosauna = True
        if Beentosauna == False and FirstTimesauna == True:
            saunawintext = "I remember this sauna!" 
        if FirstTimesauna == False and Beentosauna == False:
            saunawintext = ""
        if AVAIN != 0:
            kyykkafont = pygame.font.SysFont(None, 20)
            saunawintext = "I hope this is the right key..."
        if saunateksti.collision_test(player.obj.rect):
            saunateksti.time = 0
            saunateksti.time = 300
        if saunateksti.time > 0:
            imgsauna = kyykkafont.render(saunawintext, True, (255,255,255))
            rectsauna = imgsauna.get_rect()
            pygame.draw.rect(imgsauna, (0,0,255), rectsauna, 1)
            display.blit(imgsauna,(20,20))
            saunateksti.time -= 1
            if saunateksti.time == 0:
                FirstTimesauna = False
        
        garden1.render(display,scroll)
        garden2.render(display,scroll)
        garden3.render(display,scroll)
        kyykkateksti.render(display,scroll)
        kyykkafont = pygame.font.SysFont(None, 20)
        if garden1.collision_test(player.obj.rect) or garden2.collision_test(player.obj.rect) or garden3.collision_test(player.obj.rect):
            player.set_pos(2850, 1300)
            moving_right = False
            moving_left = False
            moving_up = False
            moving_down = False
            print("Mennaan gardeniin")
            KYYKKAWIN = gardenmg.dodge()
            Beentokyykka = True
        if Beentokyykka == False and FirstTime == True:
            kyykkawintext = "Those guys look familiar and angry..." 
        if FirstTime == False and Beentokyykka == False:
            kyykkawintext = ""
        if KYYKKAWIN ==True:
            kyykkafont = pygame.font.SysFont(None, 20)
            kyykkawintext = "You escaped with your wallet!"
        if KYYKKAWIN ==False and Beentokyykka == True:
            kyykkafont = pygame.font.SysFont(None, 20)
            kyykkawintext = "You escaped, bruised..."
        if kyykkateksti.collision_test(player.obj.rect):
            kyykkateksti.time = 0
            kyykkateksti.time = 300
        if kyykkateksti.time > 0:
            imgkyykka = kyykkafont.render(kyykkawintext, True, (255,255,255))
            rectkyykka = imgkyykka.get_rect()
            pygame.draw.rect(imgkyykka, (0,0,255), rectkyykka, 1)
            display.blit(imgkyykka,(20,20))
            kyykkateksti.time -= 1
            if kyykkateksti.time == 0:
                FirstTime = False
        
        for event in pygame.event.get(): # event loop
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:

                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    #print("left")
                    moving_left = True
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                #  print("right")
                    moving_right = True
                if event.key == pygame.K_UP or event.key == ord('w'):
                    #print("up")
                    moving_up = True
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    #print("down")
                    moving_down = True

            if event.type == KEYUP:

                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    #print("left")
                    moving_left = False
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    #print("right")
                    moving_right = False
                if event.key == pygame.K_UP or event.key == ord('w'):
                    #print("up")
                    moving_up = False
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    #print("down")
                    moving_down = False
        screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
        pygame.display.update()
        clock.tick(60)
    return 0
main()
