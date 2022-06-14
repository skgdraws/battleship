import random
import tkinter as tk
import pygame
#from PIL import ImageTk, Image
from support import *
import pathlib

pygame.init()
window= tk.Tk()
window.geometry("1280x720")
window.title("Battleship!")
window.resizable(False, False)

#Efectos de Sonido
select1 = pygame.mixer.Sound("assets/sound/sfx/select1.wav")
select1.set_volume(0.5)
select2 = pygame.mixer.Sound("assets/sound/sfx/select2.wav")
select2.set_volume(0.5)
select3 = pygame.mixer.Sound("assets/sound/sfx/select3.wav")
select3.set_volume(0.5)
select_sounds = [select1, select2, select3]

player = [[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
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
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]

def main():
    canvas= tk.Canvas(window, width=1280, height=720, borderwidth=0, highlightthickness=0, bg="black")
    canvas.pack()

    #Titulo
    #title= ImageTk.PhotoImage(Image.open('assets/images/logo.png'))
    #canvas.create_image(240, 65, anchor= tk.NW, image=title)

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
    g_canvas.pack()

    #Selección de Barcos (Imágenes)
    #boat1= ImageTk.PhotoImage(Image.open('assets/images/barco1.png'))
    #g_canvas.create_image(1150, 50, anchor= tk.N, image=boat1)

    #boat2= ImageTk.PhotoImage(Image.open('assets/images/barco2.png'))
    #g_canvas.create_image(1150, 250, anchor= tk.N, image=boat2)

    #boat3= ImageTk.PhotoImage(Image.open('assets/images/barco3.png'))
    #g_canvas.create_image(1085, 450, anchor= tk.NW, image=boat3)

    #Selección de Barcos (Botones)
    boat1_b= tk.Button(g_canvas, text= "BARCO 1", font= ("Sonic 1 HUD Font", 20), bg= "#4D6AA0", fg="#CDDEFF")
    boat1_b.place(x= 1100, y=150)

    boat2_b= tk.Button(g_canvas, text= "BARCO 2", font= ("Sonic 1 HUD Font", 20), bg= "#4D6AA0", fg="#CDDEFF")
    boat2_b.place(x= 1100, y=350)

    boat3_b= tk.Button(g_canvas, text= "BARCO 3", font= ("Sonic 1 HUD Font", 20), bg= "#4D6AA0", fg="#CDDEFF")
    boat3_b.place(x= 1100, y=550)

    #El Tablero AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

    a1 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    a2 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    a3 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    a4 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    a5 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    a6 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    a7 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    a8 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    a9 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    a10 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")

    a1.place(x=250 + 100 , y= 100)
    a2.place(x=250 + 150 , y= 100)
    a3.place(x=250 + 200 , y= 100)
    a4.place(x=250 + 250 , y= 100)
    a5.place(x=250 + 300 , y= 100)
    a6.place(x=250 + 350 , y= 100)
    a7.place(x=250 + 400 , y= 100)
    a8.place(x=250 + 450 , y= 100)
    a9.place(x=250 + 500 , y= 100)
    a10.place(x=250 + 550 , y= 100)

    #El Tablero BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB

    b1 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    b2 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    b3 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    b4 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    b5 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    b6 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    b7 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    b8 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    b9 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    b10 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")

    b1.place(x=250 + 100 , y= 150)
    b2.place(x=250 + 150 , y= 150)
    b3.place(x=250 + 200 , y= 150)
    b4.place(x=250 + 250 , y= 150)
    b5.place(x=250 + 300 , y= 150)
    b6.place(x=250 + 350 , y= 150)
    b7.place(x=250 + 400 , y= 150)
    b8.place(x=250 + 450 , y= 150)
    b9.place(x=250 + 500 , y= 150)
    b10.place(x=250 + 550 , y= 150)
    
    #El Tablero AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

    c1 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    c2 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    c3 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    c4 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    c5 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    c6 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    c7 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    c8 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    c9 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    c10 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")

    c1.place(x=250 + 100 , y= 150)
    c2.place(x=250 + 150 , y= 150)
    c3.place(x=250 + 200 , y= 150)
    c4.place(x=250 + 250 , y= 150)
    c5.place(x=250 + 300 , y= 150)
    c6.place(x=250 + 350 , y= 150)
    c7.place(x=250 + 400 , y= 150)
    c8.place(x=250 + 450 , y= 150)
    c9.place(x=250 + 500 , y= 150)
    c10.place(x=250 + 550 , y= 150)

    #El Tablero BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB

    d1 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    d2 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    d3 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    d4 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    d5 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    d6 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    d7 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    d8 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    d9 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    d10 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")

    d1.place(x=250 + 100 , y= 200)
    d2.place(x=250 + 150 , y= 200)
    d3.place(x=250 + 200 , y= 200)
    d4.place(x=250 + 250 , y= 200)
    d5.place(x=250 + 300 , y= 200)
    d6.place(x=250 + 350 , y= 200)
    d7.place(x=250 + 400 , y= 200)
    d8.place(x=250 + 450 , y= 200)
    d9.place(x=250 + 500 , y= 200)
    d10.place(x=250 + 550 , y= 200)

    #El Tablero AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

    e1 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    e2 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    e3 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    e4 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    e5 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    e6 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    e7 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    e8 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    e9 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    e10 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")

    e1.place(x=250 + 100 , y= 250)
    e2.place(x=250 + 150 , y= 250)
    e3.place(x=250 + 200 , y= 250)
    e4.place(x=250 + 250 , y= 250)
    e5.place(x=250 + 300 , y= 250)
    e6.place(x=250 + 350 , y= 250)
    e7.place(x=250 + 400 , y= 250)
    e8.place(x=250 + 450 , y= 250)
    e9.place(x=250 + 500 , y= 250)
    e10.place(x=250 + 550 , y= 250)

    #El Tablero BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB

    f1 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    f2 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    f3 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    f4 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    f5 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    f6 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    f7 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    f8 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    f9 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    f10 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")

    f1.place(x=250 + 100 , y= 300)
    f2.place(x=250 + 150 , y= 300)
    f3.place(x=250 + 200 , y= 300)
    f4.place(x=250 + 250 , y= 300)
    f5.place(x=250 + 300 , y= 300)
    f6.place(x=250 + 350 , y= 300)
    f7.place(x=250 + 400 , y= 300)
    f8.place(x=250 + 450 , y= 300)
    f9.place(x=250 + 500 , y= 300)
    f10.place(x=250 + 550 , y= 300)
    
    #El Tablero AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

    g1 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    g2 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    g3 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    g4 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    g5 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    g6 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    g7 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    g8 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    g9 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    g10 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")

    g1.place(x=250 + 100 , y= 350)
    g2.place(x=250 + 150 , y= 350)
    g3.place(x=250 + 200 , y= 350)
    g4.place(x=250 + 250 , y= 350)
    g5.place(x=250 + 300 , y= 350)
    g6.place(x=250 + 350 , y= 350)
    g7.place(x=250 + 400 , y= 350)
    g8.place(x=250 + 450 , y= 350)
    g9.place(x=250 + 500 , y= 350)
    g10.place(x=250 + 550 , y= 350)

    #El Tablero BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB

    h1 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    h2 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    h3 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    h4 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    h5 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    h6 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    h7 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    h8 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    h9 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    h10 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")

    h1.place(x=250 + 100 , y= 400)
    h2.place(x=250 + 150 , y= 400)
    h3.place(x=250 + 200 , y= 400)
    h4.place(x=250 + 250 , y= 400)
    h5.place(x=250 + 300 , y= 400)
    h6.place(x=250 + 350 , y= 400)
    h7.place(x=250 + 400 , y= 400)
    h8.place(x=250 + 450 , y= 400)
    h9.place(x=250 + 500 , y= 400)
    h10.place(x=250 + 550 , y= 400)

    #El Tablero BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB

    i1 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    i2 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    i3 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    i4 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    i5 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    i6 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    i7 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    i8 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    i9 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    i10 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")

    i1.place(x=250 + 100 , y= 450)
    i2.place(x=250 + 150 , y= 450)
    i3.place(x=250 + 200 , y= 450)
    i4.place(x=250 + 250 , y= 450)
    i5.place(x=250 + 300 , y= 450)
    i6.place(x=250 + 350 , y= 450)
    i7.place(x=250 + 400 , y= 450)
    i8.place(x=250 + 450 , y= 450)
    i9.place(x=250 + 500 , y= 450)
    i10.place(x=250 + 550 , y= 450)
    
    #El Tablero AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

    j1 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    j2 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    j3 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    j4 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    j5 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    j6 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    j7 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    j8 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    j9 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    j10 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")

    j1.place(x=250 + 100 , y= 500)
    j2.place(x=250 + 150 , y= 500)
    j3.place(x=250 + 200 , y= 500)
    j4.place(x=250 + 250 , y= 500)
    j5.place(x=250 + 300 , y= 500)
    j6.place(x=250 + 350 , y= 500)
    j7.place(x=250 + 400 , y= 500)
    j8.place(x=250 + 450 , y= 500)
    j9.place(x=250 + 500 , y= 500)
    j10.place(x=250 + 550 , y= 500)

    #El Tablero BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB

    k1 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    k2 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    k3 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    k4 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    k5 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    k6 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    k7 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    k8 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    k9 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")
    k10 = tk.Button(g_canvas, text= "   ", font= ("Sonic 1 HUD Font", 15), bg= "#444444", fg= "#CDDEFF")

    k1.place(x=250 + 100 , y= 550)
    k2.place(x=250 + 150 , y= 550)
    k3.place(x=250 + 200 , y= 550)
    k4.place(x=250 + 250 , y= 550)
    k5.place(x=250 + 300 , y= 550)
    k6.place(x=250 + 350 , y= 550)
    k7.place(x=250 + 400 , y= 550)
    k8.place(x=250 + 450 , y= 550)
    k9.place(x=250 + 500 , y= 550)
    k10.place(x=250 + 550 , y= 550)

    g_canvas.mainloop()


def play():
    p_canvas= tk.Canvas(window, width=1280, height=720, borderwidth=0, highlightthickness=0, bg="black")
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
            if lista[4][0] != '':

                score5.config(text= '5th. ' + lista[0][0] + ' turnos - ' + lista[0][1])

            if lista[3][0] != '':

                score4.config(text= '4th. ' + lista[1][0] + ' turnos - ' + lista[1][1])
            if lista[2][0] != '':

                score3.config(text= '3rd. ' + lista[2][0] + ' turnos - ' + lista[2][1])

            if lista[1][0] != '':

                score2.config(text= '2nd. ' + lista[3][0] + ' turnos - ' + lista[3][1])

            if lista[0][0] != '':

                score1.config(text= '1st. ' + lista[4][0] + ' turnos - ' + lista[4][1])

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
    help_canvas.pack()

    #Boton para cerrar ayuda
    def close_help():
        select_sounds[random.randint(0,2)].play()
        help_canvas.destroy()
        help_canvas.quit
        main()
    close_help_b= tk.Button(help_canvas, text= "Volver", font= ("Sonic 1 HUD Font", 20), bg= "black", fg="white", command= close_help)
    close_help_b.place(x= 50, y= 40)

    #ship1= ImageTk.PhotoImage(Image.open('assets/images/barco3-side.png'))
    #help_canvas.create_image(100, 650, anchor= tk.NW, image=ship1)

    title1= tk.Label(help_canvas, text= "Hola! Bienvenido a Battleship", font= ("Sonic 1 HUD Font", 20), bg= "black", fg= "white")
    title1.place(x= 50, y=110)

    title2= tk.Label(help_canvas, text= "En este juego, tu objetivo sera hundir los tres barcos enemigos", font= ("Sonic 1 HUD Font", 20), bg= "black", fg= "white")
    title2.place(x= 50, y=160)

    title3= tk.Label(help_canvas, text= "Esto sera logrado mediante el uso de dos tableros de 10x10", font= ("Sonic 1 HUD Font", 20), bg= "black", fg= "white")
    title3.place(x= 50, y=210)

    title4= tk.Label(help_canvas, text= "El primero de estos sera el tablero del jugador, en el cual debera colocar 3 barcos ", font= ("Sonic 1 HUD Font", 20), bg= "black", fg= "white")
    title4.place(x= 50, y=260)

    title5= tk.Label(help_canvas, text= "ya sea de manera horizontal o vertical", font= ("Sonic 1 HUD Font", 20), bg= "black", fg= "white")
    title5.place(x= 50, y=310)

    title6= tk.Label(help_canvas, text= "En este mismo tablero es donde se mostraran las coordenadas en donde dispara la computadora", font= ("Sonic 1 HUD Font", 20), bg= "black", fg= "white")
    title6.place(x= 50, y=360)

    title7= tk.Label(help_canvas, text= "El otro tablero, representara el de la computadora y en este no se mostraran los barcos enemigos", font= ("Sonic 1 HUD Font", 20), bg= "black", fg= "white")
    title7.place(x= 50, y=410)

    title8= tk.Label(help_canvas, text= "Solo se mostrara los puntos donde el jugador ya disparo", font= ("Sonic 1 HUD Font", 20), bg= "black", fg= "white")
    title8.place(x= 50, y=460)

    title9= tk.Label(help_canvas, text= "La manera de hundir un barco, es disparando en cada uno de los espacios que ocupa el mismo", font= ("Sonic 1 HUD Font", 20), bg= "black", fg= "white")
    title9.place(x= 50, y=510)

    title0= tk.Label(help_canvas, text= "El primero en hundir los barcos del oponente, sera el ganador!", font= ("Sonic 1 HUD Font", 20), bg= "black", fg= "white")
    title0.place(x= 50, y=560)

    help_canvas.mainloop()

game()