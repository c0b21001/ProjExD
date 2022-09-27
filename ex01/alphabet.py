import random
import time

def monndai():
    print(f"対象文字{moji[:hyouji]}")
    print(f"正規文字{seikimoji}")
    for i in range(kaitousu):
        A1 = int(input("欠損数は？A."))
        if A1 == kesson:
            print("正解,抜けている文字を一つずつ表示しなさい")
            for f in range(kesson):
                A2 = input(f"{f+1}文字目は何が抜けている？A.")
                print(kessonmoji[f])
                if A2 == kessonmoji[f]:
                    print("正解")
                else:
                    if kaitousu == 0:
                        print("不正解さようなら")
                    else:
                        print("不正解")
            break
        else:
            if kaitousu == 0:
                print("不正解さようなら")
            else:
                print("不正解")
if  __name__ == "__main__":
    start = time.time()
    moji = [chr(i)for i in range(ord("a"),ord("z")-1)]
    random.shuffle(moji)
    kesson = random.randint(1,10)
    kaitousu = 3
    hyouji=10-kesson
    seikimoji = moji[:10]
    kessonmoji = seikimoji[-kesson:]
    monndai()
    end = time.time()
    print(f"所要時間：{(end-start):.2f}秒")