from tkinter import *
from tkinter import messagebox
import random
window = Tk()
window.title("READY TO PLAY THE AMAZING GAME")
window.configure(background='red')
chance=4;
label=Label(window,text="START PLAYING GAME BY CLICKING BUTTONS")
label.grid(column=0,row=0)
a=["WORK","NAVI","SELF"]
answer=random.choice(a)
def click(alphabet):
    global chance
    if alphabet in answer:
        if alphabet=="N":
            btn1["text"]=alphabet;
        elif alphabet=="A":
            btn2["text"]= alphabet;
        elif alphabet=="V":
            btn3["text"] = alphabet;
        elif alphabet=="I":
            btn4["text"] = alphabet;
        elif alphabet=="S":
            btn1["text"] = alphabet;
        elif alphabet == "E":
            btn2["text"] = alphabet
        elif alphabet == "L":
            btn3["text"] = alphabet;
        elif alphabet == "F":
            btn4["text"] = alphabet;
        elif alphabet == "W":
            btn1["text"] = alphabet;
        elif alphabet == "O":
            btn2["text"] = alphabet;
        elif alphabet == "R":
            btn3["text"] = alphabet;
        elif alphabet == "K":
            btn4["text"] = alphabet;


    else:
        chance=chance-1;
        if chance<0:
            messagebox.showinfo("YOU LOOSE THE GAME ","BETTER LUCK NEXT TIME")
            window.destroy()

    if btn1["text"]=="N" and btn2["text"]=="A" and btn3["text"]=="V" and btn4["text"]=="I":
        messagebox.showinfo("CONGURATULATION","YOU WIN THE GAME THANKS FOR PLAYING ")
        window.destroy()
    elif btn1["text"]=="W" and btn2["text"]=="O" and btn3["text"]=="R" and btn4["text"]=="K":
        messagebox.showinfo("CONGURATULATION", "YOU WIN THE GAME THANKS FOR PLAYING ")
        window.destroy()
    elif btn1["text"] == "S" and btn2["text"] == "E" and btn3["text"] == "L" and btn4["text"] == "F":
        messagebox.showinfo("CONGURATULATION", "YOU WIN THE GAME THANKS FOR PLAYING ")
        window.destroy()
    print(chance)


btn1 =Button(window, text=" ",bg="yellow",fg="black",font=('Helvetica','20'))
btn1.grid(row=0,column=2)
btn2 =Button(window, text=" ",bg="yellow",fg="black",font=('Helvetica','20'))
btn2.grid(row=0,column=3)
btn3 =Button(window, text=" ",bg="yellow",fg="black",font=('Helvetica','20'))
btn3.grid(row=0,column=4)
btn4 =Button(window, text=" ",bg="yellow",fg="black",font=('Helvetica','20'))
btn4.grid(row=1,column=3)

btn01=Button(window,text="A",bg="violet",fg="black",font=('Helvetica','20'),command=lambda: click("A"))
btn01.grid(row=3,column=1)
btn02=Button(window,text="W",bg="violet",fg="black",font=('Helvetica','20'),command=lambda: click("W"))
btn02.grid(row=3,column=2)
btn03=Button(window,text="I",bg="violet",fg="black",font=('Helvetica','20'),command=lambda: click("I"))
btn03.grid(row=3,column=3)
btn04=Button(window,text="j",bg="violet",fg="black",font=('Helvetica','20'),command=lambda: click("J"))
btn04.grid(row=3,column=4)
btn05=Button(window,text="N",bg="violet",fg="black",font=('Helvetica','20'),command=lambda: click("N"))
btn05.grid(row=3,column=5)
btn06=Button(window,text="H",bg="violet",fg="black",font=('Helvetica','20'),command=lambda: click("H"))
btn06.grid(row=3,column=6)
btn07=Button(window,text="V",bg="violet",fg="black",font=('Helvetica','20'),command=lambda: click("V"))
btn07.grid(row=3,column=7)
btn08=Button(window,text="T",bg="violet",fg="black",font=('Helvetica','20'),command=lambda: click("T"))
btn08.grid(row=3,column=8)
btn09=Button(window,text="G",bg="violet",fg="black",font=('Helvetica','20'),command=lambda: click("G"))
btn09.grid(row=3,column=9)
btn10=Button(window,text="R",bg="violet",fg="black",font=('Helvetica','20'),command=lambda: click("R"))
btn10.grid(row=4,column=2)
btn111=Button(window,text="E",bg="violet",fg="black",font=('Helvetica','20'),command=lambda: click("E"))
btn111.grid(row=4,column=2)
btn12=Button(window,text="L",bg="violet",fg="black",font=('Helvetica','20'),command=lambda: click("L"))
btn12.grid(row=4,column=3)
btn13=Button(window,text="B",bg="violet",fg="black",font=('Helvetica','20'),command=lambda: click("B"))
btn13.grid(row=4,column=4)
btn14=Button(window,text="R",bg="violet",fg="black",font=('Helvetica','20'),command=lambda: click("R"))
btn14.grid(row=4,column=5)
btn15=Button(window,text="Z",bg="violet",fg="black",font=('Helvetica','20'),command=lambda: click("Z"))
btn15.grid(row=4,column=6)
btn16=Button(window,text="M",bg="violet",fg="black",font=('Helvetica','20'),command=lambda: click("M"))
btn16.grid(row=4,column=7)
btn17=Button(window,text="K",bg="violet",fg="black",font=('Helvetica','20'),command=lambda: click("K"))
btn17.grid(row=4,column=8)
btn18=Button(window,text="S",bg="violet",fg="black",font=('Helvetica','20'),command=lambda: click("S"))
btn18.grid(row=5,column=3)
btn19=Button(window,text="Q",bg="violet",fg="black",font=('Helvetica','20'),command=lambda: click("Q"))
btn19.grid(row=5,column=4)
btn20=Button(window,text="P",bg="violet",fg="black",font=('Helvetica','20'),command=lambda: click("P"))
btn20.grid(row=5,column=5)
btn21=Button(window,text="X",bg="violet",fg="black",font=('Helvetica','20'),command=lambda: click("X"))
btn21.grid(row=5,column=6)
btn22=Button(window,text="F",bg="violet",fg="black",font=('Helvetica','20'),command=lambda: click("F"))
btn22.grid(row=5,column=7)
btn23=Button(window,text="Y",bg="violet",fg="black",font=('Helvetica','20'),command=lambda: click("Y"))
btn23.grid(row=6,column=4)
btn24=Button(window,text="G",bg="violet",fg="black",font=('Helvetica','20'),command=lambda: click("G"))
btn24.grid(row=6,column=5)
btn25=Button(window,text="O",bg="violet",fg="black",font=('Helvetica','20'),command=lambda: click("O"))
btn25.grid(row=6,column=6)
btn26=Button(window,text="C",bg="violet",fg="black",font=('Helvetica','20'),command=lambda: click("C"))
btn26.grid(row=7,column=5)


window.mainloop()
