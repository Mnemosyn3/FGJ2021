import pygame, os, sys

'''
Variables
'''

# put variables here
worldx = 960
worldy = 720

fps = 40
ani = 4

BLUE  = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)

main = True
'''
Objects
'''

# put Python classes and functions here

class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        for i in range(1, 5):
            img = pygame.image.load(os.path.join('images', 'hero' + str(i) + '.png')).convert()
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
'''
Setup
'''

# put run-once code here

clock = pygame.time.Clock()
pygame.init()
world = pygame.display.set_mode([worldx, worldy])

player = Player()   # spawn player
player.rect.x = 0   # go to x
player.rect.y = 0   # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
'''
Main Loop
'''



# put game loop here

while main:
    world.fill(BLUE)
    player_list.draw(world) # draw player
    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False

        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
            try:
                sys.exit()
            finally:
                main = False
