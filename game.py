import sys
from support import *
import pygame

pygame.init()
pantalla = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Battleship")
clock = pygame.time.Clock()

class Juego:
    def __init__(self, pantalla):
        
        #Variables para la lógica del juego
        self.turnos = 0
        self.pantalla = pantalla
        self.save_game = None

    def set_tablero(self, layout):
        pass

    def run(self):
        self.set_tablero(1)

class Tiles(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

juego = Juego(pantalla)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill("#3333A4")
    pygame.display.update()
    juego.run()
    clock.tick(60)

