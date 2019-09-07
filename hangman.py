from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

import random

window = Tk()
window.geometry("1800x1700")
window.title("READY TO PLAY THE AMAZING GAME")
window.configure(background='grey')
chance = 4;
image_paths=[r'C:\\Users\\naveen\\Desktop\\img7.jpg',r'C:\\Users\\naveen\\Desktop\\img4.jpg',r'C:\\Users\\naveen\\Desktop\\img3.jpg',r'C:\\Users\\naveen\\Desktop\\img2.jpg',r'C:\\Users\\naveen\\Desktop\\img1.jpg']
img=Image.open(image_paths[chance])
img=img.resize((200,200),Image.ANTIALIAS)
img=ImageTk.PhotoImage(img)
panel=Label(window,image=img)
panel.grid(row=0,column=0)
a = ["WORK", "NAVI", "SELF"]
answer = random.choice(a)
def click(alphabet):
    global chance
    btn["text"] = chance;
    if alphabet in answer:
        if alphabet == "N":
            btn1["text"] = alphabet;

            img = Image.open(image_paths[4])
            img = img.resize((200, 200), Image.ANTIALIAS)
            imgnew = ImageTk.PhotoImage(img)
            panel.configure(image=imgnew)
            panel.image = imgnew
        elif alphabet == "A":
            btn2["text"] = alphabet;

            img = Image.open(image_paths[4])
            img = img.resize((200, 200), Image.ANTIALIAS)
            imgnew = ImageTk.PhotoImage(img)
            panel.configure(image=imgnew)
            panel.image = imgnew
        elif alphabet == "V":

            img = Image.open(image_paths[4])
            img = img.resize((200, 200), Image.ANTIALIAS)
            imgnew = ImageTk.PhotoImage(img)
            panel.configure(image=imgnew)
            panel.image = imgnew
            btn3["text"] = alphabet;
        elif alphabet == "I":

            img = Image.open(image_paths[4])
            img = img.resize((200, 200), Image.ANTIALIAS)
            imgnew = ImageTk.PhotoImage(img)
            panel.configure(image=imgnew)
            panel.image = imgnew
            btn4["text"] = alphabet;
        elif alphabet == "S":

            img = Image.open(image_paths[4])
            img = img.resize((200, 200), Image.ANTIALIAS)
            imgnew = ImageTk.PhotoImage(img)
            panel.configure(image=imgnew)
            panel.image = imgnew
            btn1["text"] = alphabet;
        elif alphabet == "E":

            img = Image.open(image_paths[4])
            img = img.resize((200, 200), Image.ANTIALIAS)
            imgnew = ImageTk.PhotoImage(img)
            panel.configure(image=imgnew)
            panel.image = imgnew
            btn2["text"] = alphabet
        elif alphabet == "L":

            img = Image.open(image_paths[4])
            img = img.resize((200, 200), Image.ANTIALIAS)
            imgnew = ImageTk.PhotoImage(img)
            panel.configure(image=imgnew)
            panel.image = imgnew
            btn3["text"] = alphabet;
        elif alphabet == "F":

            img = Image.open(image_paths[4])
            img = img.resize((200, 200), Image.ANTIALIAS)
            imgnew = ImageTk.PhotoImage(img)
            panel.configure(image=imgnew)
            panel.image = imgnew
            btn4["text"] = alphabet;
        elif alphabet == "W":

            img = Image.open(image_paths[4])
            img = img.resize((200, 200), Image.ANTIALIAS)
            imgnew = ImageTk.PhotoImage(img)
            panel.configure(image=imgnew)
            panel.image = imgnew
            btn1["text"] = alphabet;
        elif alphabet == "O":

            img = Image.open(image_paths[4])
            img = img.resize((200, 200), Image.ANTIALIAS)
            imgnew = ImageTk.PhotoImage(img)
            panel.configure(image=imgnew)
            panel.image = imgnew
            btn2["text"] = alphabet;
        elif alphabet == "R":

            img = Image.open(image_paths[4])
            img = img.resize((200, 200), Image.ANTIALIAS)
            imgnew = ImageTk.PhotoImage(img)
            panel.configure(image=imgnew)
            panel.image = imgnew
            btn3["text"] = alphabet;
        elif alphabet == "K":

            img = Image.open(image_paths[4])
            img = img.resize((200, 200), Image.ANTIALIAS)
            imgnew = ImageTk.PhotoImage(img)
            panel.configure(image=imgnew)
            panel.image = imgnew
            btn4["text"] = alphabet;


    else:
        txt = "chance remaining :" + str(chance);
        label1.configure(text=txt)
        img = Image.open(image_paths[chance])
        img = img.resize((200, 200), Image.ANTIALIAS)
        imgnew = ImageTk.PhotoImage(img)
        panel.configure(image=imgnew)
        panel.image=imgnew
        chance = chance - 1;
        if chance < 0:
            messagebox.showinfo("YOU LOOSE THE GAME ", "BETTER LUCK NEXT TIME")
            window.destroy()

    if btn1["text"] == "N" and btn2["text"] == "A" and btn3["text"] == "V" and btn4["text"] == "I":

        img = Image.open(image_paths[4])
        img = img.resize((200, 200), Image.ANTIALIAS)
        imgnew = ImageTk.PhotoImage(img)
        panel.configure(image=imgnew)
        panel.image = imgnew
        messagebox.showinfo("CONGRATULATION", "YOU WON THE GAME THANKS FOR PLAYING ")
        window.destroy()
    elif btn1["text"] == "W" and btn2["text"] == "O" and btn3["text"] == "R" and btn4["text"] == "K":

        img = Image.open(image_paths[4])
        img = img.resize((200, 200), Image.ANTIALIAS)
        imgnew = ImageTk.PhotoImage(img)
        panel.configure(image=imgnew)
        panel.image = imgnew
        messagebox.showinfo("CONGRATULATION", "YOU WIN THE GAME THANKS FOR PLAYING ")
        window.destroy()
    elif btn1["text"] == "S" and btn2["text"] == "E" and btn3["text"] == "L" and btn4["text"] == "F":

        img = Image.open(image_paths[4])
        img = img.resize((200, 200), Image.ANTIALIAS)
        imgnew = ImageTk.PhotoImage(img)
        panel.configure(image=imgnew)
        panel.image = imgnew
        messagebox.showinfo("CONGRATULATION", "YOU WIN THE GAME THANKS FOR PLAYING ")
        window.destroy()
    print(chance)


