import tkinter as tk

def main():

    window = tk.Tk()
    window.geometry("1280x720")

    help_canvas = tk.Canvas(window,  width=1280, height=720, borderwidth=0, highlightthickness=0, bg="white")
    help_canvas.place(x=0, y=0)
    canvas = tk.Canvas(window,  width=1280, height=720, borderwidth=0, highlightthickness=0, bg="#000000")
    canvas.place(x=0, y=0)
    
    def quit():
        window.destroy()
        window.quit

    quit_button= tk.Button(canvas, text= "Quit", command= quit)
    quit_button.place(x= 100, y= 100)
    

   


    

    window.mainloop()

main()