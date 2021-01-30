import pygame, sys
clock = pygame.time.Clock()
from pygame.locals import *
pygame.init()

pygame.display.set_caption("Trouble In Teekkaritown")

WINDOW_SIZE = (1200,800)

screen = pygame.display.set_mode(WINDOW_SIZE,0,32)
display = pygame.Surface((150,100))

scroll = [0,0]

player_image = pygame.image.load("player.png")
player_image.set_colorkey((255,255,255))

TILE_SIZE = grass_image.get_width()


def load_map(path):
    f = open(path + '.txt','r')
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))
        
    return game_map

game_map = load_map('map')

def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def move(rect, movement, tiles):
    collision_types = {"top":False,"bottom":False,"left":False,"right":False}
    rect.x += movement[0]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types["left"] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types["rigth"] = True
    
    rect.y += movement[1]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types["bottom"] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types["top"] = True
    return rect, collision_types

moving_left = False
moving_right = False
moving_up = False
moving_down = False



player_rect = pygame.Rect(50,50,player_image.get_width(),player_image.get_height())

test_rect = pygame.Rect(100,100,100,50)

while True:

    scroll[0] += (player_rect.x-scroll[0]-77)/20
    scroll[1] += (player_rect.y-scroll[1]-57)/20

    display.fill((255,255,255))
    tile_rects = []
    y = 0
    for row in game_map:
        x = 0
        for tile in row:
            
            x += 1
            if tile == "1":
                display.blit(dirt_image, (x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1]))
            if tile == "2":
                display.blit(grass_image, (x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1]))
            if tile != "0":
                tile_rects.append(pygame.Rect(x * TILE_SIZE,y * TILE_SIZE,TILE_SIZE, TILE_SIZE))
        
        y +=1

    

    player_movement = [0,0]

    if moving_left:
        player_movement[0]-=1
    if moving_right:
        player_movement[0]+=1
    if moving_up:
        player_movement[1]-=1
    if moving_down:
        player_movement[1]+=1

    player_rect,collisions = move(player_rect,player_movement,tile_rects)
    display.blit(player_image,(player_rect.x - scroll[0],player_rect.y - scroll[1]))

    for event in pygame.event.get():
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
    
    surf = pygame.transform.scale(display,WINDOW_SIZE)
    screen.blit(surf,(0,0))
    pygame.display.update()
    clock.tick(60)

