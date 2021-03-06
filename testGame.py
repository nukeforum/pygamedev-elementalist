import math
import time
import pc
import npc
import pygame, sys
import levelMap
from pygame.locals import *
        
pygame.init()
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('game')

pygame.key.set_repeat(1,1)

milli = fpsClock.tick()
seconds = milli / 1000.

load_level = levelMap.main_menu()

player = pc.actor((0, 0, 0), (50, 50))
player.giveLevel(load_level.lmap)
enemies = []
spawnTimer = 5000
lastSpawn = time.clock()

keys = {pygame.K_LEFT : False,
        pygame.K_RIGHT : False,
        pygame.K_UP : False,
        pygame.K_DOWN : False,
        pygame.K_SPACE : False}
redColor = pygame.Color(255,0,0)
greenColor = pygame.Color(0,255,0)
blueColor = pygame.Color(0,0,255)
whiteColor = pygame.Color(255,255,255)
mousex, mousey = 0, 0

fontObj = pygame.font.Font('freesansbold.ttf', 32)
msg = load_level.title
soundObj = pygame.mixer.Sound('Resources/boing.wav')

while True:
    screen.fill(whiteColor)

    for x in load_level.lmap.tiles:
        screen.blit(x.surface, x.rect)
    
    screen.blit(player.surface, player.rect)
    for bullet in player.projectiles:
        bullet.move(seconds)
        bullet.update()
        screen.blit(bullet.surface, bullet.rect)
        if bullet.rect[0] > 640 or bullet.rect[0] < 0 or bullet.rect[len(bullet.pos) - 1] > 480 or bullet.rect[len(bullet.pos) - 1] < 0:
            player.projectiles.remove(bullet)
    for baddie in enemies:
        baddie.update(player.rect)
        screen.blit(baddie.surface, baddie.rect)

    msgSurfaceObj = fontObj.render(msg, False, blueColor)
    msgRectobj = msgSurfaceObj.get_rect()
    msgRectobj.topleft = (10, 20)
    screen.blit(msgSurfaceObj, msgRectobj)

    for event in pygame.event.get():
        pressed = pygame.key.get_pressed()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif pressed[K_ESCAPE]:
            pygame.event.post(pygame.event.Event(QUIT))

        player.move(pressed, seconds)
        player.shoot(pressed)

    if (time.clock() - lastSpawn) > spawnTimer:
        lastSpawn = time.clock()
        enemies.append(npc.enemy((150,150)))

    player.update()
    pygame.display.update()
    fpsClock.tick(30)
