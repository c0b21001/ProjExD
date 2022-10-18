from email.mime import image
import tkinter as tk



if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷える工科トン")#練習１

    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack()

    tori = tk.PhotoImage(file="ex03/fig/3.png")
    cx, cy = 300, 400
    canv.create_image(cx, cy, image=tori, tag = "tori")
    
    root.mainloop()