from pytube import YouTube

url = input("Cole o link do vídeo: ")
yt = YouTube(url)

audio = yt.streams.filter(only_audio=True).first()

audio.download()
