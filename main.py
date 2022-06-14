import random
import tkinter as tk
import pygame
from PIL import ImageTk, Image
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

def main():
    canvas= tk.Canvas(window, width=1280, height=720, borderwidth=0, highlightthickness=0, bg="black")
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
    g_canvas.pack()

    boat1_b= tk.Button(g_canvas, image= str(pathlib.Path().resolve()) + "\\assets\images\\barco1.png", font= ("Sonic 1 HUD Font", 30), bg= "black", fg="white")
    boat1_b.place(x= 100, y=100)

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

    ship1= ImageTk.PhotoImage(Image.open('assets/images/barco3-side.png'))
    help_canvas.create_image(100, 650, anchor= tk.NW, image=ship1)

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

main()