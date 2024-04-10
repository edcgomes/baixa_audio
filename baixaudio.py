from pytube import YouTube
from tkinter import *

YELLOW = "#f7f5dd"

# url = input("Insira a url do vídeo: ")

# yt = YouTube(url)

# audio = yt.streams.filter(only_audio=True).first()

# audio.download()
# if audio.on_complete():
#     print("download concluído")

window = Tk()
window.title("Baixaudio")
window.config(padx=50, pady=30, bg=YELLOW)

canvas = Canvas(window, width=300, height=200)
canvas.pack()

url = canvas.create_text(150, 30, text="Insira a url do vídeo: ")

entry = Entry(window)
canvas.create_window(150, 80, window=entry)


def baixaudio():
    value = entry.get()

    def complete_func():
        global url
        url = canvas.create_text(150, 10, text="DOWNLOAD CONCLUÍDO ")

    yt = YouTube(value, on_complete_callback= complete_func())
    audio = yt.streams.filter(only_audio=True).first()
    audio.download()
    canvas.create_window(900, 170)


enviar = Button(text="Enviar", command=baixaudio)
canvas.create_window(150, 140, window=enviar)

window.mainloop()
