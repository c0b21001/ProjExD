import random

def syutudai():
    Q = [1,2,3]
    Q1 = random.choice(Q)
    
    if Q1 == 1:
        print("中島大地の1人目の元カノの名前は？")
        A =input("A.")
        if A == "ゆあ":
            print("正解")
        else:
            print("間違え")
    elif Q1 == 2:
        print("中島大地の2人目の元カノのなまえは？")
        A =input("A.")
        if A == "えゆ":
            print("正解")
        else:
            print("間違え")
    else:
        print("中島大地の三人目の元カノの名前は？")
        A =input("A.")
        if A == "すずね":
            print("正解")
        else:
            print("間違え")

if  __name__ == "__main__":

    syutudai()



