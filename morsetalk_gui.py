from tkinter import *
morse = {
"A" : ".-",
"B" : "-...", 
"C" : "-.-.", 
"D" : "-..", 
"E" : ".", 
"F" : "..-.", 
"G" : "--.", 
"H" : "....", 
"I" : "..", 
"J" : ".---", 
"K" : "-.-", 
"L" : ".-..", 
"M" : "--", 
"N" : "-.", 
"O" : "---", 
"P" : ".--.", 
"Q" : "--.-", 
"R" : ".-.", 
"S" : "...", 
"T" : "-", 
"U" : "..-", 
"V" : "...-", 
"W" : ".--", 
"X" : "-..-", 
"Y" : "-.--", 
"Z" : "--..",
"a" : ".-", 
"b" : "-...", 
"c" : "-.-.", 
"d" : "-..", 
"e" : ".", 
"f" : "..-.", 
"g" : "--.", 
"h" : "....", 
"i" : "..", 
"j" : ".---", 
"k" : "-.-", 
"l" : ".-..", 
"m" : "--", 
"n" : "-.", 
"o" : "---", 
"p" : ".--.", 
"q" : "--.-", 
"r" : ".-.", 
"s" : "...", 
"t" : "-", 
"u" : "..-", 
"v" : "...-", 
"w" : ".--", 
"x" : "-..-", 
"y" : "-.--", 
"z" : "--..", 
"0" : "-----", 
"1" : ".----", 
"2" : "..---", 
"3" : "...--", 
"4" : "....-", 
"5" : ".....", 
"6" : "-....", 
"7" : "--...", 
"8" : "---..", 
"9" : "----.", 
"." : ".-.-.-", 
"," : "--..--",
 ".-":"A",
 "-...":"B", 
 "-.-.":"C", 
 "-..":"D", 
 ".":"E", 
 "..-.":"F", 
 "--.":"G", 
 "....":"H", 
 "..":"I", 
 ".---":"J", 
 "-.-":"K", 
 ".-..":"L", 
 "--":"M", 
 "-.":"N", 
 "---":"O", 
 ".--.":"P", 
 "--.-":"Q", 
 ".-.":"R", 
 "...":"S", 
 "-":"T", 
 "..-":"U", 
 "...-":"V", 
 ".--":"W", 
 "-..-":"X", 
 "-.--":"Y", 
 "--..":"Z", 
 "-----":"0", 
 ".----":"1", 
 "..---":"2", 
 "...--":"3", 
 "....-":"4", 
 ".....":"5", 
 "-....":"6", 
 "--...":"7", 
 "---..":"8", 
 "----.":"9",
 ".-.-.-":".",
 "--..--":",",
" ":"  ",
"":" "
}

def encode():
  x=e1.get()
  print("the code is :"+'\n')
  q=''
  for i in x:
    print(morse[i],end=" ")
    q+=morse[i]
    q+=' '
    
  print('\n')
  var = messagebox.showinfo("ENCODED TEXT" ,"the code is :"+'\n'+q)


def decode():
    y=e2.get()
    y+=' '
    print("the text is :"+'\n')
    z=''
    r=""
    for j in y:
        if j!=" ":
            z+=j
        else:
            print(morse[z],end="")
            r+=morse[z]
            z=''
    print('\n')
    var = messagebox.showinfo("DECODED TEXT" ,"the text is :"+'\n'+r)
    

master = Tk()
Label(master, text="Encode").grid(row=2)
Label(master, text="Decode").grid(row=5)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=2, column=1)
e2.grid(row=5, column=1)

Button(master, text='                 Quit                 ', command=master.destroy).grid(row=9, column=1, sticky=W, pady=5)
Button(master, text='         Encode         ', command=encode).grid(row=7, column=0, sticky=W, pady=4)
Button(master, text='         Decode         ', command=decode).grid(row=7, column=2, sticky=W, pady=4)

mainloop( )
