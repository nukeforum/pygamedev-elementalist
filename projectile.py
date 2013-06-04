import pygame
import math
from gameAlgs import alg

class projectile(pygame.sprite.Sprite):
    
    #ctor
    def __init__(self, pos, imgPath, face, speed):
        #extending sprite
        pygame.sprite.Sprite.__init__(self)

        #setup gfx
        self.surface = pygame.image.load(imgPath)
        self.rect = self.surface.get_rect()
        self.rect.topleft = pos

        #init projectile vars
        self.facing = face
        self.orient(self.facing)
        self.speed = speed
        self.pos = pos
        self.dest_vector = pos
        
    #move the object
    def move(self, cr):
        moverate = cr*self.speed
        move_vector = self.facing
        #normalize diagonal movement
        if sum(map(abs, move_vector)) == 2:
            move_vector = [p/1.4142 for p in move_vector]

        move_vector = [moverate*p for p in move_vector]

        #set the destination vector
        self.dest_vector = map(sum, zip(self.dest_vector, move_vector))

    #orient the sprite
    def orient(self, face):
        rot = math.atan2(face[0],face[1])
        rot = math.degrees(rot) - 90
        self.surface = pygame.transform.rotate(self.surface, rot)

    #update the object
    def update(self):
        #interpolate movement over frames
        self.rect = map(alg.w_avg, zip(self.rect, self.dest_vector))
