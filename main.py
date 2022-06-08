from email.mime import image
import tkinter as tk
from PIL import ImageTk, Image

window= tk.Tk()
window.geometry("1280x720")

def main():
    canvas= tk.Canvas(window, width=1280, height=720, borderwidth=0, highlightthickness=0, bg="black")
    canvas.pack()

    #Titulo
    title= ImageTk.PhotoImage(Image.open('assets/images/logo.png'))
    canvas.create_image(100, 100, anchor= tk.NW, image= title)

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

main()

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

def highscore():
    hs_canvas= tk.Canvas(window, width=1280, height=720, borderwidth=0, highlightthickness=0, bg="black")
    hs_canvas.pack()
    
    #Boton para cerrar salon de la fama
    def close_hs():
        hs_canvas.destroy()
        hs_canvas.quit
        main()
    closehs_b= tk.Button(hs_canvas, text= "Volver", font= ("Sonic 1 HUD Font", 20), bg= "black", fg="white", command= close_hs)
    closehs_b.place(x=50, y=50)

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

window.mainloop()