import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
root=tk.Tk()
root.geometry("1920x1080")
image=Image.open('C:\\Users\\Shreya\\OneDrive\\Desktop\\Project\\1.ppm')
img=image.resize((1920, 1080))
bgimg=ImageTk.PhotoImage(img)
limg=Label(root,image=bgimg).place(x=0,y=0)
root.title("QR code generator")
label=tk.Label(root,text="QR Code Generator",bg='SteelBlue3',fg='azure',font=('Arial',80))
label.pack(padx=20, pady=20)
image1=Image.open('C:\\Users\\Shreya\\OneDrive\\Desktop\\Project\\QRimage.ppm')
img1=image1.resize((270,270))
bgimg1=ImageTk.PhotoImage(img1)
limg1=Label(root,image=bgimg1).place(x=1400,y=750)
label1=Label(root,text='Enter the url: ',bg='SteelBlue3',fg='azure',font=('Arial',40))
label1.place(x=400,y=300)
text=Entry(root,font=('Arial',40),bg='SteelBlue3',fg='azure')
text.place(x=800,y=300)
label2=Label(root,text='Enter the location to save : ',bg='SteelBlue3',fg='azure',font=('Arial',40))
label2.place(x=400,y=400)
text=Entry(root,font=('Arial',40),bg='SteelBlue3',fg='azure')
text.place(x=1100,y=400)
label3=Label(root,text='Enter the name of the code: ',bg='SteelBlue3',fg='azure',font=('Arial',40))
label3.place(x=400,y=500)
text=Entry(root,font=('Arial',40),bg='SteelBlue3',fg='azure')
text.place(x=1100,y=500)
label3=Label(root,text='Enter the size of the code: ',bg='SteelBlue3',fg='azure',font=('Arial',40))
label3.place(x=400,y=600)
text=Entry(root,font=('Arial',40),bg='SteelBlue3',fg='azure')
text.place(x=1100,y=600)
button=Button(root,text='Generate code',bg='SteelBlue3',fg='azure',activeforeground='red',font=('Arial',40))
button.place(x=900,y=800)
root.mainloop()

def mainloop(self):
    
    self.img = ImageTk.PhotoImage(Image.open("ball.png"))     
    self.canvas.create_image(20,20, anchor=NW, image=self.img)    
    self.canvas.image = self.img
