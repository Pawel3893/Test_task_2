import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

from PIL import Image
import os


ws = tk.Tk()
ws.title("Конвертер")
ws.geometry('500x400')
ws['bg'] = 'black'
ws.resizable(width=True, height=True)
URL_GET = ''
URL_POST = ''


def get_directory():
    global URL_GET
    URL_GET = filedialog.askdirectory()
    text = tk.Label(ws, text=f'{URL_GET}', bg='black', fg='white')
    text.place(relx=0.5, rely=0.2, anchor=CENTER)
    return URL_GET


def post_directory():
    global URL_POST
    URL_POST = filedialog.askdirectory()
    text = tk.Label(ws, text=f'{URL_POST}', bg='black', fg='white')
    text.place(relx=0.5, rely=0.4, anchor=CENTER)
    return URL_POST


button_a = tk.Button(ws, text="Выберите папку поиска",
                     padx=100,
                     pady=10,
                     command=lambda: get_directory())
button_b = tk.Button(ws, text="Выберите папку сохранения",
                     padx=86,
                     pady=10,
                     command=lambda: post_directory())
button_a.place(relx=0.5, rely=0.1, anchor=CENTER)
button_b.place(relx=0.5, rely=0.3, anchor=CENTER)


def convert(URL_GET, URL_POST):
    if URL_GET == '':
        messagebox.showerror("Ошибка", "Задайте папку для поиска")
    elif URL_POST == '':
        messagebox.showerror("Ошибка", "Задайте папку для сохранения")
    dir_path = URL_GET
    print(dir_path)
    images = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.png'):
                URL = str(root) + "\\" + str(file)
                images.append(URL)
    hsize = min(5, len(images))
    vsize = (len(images)/5) + 1

    vspace = 2
    hspace = 2

    (h, w) = Image.open(images[0]).size
    size_x = int((vsize*(w+vspace)))
    im = Image.new('RGB', ((hsize*(h+hspace)), size_x))

    for i, filename in enumerate(images):
        imin = Image.open(filename).convert('RGB')
        xpos = i % hsize
        ypos = i / hsize
        ypos = int(ypos)
        im.paste(imin, (xpos*(h+hspace), ypos*(w+vspace)))

    im.save(fr'{URL_POST}\output.tiff')
    text = tk.Label(ws, text=f'Готово!', bg='black', fg='white')
    text.place(relx=0.5, rely=0.6, anchor=CENTER)


save_button = tk.Button(ws, text="Сохранить",
                        padx=100,
                        pady=10,
                        command=lambda: convert(URL_GET, URL_POST))
save_button.place(relx=0.5, rely=0.5, anchor=CENTER)
ws.mainloop()
