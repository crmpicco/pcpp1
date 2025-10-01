from tkinter import *  
  
top = Tk()  
  
top.geometry("400x250")  
  
name = Label(top, text = "Name").place(x = 30,y = 50)  
    
  
e1 = Entry(top,fg="white", bg="black", cursor="dot").place(x = 80, y = 50)  
  
  
top.mainloop()  
