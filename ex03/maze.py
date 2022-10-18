
import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm #練習8

def key_down(event):#練習5
    global key
    key = event.keysym

def key_up(event):#練習6
    global key
    key = ""

def dame():
    global cx,cy
    if maze_lst[my][mx] == 1:
        tkm.showinfo("失敗", "✕とかべには入るな")
        root.mainloop()

def main_proc():
    global tmr,jid
    tmr = tmr+1 

    global mx,my
    global cx, cy
    global batu

    
    if mx ==13 and my ==7:                      #ゴールしたら
        tkm.showinfo("goal", f"所要時間：{tmr/10}秒\nゴールしました。")
        

        root.mainloop()


    if key == "Up":
        maze_lst[my][mx] = 1
        my -= 1
        dame()
        canv.create_image(cx, cy, image=batu, tag = "batu")
    if key == "Down":
        maze_lst[my][mx] = 1
        my += 1
        dame()
        canv.create_image(cx, cy, image=batu, tag = "batu")
    if key == "Right":
        maze_lst[my][mx] = 1
        mx += 1
        dame()
        canv.create_image(cx, cy, image=batu, tag = "batu")
    if key == "Left":
        maze_lst[my][mx] = 1
        mx -= 1
        dame()
        canv.create_image(cx, cy, image=batu, tag = "batu")
    if maze_lst[my][mx] == 0:          #床なら
        cx, cy = mx*100+50, my*100+50
    else:                              #壁なら
        if key == "Up":
            my += 1
        if key == "Down":
            my -= 1
        if key == "Right":
            mx -= 1
        if key == "Left":
            mx += 1
    
    canv.coords("tori",cx, cy)
    root.after(100,main_proc)


if __name__ == "__main__":
    tmr = 0


    root = tk.Tk()
    root.title("迷える工科トン")#練習1

    #練習2
    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack()

    #練習9,10
    maze_lst =  mm.make_maze(15, 9)
    print(maze_lst)#１：壁0：床
    mm.show_maze(canv, maze_lst)

    #スタート
    start1 = tk.PhotoImage(file="fig/start.png")
    sx, sy = 1, 1
    ssx, ssy = sx*100+50, sy*100+50
    canv.create_image(ssx, ssy, image=start1, tag = "start")

    #ゴール
    goal = tk.PhotoImage(file="fig/goal.png")
    gx, gy = 13, 7
    ggx, ggy = gx*100+50, gy*100+50
    canv.create_image(ggx, ggy, image=goal, tag = "goal")

    #通った後
    batu = tk.PhotoImage(file="fig/batu.png")

    #練習3
    tori = tk.PhotoImage(file="fig/3.png")
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    canv.create_image(cx, cy, image=tori, tag = "tori")

     #練習4
    key = "" #現在押されているキーを表す 
    #練習5,6
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)

    #練習7
    main_proc()

    root.mainloop()