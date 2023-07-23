from tkinter import *
root = Tk()
root.geometry("644x900")
root.title("Calculator by NAZIM")

def click(event):
   global  scvalue   # global is liye mana kyo ki ham ise function ke andar kabhi bhi call kar sake
   text = event.widget.cget("text")

   if text == "=":
      if scvalue.get().isdigit():                  # check value is int or not
         value = int(scvalue.get())
      else:
         try:
             value = eval(screen.get())
         except Exception as e:
            print(e)
            value = "Error"
                                                                 #evel = if  2+5 = 7 ,evel help to give result
      scvalue.set(value)
      screen.update()





   elif text == "C":
      scvalue.set("")
      screen.update()
   else:
      scvalue.set(scvalue.get()  + text)
      screen.update()


                                  #widget - button dega jis par click kiya
                                  #cget - button visit se uska text kaise nikala jaye




scvalue = StringVar()
scvalue.set("")

screen = Entry(root, textvariable= scvalue, font="lucida 40 bold ")
screen.pack(fill=X, ipadx=5, pady=6, padx=6)


f=Frame(root, background="red")

b = Button(f, text="9", padx=3, pady= 3, font="lucida 35 bold")
f.pack()
b.pack(side = LEFT, padx=5, pady=1)
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=3, pady=3, font="lucida 35 bold")
b.pack(side =LEFT, padx=5, pady=1)
b.bind("<Button-1>", click)

b = Button(f, text="7", padx=3, pady=3., font="lucida 35 bold")
b.pack(side = LEFT, padx=5, pady=1)
b.bind("<Button-1>", click)
f.pack()


f=Frame(root, background="red")
b =Button(f, text="6", padx=3, pady= 3, font="lucida 35 bold")

b.pack(side = LEFT, padx=5, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=3, pady=3, font="lucida 35 bold")
b.pack(side = LEFT, padx=5, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="4", padx=3, pady=3., font="lucida 35 bold")
b.pack(side = LEFT, padx=5, pady=10)
b.bind("<Button-1>", click)
f.pack()


f= Frame(root, background="green")

b = Button(f, text="3", padx=3, pady= 3, font="lucida 35 bold")
f.pack()
b.pack(side = LEFT, padx=5, pady=1)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=3, pady=3, font="lucida 35 bold")
b.pack(side = LEFT, padx=5, pady=1)
b.bind("<Button-1>", click)

b =Button(f, text="1", padx=3, pady=3., font="lucida 35 bold")
b.pack(side =LEFT, padx=5, pady=1)
b.bind("<Button-1>", click)
f.pack()

f= Frame(root, background="green")

b = Button(f, text="+", padx=5, pady=10, font="lucida 35 bold")
f.pack()
b.pack(side = LEFT, padx=4, pady=1)
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=5, pady=10, font="lucida 35 bold")
b.pack(side = LEFT, padx=8, pady=1)
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=5, pady=3., font="lucida 35 bold")
b.pack(side = LEFT, padx=5, pady=1)
b.bind("<Button-1>", click)
f.pack()

f= Frame(root, background="purple")

b = Button(f, text="/", padx=3, pady= 3, font="lucida 35 bold")
f.pack()
b.pack(side = LEFT, padx=4, pady=1)
b.bind("<Button-1>", click)

b = Button(f, text="%", padx=3, pady=5, font="lucida 35 bold")
b.pack(side =LEFT, padx=4, pady=1)
b.bind("<Button-1>", click)

b = Button(f, text="C", padx=3, pady=5., font="lucida 35 bold")
b.pack(side = LEFT, padx=4, pady=1)
b.bind("<Button-1>", click)
f.pack()

f= Frame(root, background="purple")

b = Button(f, text="=", padx=3, pady= 3, font="lucida 35 bold")
f.pack()
b.pack(side=LEFT, padx=5, pady=1)
b.bind("<Button-1>", click)

b =Button(f, text="0", padx=3, pady=3, font="lucida 35 bold")
b.pack(side = LEFT, padx=5, pady=1)
b.bind("<Button-1>", click)

b = Button(f, text="00", padx=3, pady=3., font="lucida 35 bold")
b.pack(side = LEFT, padx=3, pady=1)
b.bind("<Button-1>", click)
f.pack()



















root.mainloop()