btn1 = Button(window, text=" ", bg="brown", fg="black", width=4, height=2, borderwidth=8, font=('Helvetica', '20'))
btn1.grid(row=0, column=4)
btn2 = Button(window, text=" ", bg="brown", fg="black", width=4, height=2, borderwidth=8, font=('Helvetica', '20'))
btn2.grid(row=0, column=5)
btn3 = Button(window, text=" ", bg="brown", fg="black", width=4, height=2, borderwidth=8, font=('Helvetica', '20'))
btn3.grid(row=0, column=6)
btn4 = Button(window, text=" ", bg="brown", fg="black", width=4, height=2, borderwidth=8, font=('Helvetica', '20'))
btn4.grid(row=0, column=7)
btn = Button(window, text=" ", bg="brown", fg="black", width=4, height=2, borderwidth=8, font=('Helvetica', '20'))
btn.grid(row=5, column=10)
btn01 = Button(window, text="A", bg="brown", fg="black", width=4, height=2, borderwidth=8, font=('Helvetica', '20'),
               command=lambda: click("A"))
btn01.grid(row=3, column=1)
btn02 = Button(window, text="W", bg="brown", fg="black", font=('Helvetica', '20'), width=4, height=2, borderwidth=8,
               command=lambda: click("W"))
btn02.grid(row=3, column=2)
btn03 = Button(window, text="I", bg="brown", fg="black", font=('Helvetica', '20'), width=4, height=2, borderwidth=8,
               command=lambda: click("I"))
btn03.grid(row=3, column=3)
btn04 = Button(window, text="j", bg="brown", fg="black", width=4, height=2, borderwidth=8, font=('Helvetica', '20'),
               command=lambda: click("J"))
btn04.grid(row=3, column=4)
btn05 = Button(window, text="N", bg="brown", fg="black", font=('Helvetica', '20'), width=4, height=2, borderwidth=8,
               command=lambda: click("N"))
btn05.grid(row=3, column=5)
btn06 = Button(window, text="H", bg="brown", fg="black", font=('Helvetica', '20'), width=4, height=2, borderwidth=8,
               command=lambda: click("H"))
