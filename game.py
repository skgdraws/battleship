from re import S
import sys
from support import *
import pygame

pygame.init()

pantalla= pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")
clock = pygame.time.Clock()

class Button():

	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()          #initializes the Sprite module to be used later

        self.image = pygame.Surface((size, size))
        # self.image = pygame.image.load("images/tiles/ground1.png")
        self.rect = self.image.get_rect(topleft = pos)

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

        #Maneja los botones
        self.mouse_pos= pygame.mouse.get_pos()
        self.barco1= Button(image= pygame.image.load("assets/images/barcos/barco1/barco1.png"), pos=(1100, 200), text_input= "", font= self.get_font(70), base_color= "black", hovering_color= "#dfe0e8")
        self.barco1.changeColor(self.mouse_pos)

        self.barco2= Button(image= pygame.image.load("assets/images/barcos/barco2/barco2.png"), pos=(1100, 400), text_input= "", font= self.get_font(70), base_color= "black", hovering_color= "#dfe0e8")
        self.barco2.changeColor(self.mouse_pos)

        self.barco3= Button(image= pygame.image.load("assets/images/barco3-side.png"), pos=(1100, 600), text_input= "", font= self.get_font(70), base_color= "black", hovering_color= "#dfe0e8")
        self.barco3.changeColor(self.mouse_pos)

    def get_font(self, size):
        return pygame.font.Font("assets/fonts/sonic-1-hud-font.ttf", size)

    def create_tile_group(self, layout):
        pass
        
    
    dict= {"barco1":[0,0],"barco2":[0,2],"barco3":[0,3]}

    def place_barco1(self):
        print("barco1")
    
    def place_barco2(self):
        print("barco2")
    
    def place_barco3(self):
        print("barco3")

    def run(self):
        self.barco1.update(pantalla)
        self.barco2.update(pantalla)
        self.barco3.update(pantalla)
        self.mouse_pos= pygame.mouse.get_pos()


juego = Juego(pantalla)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if juego.barco1.checkForInput(juego.mouse_pos):
                juego.place_barco1()

            if juego.barco2.checkForInput(juego.mouse_pos):
                juego.place_barco2()

            if juego.barco3.checkForInput(juego.mouse_pos):
                juego.place_barco3()
         
    pantalla.fill("#3333A4")
    juego.run()
    pygame.display.update()
    clock.tick(60)