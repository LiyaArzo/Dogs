from tkinter import *
from tkinter import  ttk
import requests
from PIL import Image,ImageTk
from io import BytesIO

def show_image():
    pass

window = Tk()
window.title('Картинки с собачками')
window.geometry('360x420')

label = Label()
label.pack(pady=10)

button = Button(text='Загрузить', command=show_image)
button.pack()

window.mainloop()
