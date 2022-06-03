import tkinter as tk

def main():

    window = tk.Tk()
    window.geometry("1280x720")

    help_canvas = tk.Canvas(window,  width=1280, height=720, borderwidth=0, highlightthickness=0, bg="white")
    help_canvas.place(x=0, y=0)
    canvas = tk.Canvas(window,  width=1280, height=720, borderwidth=0, highlightthickness=0, bg="#000000")
    canvas.place(x=0, y=0)
    

    title = tk.Label(canvas, text= "Battleship", font= "Sonic-1-HUD-Font", bg= "black", fg= "white")
    title.place(x= 100, y= 100)

   


    

    window.mainloop()

main()