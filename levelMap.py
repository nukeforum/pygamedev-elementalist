from tileMap import *

class level(object):
    lmap = Map()
    uipanel = []
    def __init__(self):
        self.title = 'Balance'
    def __repr__(self):
        return self.title
    def addUI(self, ui):
        self.uipanel.append(ui)

class main_menu(level):
    def __init__(self):
        self.title = 'Main Menu'
        self.lmap.GenerateMap([
            [0,0,0,0,0],
            [0,0,0,0,0],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,1,1,1,1]], 32)
    def addUI(self, ui):
        self.uipanel.append(ui)

class level_1(level):
    def __init__(self):
        self.title = 'Level 1'
        self.lmap.GenerateMap([
            [1,1,1,1,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,1,1,1,1]], 32)
        self.uipanel = []
    def addUI(self, ui):
        self.uipanel.append(ui)
