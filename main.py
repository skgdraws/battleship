import tkinter as tk

def main():

    window = tk.Tk()
    window.geometry("1280x720")

    canvas = tk.Canvas(window,  width=1280, height=720, borderwidth=0, highlightthickness=0, bg="#000000")
    canvas.place(x=0, y=0)

    window.mainloop()