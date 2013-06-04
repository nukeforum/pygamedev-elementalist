import pygame
import time
import projectile
from gameAlgs import alg
import behaviors

class enemy(pygame.sprite.Sprite):
    
    #ctor
    def __init__(self, pos):
        #extending sprite
        pygame.sprite.Sprite.__init__(self)

        #setup gfx
        self.surface = pygame.image.load('Resources/gordon_freeman.gif')
        self.rect = self.surface.get_rect()
        self.rect.topleft = pos

        #init vars
        self.facing = pygame.K_DOWN
        self.speed = 300
        self.projSpeed = 800
        self.projectiles = []
        self.last_attack = time.clock()
        self.base_attack_cd = 0.5
        self.dest_vector = pos

    #move the object
    def move(self, target_pos):
        moverate = cr*self.speed
        move_vector = behaviors.behavior1(self.rect, target_pos)

        if sum(map(abs, move_vector)) == 2:
            move_vector = [p/1.4142 for p in move_vector]

        move_vector = [moverate*p for p in move_vector]
        
        self.dest_vector = map(sum, zip(self.dest_vector, move_vector))

    #fire projectile
    def shoot(self, keys):
        if keys[pygame.K_SPACE]:
            if (time.clock() - self.last_attack) > self.base_attack_cd:
                self.lastshoot = time.clock()
                self.projectiles.append(projectile(self.x, self.y, 'projectile.gif', self.facing, self.projSpeed))

    #face and orient the sprite
    def orient(self, o_vec):
        self.facing = o_vec

    #update the object
    def update(self, target_pos):
        self.move(target_pos)
        self.rect = map(alg.numstep, zip(self.rect, self.dest_vector))
