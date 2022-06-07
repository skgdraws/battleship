import pygame
import sys
from csv import *

pygame.init()
pantalla = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Battleship")
clock = pygame.time.Clock()

def import_layout(path):
    maps = []
    # Opening up the csv File
    with open(path) as map:
        level = reader(map, delimiter = ',')
        for row in level:
            maps.append(list(row))
        return maps

class Juego:

    def __init__(self, pantalla, path):
        
        #Variables para la lógica del juego
        self.turnos = 0
        self.pantalla = pantalla
        self.path = f"assets/data/safe{path}/game.csv"

    def set_tablero(self, layout):
        thing = import_layout(layout)
        print(thing)

    def run(self):
        self.set_tablero(self.path)

juego = Juego(pantalla,1)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill("#000000")
    pygame.display.update()
    juego.run()
    clock.tick(60)

