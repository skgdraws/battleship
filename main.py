import tkinter as tk
from tkinter.font import Font

window= tk.Tk()
window.geometry("1280x720")

def main():
    canvas= tk.Canvas(window, width=1280, height=720, borderwidth=0, highlightthickness=0, bg="black")
    canvas.pack()

    #Boton para salon de la fama
    def open_hs():
        canvas.destroy()
        canvas.quit
        highscore()
    hs_b= tk.Button(canvas, text= "HighScore", font= "Sonic 1 HUD Font", bg= "black", fg="white", command= open_hs)
    hs_b.place(x= 300, y= 300)

    #Boton para ayuda
    def open_h():
        canvas.destroy()
        canvas.quit
        help()
    help_b= tk.Button(canvas, text= "?", bg= "black", fg="white", command= open_h)
    help_b.place(x= 200, y= 200)

    #Boton para cerrar el juego
    def quit():
        window.destroy()
        window.quit
    quit_b= tk.Button(canvas, text= "Quit", bg= "black", fg="white", command= quit)
    quit_b.place(x= 100, y= 100)

main()

def highscore():
    hs_canvas= tk.Canvas(window, width=1280, height=720, borderwidth=0, highlightthickness=0, bg="black")
    hs_canvas.pack()
    
    #Boton para cerrar salon de la fama
    def close_hs():
        hs_canvas.destroy()
        hs_canvas.quit
        main()
    closehs_b= tk.Button(hs_canvas, text= "Volver", bg= "black", fg="white", command= close_hs)
    closehs_b.place(x=100, y=100)

def help():
    help_canvas= tk.Canvas(window, width=1280, height=720, borderwidth=0, highlightthickness=0, bg="black")
    help_canvas.pack()

    #Boton para cerrar ayuda
    def close_help():
        help_canvas.destroy()
        help_canvas.quit
        main()
    close_help_b= tk.Button(help_canvas, text= "Volver", bg= "black", fg="white", command= close_help)
    close_help_b.place(x= 100, y= 100)

window.mainloop()