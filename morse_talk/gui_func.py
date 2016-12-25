"""
Function to produce a G.U.I.
"""
# developed by Arindam Biswas(github handle @aribis369)

from tkinter import Label, Entry, Tk, END, mainloop
import morse_talk as mtalk

dc = ''
cd = ''
y = 'a'


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
        r = ''
        if y[-1] == ' ':
            r = mtalk.decode(y)
            if r != cd:
                cd = r
                e4.delete(0, END)
                e4.insert(0, r)
        e4.after(500, decode)

    font1 = 'Courier', 25, 'bold'
    font2 = 'Courier', 15, 'bold'
    master = Tk()
    master.title("morse_talk")

    Label(master, text="Encode", font=font1).grid(row=3)
    Label(master, text="Decode", font=font1).grid(row=11)
    Label(master, text="Encoded text", font=font1).grid(row=6)
    Label(master, text="Decoded code", font=font1).grid(row=14)

    e1 = Entry(master, font=font2)
    e2 = Entry(master, font=font2)
    e3 = Entry(master, font=font2)
    e4 = Entry(master, font=font2)

    e1.grid(row=3, column=1, ipadx=35)
    e2.grid(row=11, column=1, ipadx=35)
    e3.grid(row=6, column=1, ipadx=35)
    e4.grid(row=14, column=1, ipadx=35)

    encode()
    decode()
    mainloop()


def main():
    import doctest
    doctest.testmod()
    gui()


if __name__ == '__main__':
    main()
