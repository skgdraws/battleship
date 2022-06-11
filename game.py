from re import S
import sys
from support import *
import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()          #initializes the Sprite module to be used later

        self.image = pygame.Surface((size, size))
        # self.image = pygame.image.load("images/tiles/ground1.png")
        self.rect = self.image.get_rect(topleft = pos)

class AnimatedTile(Tile):
    def __init__(self, pos, size, path):
        super().__init__(pos, size)
        self.frames = import_folder(path)
        self.frameIndex = 0
        self.animSpeed = 0.15
        self.image = self.frames[self.frameIndex]

    def animate(self):
        self.frameIndex += self.animSpeed
        
        if self.frameIndex >= len(self.frames):
            self.frameIndex = 0
        
        self.image = self.frames[int(self.frameIndex)]

class StaticTile(Tile):

    def __init__(self, pos, size, surface):
        super().__init__(pos, size)
        self.image = surface

class Juego:
    def __init__(self, pantalla):
        
        #Variables para la lógica del juego
        self.turnos = 1
        self.pantalla = pantalla
        self.save_game = 1

        #Audio
        self.rot_sound1 = pygame.mixer.Sound("assets/sound/sfx/rotate1.wav")
        self.rot_sound1.set_volume(0.5)
        self.rot_sound2 = pygame.mixer.Sound("assets/sound/sfx/rotate2.wav")
        self.rot_sound2.set_volume(0.5)
        self.rot_sounds = [self.rot_sound1, self.rot_sound2]

        self.hit_sound = pygame.mixer.Sound("assets/sound/sfx/hit.wav")
        self.hit_sound.set_volume(0.5)
        self.hit_confirm = pygame.mixer.Sound("assets/sound/sfx/hitConfirm.wav")
        self.hit_confirm.set_volume(0.5)

        self.miss = pygame.mixer.Sound("assets/sound/sfx/miss.wav")
        self.miss.set_volume(0.5)


        #Maneja el Tablero
        self.tablero_jugador = import_csv_layout(f"assets/data/save{self.save_game}/player1.csv")
        self.tablero_sprites = self.create_tile_group(self.tablero_jugador)


    def create_tile_group(self, layout):
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                
                x = (col_index * 64) + 300
                y = (row_index * 64) + 50
                
                if val == "0":
                    surface_tile_list = import_cut_graphics('assets/images/tiles/ground1.png')
                    tile_surface = surface_tile_list[int(val)]
                    sprite = StaticTile((x,y), 64, tile_surface)

                    sprite_group.add(sprite)
                
                if val == "1":
                    tile_surface = pygame.image.load("assets/images/barcos/barco1/barco1.png").convert_alpha()
                    sprite = AnimatedTile((x,y),64, "assets/images/barcos/barco1")

                    sprite_group.add(sprite)

                    
                
        return sprite_group
    
    dict= {"barco1":[0,0],"barco2":[0,2],"barco3":[0,3]}
    
    def place_boat(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            print ("hola")


    def run(self):
        self.tablero_jugador[1][1] = 1
        self.tablero_sprites.draw(self.pantalla)