btn06.grid(row=3, column=6)
btn07 = Button(window, text="V", bg="brown", fg="black", font=('Helvetica', '20'), width=4, height=2, borderwidth=8,
               command=lambda: click("V"))
btn07.grid(row=3, column=7)
btn08 = Button(window, text="T", bg="brown", fg="black", font=('Helvetica', '20'), width=4, height=2, borderwidth=8,
               command=lambda: click("T"))
btn08.grid(row=3, column=8)
btn09 = Button(window, text="G", bg="brown", fg="black", font=('Helvetica', '20'), width=4, height=2, borderwidth=8,
               command=lambda: click("G"))
btn09.grid(row=3, column=9)
btn10 = Button(window, text="R", bg="brown", fg="black", font=('Helvetica', '20'), width=4, height=2, borderwidth=8,
               command=lambda: click("R"))
btn10.grid(row=4, column=2)
btn111 = Button(window, text="E", bg="brown", fg="black", font=('Helvetica', '20'), width=4, height=2, borderwidth=8,
                command=lambda: click("E"))
btn111.grid(row=4, column=2)
btn12 = Button(window, text="L", bg="brown", fg="black", font=('Helvetica', '20'), width=4, height=2, borderwidth=8,
               command=lambda: click("L"))
btn12.grid(row=4, column=3)
btn13 = Button(window, text="B", bg="brown", fg="black", font=('Helvetica', '20'), width=4, height=2, borderwidth=8,
               command=lambda: click("B"))
btn13.grid(row=4, column=4)
btn14 = Button(window, text="R", bg="brown", fg="black", font=('Helvetica', '20'), width=4, height=2, borderwidth=8,
               command=lambda: click("R"))
btn14.grid(row=4, column=5)
btn15 = Button(window, text="Z", bg="brown", fg="black", font=('Helvetica', '20'), width=4, height=2, borderwidth=8,
               command=lambda: click("Z"))
btn15.grid(row=4, column=6)
btn16 = Button(window, text="M", bg="brown", fg="black", font=('Helvetica', '20'), width=4, height=2, borderwidth=8,
               command=lambda: click("M"))
btn16.grid(row=4, column=7)
btn17 = Button(window, text="K", bg="brown", fg="black", font=('Helvetica', '20'), width=4, height=2, borderwidth=8,
               command=lambda: click("K"))
btn17.grid(row=4, column=8)
btn18 = Button(window, text="S", bg="brown", fg="black", font=('Helvetica', '20'), width=4, height=2, borderwidth=8,
               command=lambda: click("S"))
btn18.grid(row=5, column=3)
btn19 = Button(window, text="Q", bg="brown", fg="black", font=('Helvetica', '20'), width=4, height=2, borderwidth=8,
               command=lambda: click("Q"))
btn19.grid(row=5, column=4)
btn20 = Button(window, text="P", bg="brown", fg="black", font=('Helvetica', '20'), width=4, height=2, borderwidth=8,
               command=lambda: click("P"))
btn20.grid(row=5, column=5)
btn21 = Button(window, text="X", bg="brown", fg="black", font=('Helvetica', '20'), width=4, height=2, borderwidth=8,
               command=lambda: click("X"))
btn21.grid(row=5, column=6)
btn22 = Button(window, text="F", bg="brown", fg="black", font=('Helvetica', '20'), width=4, height=2, borderwidth=8,
               command=lambda: click("F"))
btn22.grid(row=5, column=7)
btn23 = Button(window, text="Y", bg="brown", fg="black", font=('Helvetica', '20'), width=4, height=2, borderwidth=8,
               command=lambda: click("Y"))
btn23.grid(row=6, column=4)
btn24 = Button(window, text="G", bg="brown", fg="black", font=('Helvetica', '20'), width=4, height=2, borderwidth=8,
               command=lambda: click("G"))
btn24.grid(row=6, column=5)
btn25 = Button(window, text="O", bg="brown", fg="black", font=('Helvetica', '20'), width=4, height=2, borderwidth=8,
               command=lambda: click("O"))
btn25.grid(row=6, column=6)
btn26 = Button(window, text="C", bg="brown", fg="black", font=('Helvetica', '20'), width=4, height=2, borderwidth=8,
               command=lambda: click("C"))
btn26.grid(row=7, column=5)

label1 = Label(window, text="total chances are : 5", fg="blue", bg="yellow", font="verdana 10 bold", )
label1.grid(row=6, column=10)
window.mainloop()
