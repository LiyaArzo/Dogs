from tkinter import *
from tkinter import messagebox as mb
from tkinter import  ttk
import requests
from PIL import Image,ImageTk
from io import BytesIO


def show_image():
    image_url = get_dog_image()
    if image_url:
        try:
            response = requests.get(image_url, stream=True)
            response.raise_for_status()
            img_data = BytesIO(response.content)
            img = Image.open(img_data)
            img_size = (int(width_spinbox.get()) ,int(heigh_spinbox.get()))
            img.thumbnail(img_size)
            img = ImageTk.PhotoImage(img)
            new_window = Toplevel(window)
            new_window.title('Случайное изображение')
            lb = ttk.Label(new_window,image=img)
            lb.pack()
            lb.image = img
        except Exception as e:
            mb.showerror('Ошибка', f'Возникла ошибка при загрузке изображений - {e}')
    progress.stop()


def get_dog_image():
    try:
        response = requests.get('https://dog.ceo/api/breeds/image/random')
        response.raise_for_status() # если всё ок, статус 200
        data = response.json()
        return data['message']
    except Exception as e:
        mb.showerror('Ошибка', f'Возникла ошибка при запросе к API - {e}')
        return None


def prog():
    progress['value'] = 0 # начальное положение
    progress.start(30) # будет увеличиваться
    window.after(3000, show_image)

window = Tk()
window.title('Картинки с собачками')
window.geometry('360x420')

label = ttk.Label()
label.pack(pady=10)

button = ttk.Button(text='Загрузить', command=prog)
button.pack()

progress = ttk.Progressbar(mode='determinate', length=300)
progress.pack(pady=10)

width_label = ttk.Label(text='Ширина:')
width_label.pack(side='left',padx=(10,0))
width_spinbox = ttk.Spinbox(from_=200, to=500, increment=50, width=5)
width_spinbox.pack(side='left',padx=(0,10))

heigh_label = ttk.Label(text='Высота:')
heigh_label.pack(side='left',padx=(10,0))
heigh_spinbox = ttk.Spinbox(from_=200, to=500, increment=50, width=5)
heigh_spinbox.pack(side='left',padx=(0,10))

window.mainloop()
