import pygame
import sys

pygame.init()
pantalla = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Battleship")
clock = pygame.time.Clock()

class Juego:

    def __init__(self, pantalla):
        
        #Variables para la lógica del juego
        self.turnos = 0
        self.pantalla = pantalla

    def set_tablero(self):
        pass

    def run(self):
        self.set_tablero()

juego = Juego(pantalla)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill("#000000")
    pygame.display.update()
    clock.tick(60)