import tkinter as tk
from PIL import ImageTk, Image
from support import *

window= tk.Tk()
window.geometry("1280x720")
window.resizable(False, False)

def main():
    canvas= tk.Canvas(window, width=1280, height=720, borderwidth=0, highlightthickness=0, bg="black")
    canvas.pack()

    #Titulo
    title= ImageTk.PhotoImage(Image.open('assets/images/logo.png'))
    canvas.create_image(350, 100, anchor= tk.NW, image=title)

    #Boton seleccionar una partida
    def open_p():
        canvas.destroy()
        canvas.quit
        play()
    play_b= tk.Button(canvas, text= " Play ", font= ("Sonic 1 HUD Font", 30), bg= "black", fg="white", command= open_p)
    play_b.place(x= 570, y= 300)

    #Boton para salon de la fama
    def open_hs():
        canvas.destroy()
        canvas.quit
        highscore()
    hs_b= tk.Button(canvas, text= "HighScore", font= ("Sonic 1 HUD Font", 30), bg= "black", fg="white", command= open_hs)
    hs_b.place(x= 534, y= 450)

    #Boton para cerrar el juego
    def quit():
        window.destroy()
        window.quit
    quit_b= tk.Button(canvas, text= " Quit ", font= ("Sonic 1 HUD Font", 30), bg= "black", fg="white", command= quit)
    quit_b.place(x= 570, y= 600)

    #Boton para ayuda
    def open_h():
        canvas.destroy()
        canvas.quit
        help()
    help_b= tk.Button(canvas, text= " ? ", font= ("Sonic 1 HUD Font", 20), bg= "black", fg="white", command= open_h)
    help_b.place(x= 1200, y= 40)

    window.mainloop()


def play():
    p_canvas= tk.Canvas(window, width=1280, height=720, borderwidth=0, highlightthickness=0, bg="black")
    p_canvas.pack()
    
    #Boton para cerrar selccion de partida
    def close_p():
        p_canvas.destroy()
        p_canvas.quit
        main()
    closep_b= tk.Button(p_canvas, text= "Volver", font= ("Sonic 1 HUD Font", 20), bg= "black", fg="white", command= close_p)
    closep_b.place(x= 50, y= 50)

    fileb_1= tk.Button(p_canvas, text= " File 1 ", font= ("Sonic 1 HUD Font", 60), bg= "black", fg="white")
    fileb_1.place(x= 464, y= 100)

    fileb_2= tk.Button(p_canvas, text= " File 2 ", font= ("Sonic 1 HUD Font", 60), bg= "black", fg="white")
    fileb_2.place(x= 464, y= 300)

    fileb_3= tk.Button(p_canvas, text= " File 3 ", font= ("Sonic 1 HUD Font", 60), bg= "black", fg="white")
    fileb_3.place(x= 464, y= 500)

    p_canvas.mainloop()

def highscore():

    hs_canvas= tk.Canvas(window, width=1280, height=720, borderwidth=0, highlightthickness=0, bg="black")
    hs_canvas.pack()
    
    logo = ImageTk.PhotoImage(Image.open('assets/images/logo.png'))
    hs_canvas.create_image(350, 100, anchor = tk.NW, image= logo)

    score1 = tk.Label(text=f"1st.", font=("Sonic 1 HUD Font", 25), fg='#ffffff', bg="#000000")
    score1.place(x= 480, y= 240)

    score2 = tk.Label(text=f"2nd.", font=("Sonic 1 HUD Font", 25), fg='#ffffff', bg="#000000")
    score2.place(x= 480, y= 320)

    score3 = tk.Label(text=f"3rd.", font=("Sonic 1 HUD Font", 25), fg='#ffffff', bg="#000000")
    score3.place(x= 480, y= 400)

    score4 = tk.Label(text=f"4rd.", font=("Sonic 1 HUD Font", 25), fg='#ffffff', bg="#000000")
    score4.place(x= 480, y= 480)

    score5 = tk.Label(text=f"5th.", font=("Sonic 1 HUD Font", 25), fg='#ffffff', bg="#000000")
    score5.place(x= 480, y= 560)

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
        help_canvas.destroy()
        help_canvas.quit
        main()
    close_help_b= tk.Button(help_canvas, text= "Volver", font= ("Sonic 1 HUD Font", 20), bg= "black", fg="white", command= close_help)
    close_help_b.place(x= 50, y= 50)

    help_canvas.mainloop()

main()