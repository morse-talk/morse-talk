from tkinter import *
import time
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
  global dc
  x=e1.get()
  q=''
  for i in x:
    q+=morse[i]
    q+=' '

  if q!=dc:
      dc=q
      c.config(text=q)

  c.after(500,encode)  
    
  


def decode():
    global cd
    global y
    if e2.get()=='':
        y="a"
    else:    
        y=e2.get()
    z=''
    r=""
    
    if y[-1]==' ':
      for j in y:
          if j!=" ":
              z+=j
          else:
              r+=morse[z]
              z=''
      if r!=cd:
          cd=r
          d.config(text=r)
        
    d.after(500,decode)
        
    
dc=''
cd=''
y="a"
master = Tk()
Label(master, text="Encode",font=('times', 15,'bold'),fg='red').grid(row=2)
Label(master, text="Decode",font=('times', 15,'bold'),fg='blue').grid(row=8)
Label(master, text="Encoded text",font=('times', 15,'bold'),fg='red').grid(row=5)
Label(master, text="Decoded code",font=('times', 15,'bold'),fg='blue').grid(row=11)
c=Label(master, font=('times', 20, 'bold'),fg='green')
d=Label(master, font=('times', 20, 'bold'),fg='green')


e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=2, column=1)
e2.grid(row=8, column=1)
c.grid(row=5,column=1)
d.grid(row=11,column=1)

encode()
decode()

mainloop( )
