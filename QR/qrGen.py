import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import qrcode

def generateQR():
	qrgen = qrcode.QRCode(version = text4.get(),
		box_size = 12,
		border = 6)
	qrgen.add_data(text1.get()) 
	qrgen.make(fit = True)
	img = qrgen.make_image(fill_color = 'blue', back_color = 'white')	
	fileDirec=text2.get()+'/'+text3.get() 
	img.save(f'{fileDirec}.png') 
	img.show()
	messagebox.showinfo("QR-Code Generator","QR Code is saved successfully!")

#create a root
root=tk.Tk()
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
window_width=int(screen_width)
window_height=int(screen_height)
root.geometry(f"{window_width}x{window_height}")
image=Image.open('1.ppm')
img=image.resize((1920, 1080))
bgimg=ImageTk.PhotoImage(img)
limg=Label(root,image=bgimg).place(x=0,y=0)
root.title("QR code generator")
label=tk.Label(root,text="QR Code Generator",bg='SteelBlue3',fg='azure',font=('Arial',80))
label.pack(padx=20, pady=20)
image1=Image.open('QRimage.ppm')
img1=image1.resize((270,270))
bgimg1=ImageTk.PhotoImage(img1)
limg1=Label(root,image=bgimg1).place(x=1400,y=750)
label1=Label(root,text='Enter the text: ',bg='SteelBlue3',fg='azure',font=('Arial',40))
label1.place(x=400,y=300)
text1=Entry(root,font=('Arial',40),bg='SteelBlue3',fg='azure')
text1.place(x=800,y=300)
label2=Label(root,text='Enter the location to save: ',bg='SteelBlue3',fg='azure',font=('Arial',40))
label2.place(x=400,y=400)
text2=Entry(root,font=('Arial',40),bg='SteelBlue3',fg='azure')
text2.place(x=1100,y=400)
label3=Label(root,text='Enter the name of the code: ',bg='SteelBlue3',fg='azure',font=('Arial',40))
label3.place(x=400,y=500)
text3=Entry(root,font=('Arial',40),bg='SteelBlue3',fg='azure')
text3.place(x=1100,y=500)
label4=Label(root,text='Enter the size of the code: ',bg='SteelBlue3',fg='azure',font=('Arial',40))
label4.place(x=400,y=600)
text4=Entry(root,font=('Arial',40),bg='SteelBlue3',fg='azure')
text4.place(x=1100,y=600)
button=Button(root,text='Generate code',bg='SteelBlue3',fg='azure',activeforeground='red',font=('Arial',40),command=generateQR)
button.place(x=700,y=800)
root.mainloop()



