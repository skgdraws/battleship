import random
import pygame, sys
from support import *

pygame.init()

screen= pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

def get_font(size):
    return pygame.font.Font("assets/fonts/sonic-1-hud-font.ttf", size)

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

        #Efectos de Sonido
		self.select1 = pygame.mixer.Sound("assets/sound/sfx/select1.wav")
		self.select1.set_volume(0.5)
		self.select2 = pygame.mixer.Sound("assets/sound/sfx/select2.wav")
		self.select2.set_volume(0.5)
		self.select3 = pygame.mixer.Sound("assets/sound/sfx/select3.wav")
		self.select3.set_volume(0.5)
		self.select_sounds = [self.select1, self.select2, self.select3]

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.select_sounds[random.randint(0,2)].play()
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

def main_menu():
    pygame.display.set_caption("MainMenu")

    while True:
        mouse_pos= pygame.mouse.get_pos()
        screen.fill("black")

        logo= pygame.image.load("assets/images/logo.png")
        screen.blit(logo, (230, 50))

        play_b= Button(image= None, pos=(640, 400), text_input= "PLAY", font= get_font(70), base_color= "White", hovering_color= "#dfe0e8")
        play_b.changeColor(mouse_pos)
        play_b.update(screen)

        hs_b= Button(image= None, pos=(640, 500), text_input= "HIGHSCORE", font= get_font(70), base_color= "White", hovering_color= "#dfe0e8")
        hs_b.changeColor(mouse_pos)
        hs_b.update(screen)

        quit_b= Button(image= None, pos=(640, 600), text_input= "QUIT", font= get_font(70), base_color= "White", hovering_color= "#dfe0e8")
        quit_b.changeColor(mouse_pos)
        quit_b.update(screen)

        help_b= Button(image= None, pos=(1220, 70), text_input= "?", font= get_font(70), base_color= "White", hovering_color= "#dfe0e8")
        help_b.changeColor(mouse_pos)
        help_b.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_b.checkForInput(mouse_pos):
                    play()
                if hs_b.checkForInput(mouse_pos):
                    highscore()
                if quit_b.checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()
                if help_b.checkForInput(mouse_pos):
                    help()

        pygame.display.update()

def play():
    pygame.display.set_caption("FileSelect")

    while True:
        mouse_pos= pygame.mouse.get_pos()
        screen.fill("black")

        hs_b= Button(image= None, pos=(90, 60), text_input= "BACK", font= get_font(50), base_color= "White", hovering_color= "#dfe0e8")
        hs_b.changeColor(mouse_pos)
        hs_b.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu()

        pygame.display.update()

