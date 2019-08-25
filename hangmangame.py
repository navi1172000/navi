from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("READY TO PLAY THE AMAZING GAME")
window.configure(background='red')
chance=4;
label=Label(window,text="START PLAYING GAME BY CLICKING BUTTONS")
label.grid(column=0,row=0)
def click(alphabet):
    global chance
    answer="LIONELMESSI"
    if alphabet in answer:
        if alphabet=="L":
            btn1["text"]= btn6["text"]=alphabet;
        elif alphabet=="I":
            btn2["text"] =btn11["text"]= alphabet;
        elif alphabet=="O":
            btn3["text"] = alphabet;
        elif alphabet=="N":
            btn4["text"] = alphabet;
        elif alphabet=="E":
            btn5["text"] = btn8["text"] =alphabet;
        elif alphabet == "M":
            btn7["text"] = alphabet;
        elif alphabet == "S":
            btn9["text"] = btn101["text"] =alphabet;

    else:
        chance=chance-1;
        if chance<0:
            messagebox.showinfo("YOU LOOSE THE GAME ","BETTER LUCK NEXT TIME")
            window.destroy()

    if btn1["text"]=="L" and btn2["text"]=="I" and btn3["text"]=="O" and btn4["text"]=="N" and btn5["text"]=="E" \
            and btn6["text"]=="L" and btn7["text"]=="M" and btn8["text"]=="E" and btn9["text"]=="S" and btn101["text"]=="S"and btn11["text"]=="I":
        messagebox.showinfo("CONGURATULATION","YOU WIN THE GAME THANKS FOR PLAYING ")
        window.destroy()

    print(chance)


btn1 =Button(window, text=" ",bg="yellow",fg="black",font=('Helvetica','20'))
btn1.grid(row=0,column=2)
btn2 =Button(window, text=" ",bg="yellow",fg="black",font=('Helvetica','20'))
btn2.grid(row=0,column=3)
btn3 =Button(window, text=" ",bg="yellow",fg="black",font=('Helvetica','20'))
btn3.grid(row=0,column=4)
btn4 =Button(window, text=" ",bg="yellow",fg="black",font=('Helvetica','20'))
btn4.grid(row=0,column=5)
btn5 =Button(window, text=" ",bg="yellow",fg="black",font=('Helvetica','20'))
btn5.grid(row=0,column=6)
btn6 =Button(window, text=" ",bg="yellow",fg="black",font=('Helvetica','20'))
btn6.grid(row=0,column=7)
btn7 =Button(window, text=" ",bg="yellow",fg="black",font=('Helvetica','20'))
btn7.grid(row=1,column=3)
btn8 =Button(window, text=" ",bg="yellow",fg="black",font=('Helvetica','20'))
btn8.grid(row=1,column=4)
btn9 =Button(window, text=" ",bg="yellow",fg="black",font=('Helvetica','20'))
btn9.grid(row=1,column=5)
btn101 =Button(window, text=" ",bg="yellow",fg="black",font=('Helvetica','20'))
btn101.grid(row=1,column=6)
btn11 =Button(window, text=" ",bg="yellow",fg="black",font=('Helvetica','20'))
btn11.grid(row=2,column=5)

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
btn14=Button(window,text="D",bg="violet",fg="black",font=('Helvetica','20'),command=lambda: click("D"))
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
btn26=Button(window,text="U",bg="violet",fg="black",font=('Helvetica','20'),command=lambda: click("U"))
btn26.grid(row=7,column=5)


window.mainloop()
