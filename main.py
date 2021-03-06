import random
import time
import tkinter as tk
import pygame
from PIL import ImageTk, Image
from support import *

pygame.init()
window= tk.Tk()
window.geometry("1280x720")
window.title("Battleship!")
window.resizable(False, False)

#Efectos de Sonido
select1 = pygame.mixer.Sound("assets/sound/sfx/select1.wav")
select1.set_volume(0.35)
select2 = pygame.mixer.Sound("assets/sound/sfx/select2.wav")
select2.set_volume(0.35)
select3 = pygame.mixer.Sound("assets/sound/sfx/select3.wav")
select3.set_volume(0.35)
select_sounds = [select1, select2, select3]

title_theme = pygame.mixer.Sound("assets/sound/music/title-theme.mp3")
title_theme.set_volume(0.35)

battle_theme = pygame.mixer.Sound("assets/sound/music/declare-war.mp3")
battle_theme.set_volume(0.35)

player = [[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]

enemy = [[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]

barco = 0
place_boat1 = False
place_boat2 = False
place_boat3 = False

boat1_pos = ""
boat2_pos = ""
boat3_pos = ""

curEnemy1 = 1
curEnemy2 = 2
curEnemy3 = 3

curPlayer1 = 1
curPlayer2 = 2
curPlayer3 = 3


turnos = 0
aciertos = 0
fallos = 0

title_theme.play(-1)

def main():
    canvas= tk.Canvas(window, width=1280, height=720, borderwidth=0, highlightthickness=0, bg="black")
    window.title('Battleship! - TitleScreen')
    canvas.pack()

    #Titulo
    title= ImageTk.PhotoImage(Image.open('assets/images/logo.png'))
    canvas.create_image(240, 65, anchor= tk.NW, image=title)

    #Boton seleccionar una partida
    def open_p():
        select_sounds[random.randint(0,2)].play()
        canvas.destroy()
        canvas.quit
        play()
    play_b= tk.Button(canvas, text= " PLAY ", font= ("Sonic 1 HUD Font", 30), bg= "black", fg="white", command= open_p)
    play_b.place(x= 570, y= 300)

    #Boton para salon de la fama
    def open_hs():
        select_sounds[random.randint(0,2)].play()
        canvas.destroy()
        canvas.quit
        highscore()
    hs_b= tk.Button(canvas, text= "HIGHSCORE", font= ("Sonic 1 HUD Font", 30), bg= "black", fg="white", command= open_hs)
    hs_b.place(x= 534, y= 450)

    #Boton para cerrar el juego
    def quit():
        window.destroy()
        window.quit
    quit_b= tk.Button(canvas, text= " QUIT ", font= ("Sonic 1 HUD Font", 30), bg= "black", fg="white", command= quit)
    quit_b.place(x= 570, y= 600)

    #Boton para ayuda
    def open_h():
        select_sounds[random.randint(0,2)].play()
        canvas.destroy()
        canvas.quit
        help()
    help_b= tk.Button(canvas, text= " ? ", font= ("Sonic 1 HUD Font", 20), bg= "black", fg="white", command= open_h)
    help_b.place(x= 1200, y= 40)

    window.mainloop()

def game():
    g_canvas= tk.Canvas(window, width=1280, height=720, borderwidth=0, highlightthickness=0, bg="blue")
    window.title('Battleship! - Placing Boats')
    g_canvas.pack()

    global barco
    global player
    global enemy
    global boat1_pos
    global boat2_pos
    global boat3_pos
    
    #Selecci??n de Barcos (Im??genes)
    boat1= ImageTk.PhotoImage(Image.open('assets/images/barco1.png'))
    g_canvas.create_image(1150, 50, anchor= tk.N, image=boat1)

    boat2= ImageTk.PhotoImage(Image.open('assets/images/barco2.png'))
    g_canvas.create_image(1150, 250, anchor= tk.N, image=boat2)

    boat3= ImageTk.PhotoImage(Image.open('assets/images/barco3.png'))
    g_canvas.create_image(1085, 450, anchor= tk.NW, image=boat3)

    #Selecci??n de Barcos (Botones)
    boat1_b= tk.Button(g_canvas, text= "BARCO 1", font= ("Sonic 1 HUD Font", 20), bg= "#4D6AA0", fg="#CDDEFF", command= lambda: select_boat(1))
    boat1_b.place(x= 1100, y=150)

    boat2_b= tk.Button(g_canvas, text= "BARCO 2", font= ("Sonic 1 HUD Font", 20), bg= "#4D6AA0", fg="#CDDEFF",command= lambda: select_boat(2))
    boat2_b.place(x= 1100, y=350)

    boat3_b= tk.Button(g_canvas, text= "BARCO 3", font= ("Sonic 1 HUD Font", 20), bg= "#4D6AA0", fg="#CDDEFF",command= lambda: select_boat(3))
    boat3_b.place(x= 1100, y=550)

    #Posici??n de los Barcos
    pos_boat1_label = tk.Label(text= "Sin Poner", font=("Sonic 1 HUD Font", 15), bg= "blue", fg= "#CDDEFF")
    pos_boat1_label.place(x= 200, y= 350 + 15)
    pos_boat1= ImageTk.PhotoImage(Image.open('assets/images/barco1.png'))
    g_canvas.create_image(100, 350, anchor= tk.N, image=pos_boat1)

    pos_boat2_label = tk.Label(text= "Sin Poner", font=("Sonic 1 HUD Font", 15), bg= "blue", fg= "#CDDEFF")
    pos_boat2_label.place(x= 200, y=420 + 15)
    pos_boat2= ImageTk.PhotoImage(Image.open('assets/images/barco2.png'))
    g_canvas.create_image(100, 420, anchor= tk.N, image=pos_boat2)

    pos_boat3_label = tk.Label(text= "Sin Poner", font=("Sonic 1 HUD Font", 15), bg= "blue", fg= "#CDDEFF")
    pos_boat3_label.place(x= 200, y=490 + 15)
    pos_boat3= ImageTk.PhotoImage(Image.open('assets/images/barco3.png'))
    g_canvas.create_image(100, 490, anchor= tk.N, image=pos_boat3)

    def open_a():
        title_theme.stop()
        battle_theme.play(-1)
        g_canvas.destroy()
        g_canvas.quit
        attack()

    attack_b= tk.Button(g_canvas, text= "ATACAR", font= ("Sonic 1 HUD Font", 20), bg= "#4D6AA0", fg="#CDDEFF", command= open_a)
    attack_b.place(x= 100, y= 150)

    #Funciones para el tablero
    def place_boat(i, j, barco):

        global place_boat1
        global place_boat2
        global place_boat3
        global boat1_pos
        global boat2_pos
        global boat3_pos

        if barco == 1 and not place_boat1:
            player[j][i]= barco
            pos_boat1_label.config(text= f"[{i},{j}]")
            place_boat1 = True
            boat1_pos = f"[{i}, {j}]"

        elif barco == 2 and not place_boat2:
            try:
                player[j][i]= barco
                player [j][i+1]= barco
                pos_boat2_label.config(text= f"[{i},{j}], [{i+1},{j}]")
                place_boat2 = True
                boat2_pos = f"[{i}, {j}], [{i+1},{j}]"

            except IndexError:
                player[j][i]= barco
                player [j][i-1]= barco
                pos_boat2_label.config(text= f"[{i},{j}], [{i-1},{j}]")
                place_boat2 = True
                boat2_pos = f"[{i}, {j}], [{i-1},{j}]"

        elif barco == 3 and not place_boat3:
            player[j][i]= barco
            try:
                player[j][i+1]= barco
                player[j][i+2]= barco
                pos_boat3_label.config(text= f"[{i},{j}], [{i+1},{j}], [{i+2},{j}]")
                place_boat3 = True
                boat3_pos = f"[{i}, {j}], [{i+1},{j}], [{i+2},{j}]"

            except IndexError:
                player[j][i-1]= barco
                try:
                    player[j][i+1]= barco
                    pos_boat3_label.config(text= f"[{i},{j}], [{i-1},{j}], [{i+1},{j}]")
                    place_boat3 = True
                    boat3_pos = f"[{i}, {j}], [{i-1},{j}], [{i+1},{j}]"

                except IndexError:
                    player[j][i-1]= barco
                    player[j][i-2]= barco
                    pos_boat3_label.config(text= f"[{i},{j}], [{i-2},{j}], [{i-1},{j}]")
                    place_boat3 = True
                    boat3_pos = f"[{i}, {j}], [{i-1},{j}], [{i-2},{j}]"

        print (player)
        
    def select_boat(value):
        global barco 
        if value == 1 or value == 2 or value == 3:
            barco = value
        else:
            print("You filthy hacker lol")

    def enemy_boats(boat):
        i = random.randint(0,9)
        j = random.randint(0,9)

        if boat == 1 and enemy[j][i] == 0:
            enemy[j][i] = boat
            print(f"[{i},{j}]")
            
        elif boat == 2 and enemy[j][i] == 0:
            try:
                enemy[j][i]= boat
                enemy[j][i+1]= boat
                print(f"[{i},{j}], [{i+1},{j}]")

            except IndexError:
                enemy[j][i]= boat
                enemy[j][i-1]= boat
                print(f"[{i},{j}], [{i-1},{j}]")

        elif boat == 3 and enemy[j][i] == 0:
            enemy[j][i]= boat
            try:
                enemy[j][i+1]= boat
                enemy[j][i+2]= boat
                print(f"[{i},{j}], [{i+1},{j}], [{i+2},{j}]")

            except IndexError:
                enemy[j][i-1]= boat
                try:
                    enemy[j][i+1]= boat
                    print(f"[{i},{j}], [{i+1},{j}], [{i-1},{j}]")

                except IndexError:
                    enemy[j][i-1]= boat
                    enemy[j][i-2]= boat
                    print(f"[{i},{j}], [{i-1},{j}], [{i-2},{j}]")
        else:
            enemy_boats(boat)

    enemy_boats(1)
    enemy_boats(2)
    enemy_boats(3)
    print("enemy:",enemy)

    #El Tablero AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

    a1 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(0,0,barco))
    a2 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(1,0,barco))
    a3 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(2,0,barco))
    a4 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(3,0,barco))
    a5 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(4,0,barco))
    a6 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(5,0,barco))
    a7 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(6,0,barco))
    a8 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(7,0,barco))
    a9 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(8,0,barco))
    a10 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(9,0,barco))

    a1.place(x=300 + 100 , y= 100)
    a2.place(x=300 + 150 , y= 100)
    a3.place(x=300 + 200 , y= 100)
    a4.place(x=300 + 250 , y= 100)
    a5.place(x=300 + 300 , y= 100)
    a6.place(x=300 + 350 , y= 100)
    a7.place(x=300 + 400 , y= 100)
    a8.place(x=300 + 450 , y= 100)
    a9.place(x=300 + 500 , y= 100)
    a10.place(x=300 + 550 , y= 100)

    #El Tablero BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB

    b1 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(0,1,barco))
    b2 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(1,1,barco))
    b3 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(2,1,barco))
    b4 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(3,1,barco))
    b5 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(4,1,barco))
    b6 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(5,1,barco))
    b7 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(6,1,barco))
    b8 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(7,1,barco))
    b9 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(8,1,barco))
    b10 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(9,1,barco))

    b1.place(x=300 + 100 , y= 150)
    b2.place(x=300 + 150 , y= 150)
    b3.place(x=300 + 200 , y= 150)
    b4.place(x=300 + 250 , y= 150)
    b5.place(x=300 + 300 , y= 150)
    b6.place(x=300 + 350 , y= 150)
    b7.place(x=300 + 400 , y= 150)
    b8.place(x=300 + 450 , y= 150)
    b9.place(x=300 + 500 , y= 150)
    b10.place(x=300 + 550 , y= 150)
    
    #El Tablero AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

    c1 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(0,2,barco))
    c2 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(1,2,barco))
    c3 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(2,2,barco))
    c4 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(3,2,barco))
    c5 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(4,2,barco))
    c6 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(5,2,barco))
    c7 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(6,2,barco))
    c8 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(7,2,barco))
    c9 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(8,2,barco))
    c10 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(9,2,barco))

    c1.place(x=300 + 100 , y= 200)
    c2.place(x=300 + 150 , y= 200)
    c3.place(x=300 + 200 , y= 200)
    c4.place(x=300 + 250 , y= 200)
    c5.place(x=300 + 300 , y= 200)
    c6.place(x=300 + 350 , y= 200)
    c7.place(x=300 + 400 , y= 200)
    c8.place(x=300 + 450 , y= 200)
    c9.place(x=300 + 500 , y= 200)
    c10.place(x=300 + 550 , y= 200)

    #El Tablero BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB

    d1 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(0,3,barco))
    d2 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(1,3,barco))
    d3 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(2,3,barco))
    d4 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(3,3,barco))
    d5 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(4,3,barco))
    d6 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(5,3,barco))
    d7 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(6,3,barco))
    d8 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(7,3,barco))
    d9 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(8,3,barco))
    d10 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(9,3,barco))

    d1.place(x=300 + 100 , y= 250)
    d2.place(x=300 + 150 , y= 250)
    d3.place(x=300 + 200 , y= 250)
    d4.place(x=300 + 250 , y= 250)
    d5.place(x=300 + 300 , y= 250)
    d6.place(x=300 + 350 , y= 250)
    d7.place(x=300 + 400 , y= 250)
    d8.place(x=300 + 450 , y= 250)
    d9.place(x=300 + 500 , y= 250)
    d10.place(x=300 + 550 , y= 250)

    #El Tablero AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

    e1 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(0,4,barco))
    e2 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(1,4,barco))
    e3 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(2,4,barco))
    e4 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(3,4,barco))
    e5 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(4,4,barco))
    e6 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(5,4,barco))
    e7 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(6,4,barco))
    e8 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(7,4,barco))
    e9 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(8,4,barco))
    e10 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(9,4,barco))

    e1.place(x=300 + 100 , y= 300)
    e2.place(x=300 + 150 , y= 300)
    e3.place(x=300 + 200 , y= 300)
    e4.place(x=300 + 250 , y= 300)
    e5.place(x=300 + 300 , y= 300)
    e6.place(x=300 + 350 , y= 300)
    e7.place(x=300 + 400 , y= 300)
    e8.place(x=300 + 450 , y= 300)
    e9.place(x=300 + 500 , y= 300)
    e10.place(x=300 + 550 , y= 300)

    #El Tablero BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB

    f1 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(0,5,barco))
    f2 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(1,5,barco))
    f3 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(2,5,barco))
    f4 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(3,5,barco))
    f5 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(4,5,barco))
    f6 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(5,5,barco))
    f7 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(6,5,barco))
    f8 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(7,5,barco))
    f9 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(8,5,barco))
    f10 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(9,5,barco))

    f1.place(x=300 + 100 , y= 350)
    f2.place(x=300 + 150 , y= 350)
    f3.place(x=300 + 200 , y= 350)
    f4.place(x=300 + 250 , y= 350)
    f5.place(x=300 + 300 , y= 350)
    f6.place(x=300 + 350 , y= 350)
    f7.place(x=300 + 400 , y= 350)
    f8.place(x=300 + 450 , y= 350)
    f9.place(x=300 + 500 , y= 350)
    f10.place(x=300 + 550 , y= 350)
    
    #El Tablero AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

    g1 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(0,6,barco))
    g2 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(1,6,barco))
    g3 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(2,6,barco))
    g4 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(3,6,barco))
    g5 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(4,6,barco))
    g6 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(5,6,barco))
    g7 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(6,6,barco))
    g8 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(7,6,barco))
    g9 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(8,6,barco))
    g10 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(9,6,barco))

    g1.place(x=300 + 100 , y= 400)
    g2.place(x=300 + 150 , y= 400)
    g3.place(x=300 + 200 , y= 400)
    g4.place(x=300 + 250 , y= 400)
    g5.place(x=300 + 300 , y= 400)
    g6.place(x=300 + 350 , y= 400)
    g7.place(x=300 + 400 , y= 400)
    g8.place(x=300 + 450 , y= 400)
    g9.place(x=300 + 500 , y= 400)
    g10.place(x=300 + 550 , y= 400)

    #El Tablero BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB

    h1 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(0,7,barco))
    h2 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(1,7,barco))
    h3 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(2,7,barco))
    h4 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(3,7,barco))
    h5 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(4,7,barco))
    h6 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(5,7,barco))
    h7 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(6,7,barco))
    h8 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(7,7,barco))
    h9 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(8,7,barco))
    h10 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(9,7,barco))

    h1.place(x=300 + 100 , y= 450)
    h2.place(x=300 + 150 , y= 450)
    h3.place(x=300 + 200 , y= 450)
    h4.place(x=300 + 250 , y= 450)
    h5.place(x=300 + 300 , y= 450)
    h6.place(x=300 + 350 , y= 450)
    h7.place(x=300 + 400 , y= 450)
    h8.place(x=300 + 450 , y= 450)
    h9.place(x=300 + 500 , y= 450)
    h10.place(x=300 + 550 , y= 450)

    #El Tablero BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB

    i1 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(0,8,barco))
    i2 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(1,8,barco))
    i3 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(2,8,barco))
    i4 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(3,8,barco))
    i5 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(4,8,barco))
    i6 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(5,8,barco))
    i7 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(6,8,barco))
    i8 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(7,8,barco))
    i9 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(8,8,barco))
    i10 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(9,8,barco))

    i1.place(x=300 + 100 , y= 500)
    i2.place(x=300 + 150 , y= 500)
    i3.place(x=300 + 200 , y= 500)
    i4.place(x=300 + 250 , y= 500)
    i5.place(x=300 + 300 , y= 500)
    i6.place(x=300 + 350 , y= 500)
    i7.place(x=300 + 400 , y= 500)
    i8.place(x=300 + 450 , y= 500)
    i9.place(x=300 + 500 , y= 500)
    i10.place(x=300 + 550 , y= 500)
    #El Tablero BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB

    j1 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(0,9,barco))
    j2 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(1,9,barco))
    j3 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(2,9,barco))
    j4 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(3,9,barco))
    j5 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(4,9,barco))
    j6 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(5,9,barco))
    j7 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(6,9,barco))
    j8 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(7,9,barco))
    j9 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(8,9,barco))
    j10 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: place_boat(9,9,barco))

    j1.place(x=300 + 100 , y= 550)
    j2.place(x=300 + 150 , y= 550)
    j3.place(x=300 + 200 , y= 550)
    j4.place(x=300 + 250 , y= 550)
    j5.place(x=300 + 300 , y= 550)
    j6.place(x=300 + 350 , y= 550)
    j7.place(x=300 + 400 , y= 550)
    j8.place(x=300 + 450 , y= 550)
    j9.place(x=300 + 500 , y= 550)
    j10.place(x=300 + 550 , y= 550)

    g_canvas.mainloop()

