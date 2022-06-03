import tkinter as tk

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
    hs_b= tk.Button(canvas, text= "HighScore", bg= "black", fg="white", command= open_hs)
    hs_b.place(x= 300, y= 300)

    #Boton para ayuda
    def open_h():
        canvas.destroy()
        canvas.quit
        help()
    help_b= tk.Button(canvas, text= "Ayuda", bg= "black", fg="white", command= open_h)
    help_b.place(x= 200, y= 200)

    #Boton para cerrar el juego
    def quit():
        window.destroy()
        window.quit
    quit_b= tk.Button(canvas, text= "QUIT", bg= "black", fg="white", command= quit)
    quit_b.place(x= 100, y= 100)

main()

def highscore():
    hs_canvas= tk.Canvas(window, width=1280, height=720, borderwidth=0, highlightthickness=0, bg="red")
    hs_canvas.pack()

def help():
    help_canvas= tk.Canvas(window, width=1280, height=720, borderwidth=0, highlightthickness=0, bg="blue")
    help_canvas.pack()

window.mainloop()