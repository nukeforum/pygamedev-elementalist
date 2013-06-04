import pygame

class Tile(object):
    def __init__(self, tileId, topLeft):
        self.surface = pygame.image.load('Resources/tex' + str(tileId) + '.png')
        self.rect = self.surface.get_rect()
        self.rect.topleft = topLeft

class Map(object):
    width = 0
    height = 0
    tiles = []
    def __init__(self):
        pass
    def GenerateMap(self, nmap, tsize):
        for y in range(len(nmap)):
            for x in range(len(nmap[y])):
                tileId = nmap[y][x]

                if tileId > 0:
                    self.tiles.append(Tile(tileId, (tsize*x, tsize*y)))

                self.width = tsize*(x+1)
            self.height = tsize*(y+1)