def attack():
    a_canvas= tk.Canvas(window, width=1280, height=720, borderwidth=0, highlightthickness=0, bg="blue")
    window.title('Battleship! - Attack')
    a_canvas.pack()

    inicio = time.time()
    global turnos
    global aciertos
    global fallos
    global curEnemy1 
    global curEnemy2 
    global curEnemy3 
    global curPlayer1
    global curPlayer2
    global curPlayer3
    
    turnos = 0
    aciertos = 0
    fallos = 0

    curEnemy1 = 1
    curEnemy2 = 2
    curEnemy3 = 3
    curPlayer1 = 1
    curPlayer2 = 2
    curPlayer3 = 3

    hit_sound = pygame.mixer.Sound('assets/sound/sfx/hit.wav')
    hit_sound.set_volume(0.35)
    hit_confirm_sound = pygame.mixer.Sound('assets/sound/sfx/hitConfirm.wav')
    hit_confirm_sound.set_volume(0.35)
    miss_sound = pygame.mixer.Sound("assets/sound/sfx/miss.wav")
    miss_sound.set_volume(0.35)

    player_status= tk.Label(text= "Player Status", font=("Sonic 1 HUD Font", 20), bg= "blue", fg= "#CDDEFF")
    player_status.place(x= 1000, y= 150)
    player_info= tk.Label(text= "None", font=("Sonic 1 HUD Font", 20), bg= "blue", fg= "#CDDEFF")
    player_info.place(x= 1050, y= 200)

    enemy_status= tk.Label(text= "Enemy Status", font=("Sonic 1 HUD Font", 20), bg= "blue", fg= "#CDDEFF")
    enemy_status.place(x= 1000, y= 400)
    enemy_info= tk.Label(text= "None", font=("Sonic 1 HUD Font", 20), bg= "blue", fg= "#CDDEFF")
    enemy_info.place(x= 1050, y= 450)
    
    pos_boat1_label = tk.Label(text= boat1_pos, font=("Sonic 1 HUD Font", 15), bg= "blue", fg= "#CDDEFF")
    pos_boat1_label.place(x= 200, y= 350 + 15)
    pos_boat1= ImageTk.PhotoImage(Image.open('assets/images/barco1.png'))
    a_canvas.create_image(100, 350, anchor= tk.N, image=pos_boat1)

    pos_boat2_label = tk.Label(text= boat2_pos, font=("Sonic 1 HUD Font", 15), bg= "blue", fg= "#CDDEFF")
    pos_boat2_label.place(x= 200, y=420 + 15)
    pos_boat2= ImageTk.PhotoImage(Image.open('assets/images/barco2.png'))
    a_canvas.create_image(100, 420, anchor= tk.N, image=pos_boat2)

    pos_boat3_label = tk.Label(text= boat3_pos, font=("Sonic 1 HUD Font", 15), bg= "blue", fg= "#CDDEFF")
    pos_boat3_label.place(x= 200, y=490 + 15)
    pos_boat3= ImageTk.PhotoImage(Image.open('assets/images/barco3.png'))
    a_canvas.create_image(100, 490, anchor= tk.N, image=pos_boat3)

    def enemy_attack():
        global curPlayer1
        global curPlayer2
        global curPlayer3
        
        global turnos
        global aciertos
        global fallos

        i = random.randint(0,9)
        j = random.randint(0,9)

        if player [j][i] == 1:
            curPlayer1 -= 1
            hit_confirm_sound.play()
            turnos += 1
            enemy_info.config(text= "HIT")
        
        elif player [j][i] == 2:
            curPlayer2 -= 1
            turnos += 1

            if curPlayer2 == 0:
                hit_confirm_sound.play()
            else:
                hit_sound.play()
            enemy_info.config(text= "HIT")
        
        elif player [j][i] == 3:
            curPlayer3 -= 1
            turnos += 1

            if curPlayer3 == 0:
                hit_confirm_sound.play()
            else:
                hit_sound.play()
            enemy_info.config(text= "HIT")
        
        else:
            miss_sound.play()
            turnos += 1
            print('miss')
            enemy_info.config(text= "MISS")

        if curPlayer1 == 0 and curPlayer2 == 0 and curPlayer3 == 0:
            print('perdiste :(')
            a_canvas.destroy()
            a_canvas.quit
            battle_theme.stop()
            title_theme.play()
            fin = time.time()
            tiempo = int(fin - inicio)
            gameOver(turnos, tiempo, fallos, aciertos)
            
    def attack_boat(i, j, button):
        global curEnemy1
        global curEnemy2
        global curEnemy3
        global turnos
        global aciertos
        global fallos

        print(f"[{i},{j}]")

        if enemy[j][i] == 1:
            curEnemy1 -= 1
            turnos += 1
            aciertos += 1
            hit_confirm_sound.play()
            button.config(bg = 'red')
            print('hit')
            player_info.config(text= "HIT")

        elif enemy[j][i] == 2:
            button.config(bg = 'red')
            curEnemy2 -= 1
            turnos += 1
            aciertos += 1
            if curEnemy2 == 0:
                hit_confirm_sound.play()
            else:
                hit_sound.play()
            print('hit')
            player_info.config(text= "HIT")

        elif enemy[j][i] == 3:
            curEnemy3 -= 1
            turnos += 1
            aciertos += 1
            if curEnemy3 == 0:
                hit_confirm_sound.play()
            else:
                hit_sound.play()
            button.config(bg = 'red')
            print('hit')
            player_info.config(text= "HIT")

        else:
            miss_sound.play()
            turnos += 1
            fallos += 1
            button.config(bg = 'white')
            print('miss')
            player_info.config(text= "MISS")
            enemy_attack()

        if curEnemy1 == 0 and curEnemy2 == 0 and curEnemy3 == 0:
            print('ganaste!')
            a_canvas.destroy()
            a_canvas.quit
            battle_theme.stop()
            title_theme.play()
            fin = time.time()
            tiempo = fin - inicio
            gameOver(turnos, tiempo, fallos, aciertos)

    #El Tablero AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

    a1 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(0,0,a1))
    a2 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(1,0,a2))
    a3 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(2,0,a3))
    a4 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(3,0,a4))
    a5 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(4,0,a5))
    a6 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(5,0,a6))
    a7 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(6,0,a7))
    a8 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(7,0,a8))
    a9 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(8,0,a9))
    a10 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(9,0,a10))

    a1.place(x=300 + 100 , y= 100)
    a2.place(x=300 + 150 , y= 100)
    a3.place(x=300 + 200 , y= 100)
    a4.place(x=300 + 250 , y= 100)
    a5.place(x=300 + 300 , y= 100)
    a6.place(x=300 + 350 , y= 100)
    a7.place(x=300 + 400 , y= 100)
    a8.place(x=300 + 450 , y= 100)
    a9.place(x=300 + 500 , y= 100)
    a10.place(x=300 + 550 , y= 100)

    #El Tablero BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB

    b1 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(0,1,b1))
    b2 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(1,1,b2))
    b3 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(2,1,b3))
    b4 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(3,1,b4))
    b5 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(4,1,b5))
    b6 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(5,1,b6))
    b7 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(6,1,b7))
    b8 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(7,1,b8))
    b9 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(8,1,b9))
    b10 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(9,1,b10))

    b1.place(x=300 + 100 , y= 150)
    b2.place(x=300 + 150 , y= 150)
    b3.place(x=300 + 200 , y= 150)
    b4.place(x=300 + 250 , y= 150)
    b5.place(x=300 + 300 , y= 150)
    b6.place(x=300 + 350 , y= 150)
    b7.place(x=300 + 400 , y= 150)
    b8.place(x=300 + 450 , y= 150)
    b9.place(x=300 + 500 , y= 150)
    b10.place(x=300 + 550 , y= 150)
    
    #El Tablero AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

    c1 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(0,2, c1))
    c2 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(1,2, c2))
    c3 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(2,2, c3))
    c4 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(3,2, c4))
    c5 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(4,2, c5))
    c6 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(5,2, c6))
    c7 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(6,2, c7))
    c8 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(7,2, c8))
    c9 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(8,2, c9))
    c10 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(9,2, c10))

    c1.place(x=300 + 100 , y= 200)
    c2.place(x=300 + 150 , y= 200)
    c3.place(x=300 + 200 , y= 200)
    c4.place(x=300 + 250 , y= 200)
    c5.place(x=300 + 300 , y= 200)
    c6.place(x=300 + 350 , y= 200)
    c7.place(x=300 + 400 , y= 200)
    c8.place(x=300 + 450 , y= 200)
    c9.place(x=300 + 500 , y= 200)
    c10.place(x=300 + 550 , y= 200)

    #El Tablero BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB

    d1 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(0,3, d1))
    d2 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(1,3, d2))
    d3 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(2,3, d3))
    d4 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(3,3, d4))
    d5 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(4,3, d5))
    d6 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(5,3, d6))
    d7 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(6,3, d7))
    d8 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(7,3, d8))
    d9 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(8,3, d9))
    d10 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(9,3, d10))

    d1.place(x=300 + 100 , y= 250)
    d2.place(x=300 + 150 , y= 250)
    d3.place(x=300 + 200 , y= 250)
    d4.place(x=300 + 250 , y= 250)
    d5.place(x=300 + 300 , y= 250)
    d6.place(x=300 + 350 , y= 250)
    d7.place(x=300 + 400 , y= 250)
    d8.place(x=300 + 450 , y= 250)
    d9.place(x=300 + 500 , y= 250)
    d10.place(x=300 + 550 , y= 250)

    #El Tablero AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

    e1 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(0,4,e1))
    e2 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(1,4,e2))
    e3 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(2,4,e3))
    e4 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(3,4,e4))
    e5 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(4,4,e5))
    e6 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(5,4,e6))
    e7 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(6,4,e7))
    e8 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(7,4,e8))
    e9 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(8,4,e9))
    e10 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(9,4,e10))

    e1.place(x=300 + 100 , y= 300)
    e2.place(x=300 + 150 , y= 300)
    e3.place(x=300 + 200 , y= 300)
    e4.place(x=300 + 250 , y= 300)
    e5.place(x=300 + 300 , y= 300)
    e6.place(x=300 + 350 , y= 300)
    e7.place(x=300 + 400 , y= 300)
    e8.place(x=300 + 450 , y= 300)
    e9.place(x=300 + 500 , y= 300)
    e10.place(x=300 + 550 , y= 300)

    #El Tablero BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB

    f1 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(0,5,f1))
    f2 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(1,5,f2))
    f3 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(2,5,f3))
    f4 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(3,5,f4))
    f5 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(4,5,f5))
    f6 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(5,5,f6))
    f7 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(6,5,f7))
    f8 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(7,5,f8))
    f9 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(8,5,f9))
    f10 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(9,5,f10))

    f1.place(x=300 + 100 , y= 350)
    f2.place(x=300 + 150 , y= 350)
    f3.place(x=300 + 200 , y= 350)
    f4.place(x=300 + 250 , y= 350)
    f5.place(x=300 + 300 , y= 350)
    f6.place(x=300 + 350 , y= 350)
    f7.place(x=300 + 400 , y= 350)
    f8.place(x=300 + 450 , y= 350)
    f9.place(x=300 + 500 , y= 350)
    f10.place(x=300 + 550 , y= 350)
    
    #El Tablero AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

    g1 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(0,6,g1))
    g2 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(1,6,g2))
    g3 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(2,6,g3))
    g4 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(3,6,g4))
    g5 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(4,6,g5))
    g6 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(5,6,g6))
    g7 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(6,6,g7))
    g8 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(7,6,g8))
    g9 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(8,6,g9))
    g10 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(9,6,g10))

    g1.place(x=300 + 100 , y= 400)
    g2.place(x=300 + 150 , y= 400)
    g3.place(x=300 + 200 , y= 400)
    g4.place(x=300 + 250 , y= 400)
    g5.place(x=300 + 300 , y= 400)
    g6.place(x=300 + 350 , y= 400)
    g7.place(x=300 + 400 , y= 400)
    g8.place(x=300 + 450 , y= 400)
    g9.place(x=300 + 500 , y= 400)
    g10.place(x=300 + 550 , y= 400)

    #El Tablero BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB

    h1 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(0,7,h1))
    h2 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(1,7,h2))
    h3 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(2,7,h3))
    h4 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(3,7,h4))
    h5 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(4,7,h5))
    h6 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(5,7,h6))
    h7 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(6,7,h7))
    h8 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(7,7,h8))
    h9 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(8,7,h9))
    h10 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(9,7,h10))

    h1.place(x=300 + 100 , y= 450)
    h2.place(x=300 + 150 , y= 450)
    h3.place(x=300 + 200 , y= 450)
    h4.place(x=300 + 250 , y= 450)
    h5.place(x=300 + 300 , y= 450)
    h6.place(x=300 + 350 , y= 450)
    h7.place(x=300 + 400 , y= 450)
    h8.place(x=300 + 450 , y= 450)
    h9.place(x=300 + 500 , y= 450)
    h10.place(x=300 + 550 , y= 450)

    #El Tablero BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB

    i1 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(0,8, i1))
    i2 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(1,8, i2))
    i3 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(2,8, i3))
    i4 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(3,8, i4))
    i5 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(4,8, i5))
    i6 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(5,8, i6))
    i7 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(6,8, i7))
    i8 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(7,8, i8))
    i9 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(8,8, i9))
    i10 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(9,8, i10))

    i1.place(x=300 + 100 , y= 500)
    i2.place(x=300 + 150 , y= 500)
    i3.place(x=300 + 200 , y= 500)
    i4.place(x=300 + 250 , y= 500)
    i5.place(x=300 + 300 , y= 500)
    i6.place(x=300 + 350 , y= 500)
    i7.place(x=300 + 400 , y= 500)
    i8.place(x=300 + 450 , y= 500)
    i9.place(x=300 + 500 , y= 500)
    i10.place(x=300 + 550 , y= 500)

    #El Tablero BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB

    j1 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(0,9, j1))
    j2 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(1,9, j2))
    j3 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(2,9, j3))
    j4 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(3,9, j4))
    j5 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(4,9, j5))
    j6 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(5,9, j6))
    j7 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(6,9, j7))
    j8 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(7,9, j8))
    j9 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(8,9, j9))
    j10 = tk.Button(a_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF", command= lambda: attack_boat(9,9, j10))

    j1.place(x=300 + 100 , y= 550)
    j2.place(x=300 + 150 , y= 550)
    j3.place(x=300 + 200 , y= 550)
    j4.place(x=300 + 250 , y= 550)
    j5.place(x=300 + 300 , y= 550)
    j6.place(x=300 + 350 , y= 550)
    j7.place(x=300 + 400 , y= 550)
    j8.place(x=300 + 450 , y= 550)
    j9.place(x=300 + 500 , y= 550)
    j10.place(x=300 + 550 , y= 550)

    a_canvas.mainloop()

def gameOver(turnos, tiempo, fallos, aciertos):
    o_canvas= tk.Canvas(window, width=1280, height=720, borderwidth=0, highlightthickness=0, bg="black")
    window.title('Battleship! - Game Over')
    o_canvas.pack()

    #Titulo
    title= ImageTk.PhotoImage(Image.open('assets/images/logo.png'))
    o_canvas.create_image(240, 65, anchor= tk.NW, image=title)
    
    #Calcula los turnos
    turnos_label = tk.Label(text= f"Turnos: {turnos}", font=("Sonic 1 HUD Font", 35), bg= 'black', fg= 'white')
    turnos_label.place(x=150, y=300)

    #Calcula los Tiempo de Partida
    tiempo_label = tk.Label(text= f"Tiempo de Partida: {tiempo}", font=("Sonic 1 HUD Font", 35), bg= 'black', fg= 'white')
    tiempo_label.place(x=150, y=380)

    #Calcula los Tiempo de Partida
    aciertos_label = tk.Label(text= f"Aciertos del Jugador: {aciertos}", font=("Sonic 1 HUD Font", 35), bg= 'black', fg= 'white')
    aciertos_label.place(x=150, y=460)

    #Calcula los Tiempo de Partida
    fallos_label = tk.Label(text= f"Fallos del Jugador: {fallos}", font=("Sonic 1 HUD Font", 35), bg= 'black', fg= 'white')
    fallos_label.place(x=150, y=540)

    var = tk.StringVar()
    entry = tk.Entry(font=("Sonic 1 HUD Font", 35), textvariable=var, justify=tk.CENTER, width= 10)
    entry.place(x=950, y=375)

    def saving_the_funni():
        if var.get() != '':
            save_data(turnos, var.get())
            select_sounds[random.randint(0,2)].play()
            o_canvas.destroy()
            o_canvas.quit
            highscore()

    save_button = tk.Button(o_canvas, text="Guardar Nombre", font=("Sonic 1 HUD Font", 20), fg="#ffffff", bg="#18191c", command=saving_the_funni)
    save_button.place(x = 1000, y = 450)

    o_canvas.mainloop()

def play():
    p_canvas= tk.Canvas(window, width=1280, height=720, borderwidth=0, highlightthickness=0, bg="black")
    window.title('Battleship! - File System')
    p_canvas.pack()
    
    #Boton para cerrar selccion de partida
    def close_p():
        select_sounds[random.randint(0,2)].play()
        p_canvas.destroy()
        p_canvas.quit
        main()
    
    def open_file1():
        select_sounds[random.randint(0,2)].play()
        p_canvas.destroy()
        p_canvas.quit
        game()
    
    def open_file2():
        select_sounds[random.randint(0,2)].play()
        p_canvas.destroy()
        p_canvas.quit
        game()
    
    def open_file3():
        select_sounds[random.randint(0,2)].play()
        p_canvas.destroy()
        p_canvas.quit
        game()

    closep_b= tk.Button(p_canvas, text= "Volver", font= ("Sonic 1 HUD Font", 20), bg= "black", fg="white", command= close_p)
    closep_b.place(x= 50, y= 50)

    fileb_1= tk.Button(p_canvas, text= " File 1 ", font= ("Sonic 1 HUD Font", 60), bg= "black", fg="white", command= open_file1)
    fileb_1.place(x= 464, y= 100)

    fileb_2= tk.Button(p_canvas, text= " File 2 ", font= ("Sonic 1 HUD Font", 60), bg= "black", fg="white", command= open_file2)
    fileb_2.place(x= 464, y= 300)

    fileb_3= tk.Button(p_canvas, text= " File 3 ", font= ("Sonic 1 HUD Font", 60), bg= "black", fg="white", command= open_file3)
    fileb_3.place(x= 464, y= 500)

    p_canvas.mainloop()

def highscore():

    hs_canvas= tk.Canvas(window, width=1280, height=720, borderwidth=0, highlightthickness=0, bg="black")
    window.title('Battleship! - Hall of Fame')
    hs_canvas.pack()

    score1 = tk.Label(text=f"1st.", font=("Sonic 1 HUD Font", 25), fg='#ffffff', bg="#000000")
    score1.place(x= 450, y= 250)

    score2 = tk.Label(text=f"2nd.", font=("Sonic 1 HUD Font", 25), fg='#ffffff', bg="#000000")
    score2.place(x= 450, y= 330)

    score3 = tk.Label(text=f"3rd.", font=("Sonic 1 HUD Font", 25), fg='#ffffff', bg="#000000")
    score3.place(x= 450, y= 410)

    score4 = tk.Label(text=f"4rd.", font=("Sonic 1 HUD Font", 25), fg='#ffffff', bg="#000000")
    score4.place(x= 450, y= 490)

    score5 = tk.Label(text=f"5th.", font=("Sonic 1 HUD Font", 25), fg='#ffffff', bg="#000000")
    score5.place(x= 450, y= 570)

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

    def set_scores(lista):

        if lista == []:
            return
        
        else:
            if lista[-5][0] != '':
                score5.config(text= '5th. ' + lista[-5][1] + ' - ' + lista[-5][0] + ' turnos')
            else:
                score4.config(text= '5th. Nadie')

            if lista[-4][0] != '':
                score4.config(text= '4th. ' + lista[-4][1] + ' - ' + lista[-4][0] + ' turnos')
            else:
                score4.config(text= '4th. Nadie')

            if lista[-3][0] != '':

                score3.config(text= '3rd. ' + lista[-3][1] + ' - ' + lista[-3][0] + ' turnos') 
            else:
                score3.config(text= '3rd. Nadie')

            if lista[-2][0] != '':
                score2.config(text= '2nd. ' + lista[-2][1] + ' - ' + lista[-2][0] + ' turnos')
            else:
                score1.config(text= '2nd. Nadie')

            if lista[-1][0] != '':
                score1.config(text= '1st. ' + lista[-1][1] + ' - ' + lista[-1][0] + ' turnos')     
            else:
                score1.config(text= '1st. Nadie')


    scores = organize_score_list()
    set_scores(scores)

    #Boton para cerrar salon de la fama
    def close_hs():
        select_sounds[random.randint(0,2)].play()
        hs_canvas.destroy()
        hs_canvas.quit
        main()
    closehs_b= tk.Button(hs_canvas, text= "Volver", font= ("Sonic 1 HUD Font", 20), bg= "black", fg="white", command= close_hs)
    closehs_b.place(x=50, y=50)

    hs_canvas.mainloop()

def help():
    help_canvas= tk.Canvas(window, width=1280, height=720, borderwidth=0, highlightthickness=0, bg="black")
    window.title('Battleship! - Help Screen')
    help_canvas.pack()

    #Boton para cerrar ayuda
    def close_help():
        select_sounds[random.randint(0,2)].play()
        help_canvas.destroy()
        help_canvas.quit
        main()
    close_help_b= tk.Button(help_canvas, text= "Volver", font= ("Sonic 1 HUD Font", 20), bg= "black", fg="white", command= close_help)
    close_help_b.place(x= 50, y= 40)

    ship3= ImageTk.PhotoImage(Image.open('assets/images/barco3.png'))
    help_canvas.create_image(100, 590, anchor= tk.NW, image=ship3)

    ship2= ImageTk.PhotoImage(Image.open('assets/images/barco2.png'))
    help_canvas.create_image(500, 590, anchor= tk.NW, image=ship2)

    ship1= ImageTk.PhotoImage(Image.open('assets/images/barco1.png'))
    help_canvas.create_image(1000, 590, anchor= tk.NW, image=ship1)

    title1= tk.Label(help_canvas, text= "Hola! Bienvenido a Battleship", font= ("Sonic 1 HUD Font", 20), bg= "black", fg= "white")
    title1.place(x= 50, y=110)

    title2= tk.Label(help_canvas, text= "En este juego, tu objetivo sera hundir los tres barcos enemigos", font= ("Sonic 1 HUD Font", 20), bg= "black", fg= "white")
    title2.place(x= 50, y=160)

    title3= tk.Label(help_canvas, text= "Esto sera logrado mediante el uso de un tablero de 10x10", font= ("Sonic 1 HUD Font", 20), bg= "black", fg= "white")
    title3.place(x= 50, y=210)

    title4= tk.Label(help_canvas, text= "El jugador debera colocar 3 barcos en el tablero", font= ("Sonic 1 HUD Font", 20), bg= "black", fg= "white")
    title4.place(x= 50, y=260)

    title5= tk.Label(help_canvas, text= "Los barcos tiene tama??os de 1, 2 y 3 espacios cada uno", font= ("Sonic 1 HUD Font", 20), bg= "black", fg= "white")
    title5.place(x= 50, y=310)

    title6= tk.Label(help_canvas, text= "Luego deber?? elegir en el tablero, las coordenadas donde piensa que hay un barco enemigo", font= ("Sonic 1 HUD Font", 20), bg= "black", fg= "white")
    title6.place(x= 50, y=360)

    title7= tk.Label(help_canvas, text= "Al clickear en este, se le avisar?? al jugador si fall??, si le dio a un barco, o si hundi?? alg??n barco", font= ("Sonic 1 HUD Font", 20), bg= "black", fg= "white")
    title7.place(x= 50, y=410)

    title8= tk.Label(help_canvas, text= "A continuaci??n, la computadora eligir?? un punto en donde disparar para asi hundir los barcos del jugador", font= ("Sonic 1 HUD Font", 20), bg= "black", fg= "white")
    title8.place(x= 50, y=460)

    title9= tk.Label(help_canvas, text= "El primero en hundir los barcos del oponente, ser?? el ganador!", font= ("Sonic 1 HUD Font", 20), bg= "black", fg= "white")
    title9.place(x= 50, y=510)

    help_canvas.mainloop()

main()