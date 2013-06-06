import pygame
import projectile
import time
import math
from gameAlgs import alg

class actor(pygame.sprite.Sprite):
    level = []
    
    #ctor
    def __init__(self, color, start_pos):
        #extending sprite
        pygame.sprite.Sprite.__init__(self)

        #setup player gfx
        self.surface = pygame.image.load('Resources/gordon_freeman.gif')
        self.rect = self.surface.get_rect()
        self.rect.topleft = start_pos

        #init player vars
        self.facing = pygame.K_DOWN
        self.speed = 500
        self.projSpeed = 800
        self.projectiles = []
        self.pos = start_pos
        self.last_attack = time.clock()
        self.base_attack_cd = 0.5
        self.move_map = {pygame.K_LEFT: (-1, 0),
                        pygame.K_RIGHT: (1, 0),
                        pygame.K_UP: (0, -1),
                        pygame.K_DOWN: (0, 1)}
        self.dest_vector = self.pos

    #move the object
    def move(self, keys, cr):
        pressed = pygame.key.get_pressed()
        moverate = cr*self.speed
        move_vector = (0, 0)
        for m in (self.move_map[key] for key in self.move_map if pressed[key]):
            move_vector = map(sum, zip(move_vector, m))
            self.orient(move_vector)

        if sum(map(abs, move_vector)) == 2:
            move_vector = [p/1.4142 for p in move_vector]

        move_vector = [moverate*p for p in move_vector]

        self.dest_vector = map(sum, zip(self.dest_vector, move_vector))

    #fire a projectile
    def shoot(self, keys):
        if keys[pygame.K_SPACE]:
            if (time.clock() - self.last_attack) > self.base_attack_cd:
                self.lastshoot = time.clock()
                self.projectiles.append(projectile.projectile(self.rect, 'Resources/projectile.gif', self.facing, self.projSpeed))

    #face and orient the sprite
    def orient(self, o_vec):
        self.facing = o_vec

    #update the object
    def update(self):
        self.rect = map(alg.w_avg, zip(self.rect, self.dest_vector))

    def giveLevel(self, level):
        self.level = level
        print self.level
