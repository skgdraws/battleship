from email.headerregistry import Group
from re import S
import sys
from support import *
import pygame

pygame.init()

pantalla= pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Battleship!")
clock = pygame.time.Clock()

grid = []

spr_blank = pygame.image.load("assets/images/barcos/barco1/barco1.png")
spr_boat1 = pygame.image.load("assets/images/barcos/barco1/barco2.png")
spr_boat2 = pygame.image.load("assets/images/barcos/barco2/barco3.png")
# spr_boat3 = pygame.image.load("assets/images/barcos/barco3/barco1.png")

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

class Grid:

	def __init__(self, xGrid, yGrid, type):
		
		self.xGrid = xGrid
		self.yGrid = yGrid
		self.clicked= False
		self.isBoat1 = False
		self.isBoat2 = False
		self.isBoat3 = False
		self.attacked = False
		
		self.rect = pygame.Rect(300 + self.xGrid * 64, 50 + self.xGrid * 64, 64, 64)
		self.val = type

	def draw_grid(self):

		if self.clicked:

			if self.val == 0:
				if self.attacked:
					pantalla.blit(spr_blank, self.rect)
				else:
					pantalla.blit(spr_blank, self.rect)

			if self.val == 1:
				pantalla.blit(spr_boat1, self.rect)

			if self.val == 2:
				pantalla.blit(spr_boat2, self.rect)

			# if self.val == 3:
			# 	pantalla.blit(spr_boat3, self.rect)

		else:
			pantalla.blit(spr_blank, self.rect)

	def update_value(self, value):
		if self.val == 0:

			for x in range(0,4):
				if self.xGrid + x >= 0 and self.xGrid + x < 10:

					for y in range(-1, 2):

						if self.yGrid + y >= 0 and self.yGrid + y < 10:

							if grid[self.yGrid + y][self.xGrid + x].val == -1:
								self.val = value

def game(save):

	gameState = "Playing"
	global grid
	grid = []

	for j in range(10):
		line = []
		for i in range(10):
			line.append(Grid(i, j, 0))
		
		grid.append(line)

	while True:
		
		pantalla.fill("#3333A4")
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			
			else:
				if event.type == pygame.MOUSEBUTTONUP:
					for i in grid:
						for j in i:
							if j.rect.collidepoint(event.pos):
								if event.button == 1:
									print("atacaste!")
		for i in grid:
			for j in i:
				j.draw_grid()

		#grid.run()
		pygame.display.update()
		clock.tick(60)

game(1)