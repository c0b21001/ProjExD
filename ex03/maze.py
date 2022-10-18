import tkinter as tk
import maze_maker as mm #練習8


def key_down(event):#練習5
    global key
    key = event.keysym

def key_up(event):#練習6
    global key
    key = ""

def main_proc():
    global cx, cy
    if key == "Up":
        cy -= 20
    if key == "Down":
        cy += 20
    if key == "Right":
        cx += 20
    if key == "Left":
        cx -= 20
    canv.coords("tori",cx, cy)
    root.after(100,main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷える工科トン")#練習1

    #練習2
    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack()

    #練習3
    tori = tk.PhotoImage(file="fig/3.png")
    cx, cy = 300, 400
    canv.create_image(cx, cy, image=tori, tag = "tori")

     #練習4
    key = "" #現在押されているキーを表す 
    #練習5,6
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)


    #練習7
    main_proc()
    #練習9
    maze_lst =  mm.make_maze(15, 9)
    print(maze_lst)#１：壁0：床
    mm.show_maze(canv, maze_lst)
    root.mainloop()