def highscore():
    pygame.display.set_caption("HighScore")

    def organize_score_list():
        lista = import_scores("assets/data/scores.csv")
        reorganize = []

        return organizar(lista, reorganize)

    def organizar(lista, reorden): 
        if lista == []: 
            return reorden
        else: 
            buscar_mayor = buscar(lista, mayor(lista), 0)
            return organizar(eliminar(lista, buscar_mayor, []), reorden + [buscar_mayor])

    def eliminar(lista, buscar_mayor, nueva_lista): 
        if lista == []: 
            return nueva_lista
        elif lista[0] == buscar_mayor: 
            return eliminar(lista[1:], buscar_mayor, nueva_lista)
        else: 
            return eliminar(lista[1:], buscar_mayor, [lista[0]] + nueva_lista)

    def buscar(lista, num, i): 
        if num == int(lista[i][0]):
            return lista[i]
        else: 
            return buscar(lista, num, i + 1)

    def mayor(lista): 
        if lista[1:] == []: 
            return int(lista[0][0])
        else: 
            return compara(int(lista[0][0]), mayor(lista[1:]))

    def compara(x, y): 
        if x > y: 
            return x
        else: 
            return y


    while True:
        mouse_pos= pygame.mouse.get_pos()
        screen.fill("black")

        scores = organize_score_list()

        hs_b= Button(image= None, pos=(90, 60), text_input= "BACK", font= get_font(50), base_color= "White", hovering_color= "#dfe0e8")
        hs_b.changeColor(mouse_pos)
        hs_b.update(screen)

        logo= pygame.image.load("assets/images/logo.png")
        screen.blit(logo, (230, 50))

        t1= get_font(45).render(f"1st. {scores[-1][-1]} - {scores[-1][0]}", True, "white")
        t1_rect= t1.get_rect(center= (640, 280))
        screen.blit(t1, t1_rect)

        t2= get_font(45).render(f"2nd. {scores[-2][-1]} - {scores[-2][0]}", True, "white")
        t2_rect= t2.get_rect(center= (640, 360))
        screen.blit(t2, t2_rect)

        t3= get_font(45).render(f"3rd. {scores[-3][-1]} - {scores[-3][0]}", True, "white")
        t3_rect= t3.get_rect(center= (640, 440))
        screen.blit(t3, t3_rect)

        t4= get_font(45).render(f"4th. {scores[-4][-1]} - {scores[-4][0]}", True, "white")
        t4_rect= t4.get_rect(center= (640, 520))
        screen.blit(t4, t4_rect)

        t5= get_font(45).render(f"5th. {scores[-5][-1]} - {scores[-5][0]}", True, "white")
        t5_rect= t5.get_rect(center= (640, 600))
        screen.blit(t5, t5_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu()

        pygame.display.update()

def help():
    pygame.display.set_caption("Help")

    while True:
        mouse_pos= pygame.mouse.get_pos()
        screen.fill("black")

        boat= pygame.image.load("assets/images/barco3-side.png")
        screen.blit(boat, (440, 600))

        t0= get_font(30).render("Hola! Bienvenido a Battleship", True, "white")
        t0_rect= t0.get_rect(center= (640, 100))
        screen.blit(t0, t0_rect)

        t1= get_font(25).render("En este juego, tu objetivo sera hundir los tres barcos enemigos", True, "white")
        t1_rect= t1.get_rect(center= (640, 150))
        screen.blit(t1, t1_rect)

        t2= get_font(25).render("Esto sera logrado mediante el uso de un tablero de 10x10", True, "white")
        t2_rect= t2.get_rect(center= (640, 200))
        screen.blit(t2, t2_rect)

        t3= get_font(25).render("El jugador debera colocar 3 barcos en el tablero, ya sea de manera horizontal o vertical ", True, "white")
        t3_rect= t3.get_rect(center= (640, 250))
        screen.blit(t3, t3_rect)

        t4= get_font(25).render("Los barcos tiene tamaños de 1, 2 y 3 espacioscada uno ", True, "white")
        t4_rect= t4.get_rect(center= (640, 300))
        screen.blit(t4, t4_rect)

        t5= get_font(25).render("Luego deberá elegir en el tablero, las coordenadas donde piensa que hay un barco enemigo", True, "white")
        t5_rect= t5.get_rect(center= (640, 350))
        screen.blit(t5, t5_rect)

        t6= get_font(25).render("Al clickear en este, se le avisará al jugador si falló, si le dio a un barco, o si hundió algún barco", True, "white")
        t6_rect= t6.get_rect(center= (640, 400))
        screen.blit(t6, t6_rect)

        t7= get_font(25).render("A continuación, la computadora eligirá un punto en donde disparar para asi hundir los barcos del jugador", True, "white")
        t7_rect= t7.get_rect(center= (640, 450))
        screen.blit(t7, t7_rect)

        t8= get_font(25).render("El primero en hundir los barcos del oponente, será el ganador!", True, "white")
        t8_rect= t8.get_rect(center= (640, 500))
        screen.blit(t8, t8_rect)

        hs_b= Button(image= None, pos=(90, 60), text_input= "BACK", font= get_font(50), base_color= "White", hovering_color= "#dfe0e8")
        hs_b.changeColor(mouse_pos)
        hs_b.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu()

        pygame.display.update()

main_menu()