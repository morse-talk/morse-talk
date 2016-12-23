from tkinter import *
import time
import morse_talk as mtalk
import sys

dc = ''
cd = ''


def gui():
    def encode():
        global dc
        x = e1.get()
        q = mtalk.encode(x)
        if q != dc:
            dc = q
            e3.delete(0, END)
            e3.insert(0, q)
        e3.after(500, encode)

    def decode():
        global cd
        global y
        if e2.get() == '':
            y = "a"
        else:
            y = e2.get()
        z = ''
        r = ""
        if y[-1] == ' ':
            r = mtalk.decode(y)
            if r != cd:
                cd = r
                e4.delete(0, END)
                e4.insert(0, r)
        e4.after(500, decode)

    dc = ''
    cd = ''
    y = "a"
    v='Courier', 20, 'bold'
    u='Courier', 25, 'bold'
    master = Tk()
    master.title("morse_talk")

    Label(master, text="Encode", font=u).grid(row=3)
    Label(master, text="Decode", font=u).grid(row=11)
    Label(master, text="Encoded text", font=u).grid(row=6)
    Label(master, text="Decoded code", font=u).grid(row=14)

    e1 = Entry(master, font=v)
    e2 = Entry(master, font=v)
    e3 = Entry(master, font=v)
    e4 = Entry(master, font=v)

    e1.grid(row=3, column=1)
    e2.grid(row=11, column=1)
    e3.grid(row=6, column=1)
    e4.grid(row=14, column=1)

    encode()
    decode()
    mainloop()


def main():
    import doctest
    doctest.testmod()
    gui()


if __name__ == '__main__':
    main()
