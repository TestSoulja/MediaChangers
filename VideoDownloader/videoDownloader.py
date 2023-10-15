from pytube import YouTube
import os

s = os.path.abspath(__file__)
c = s.replace(os.path.basename(os.path.abspath(__file__)), '')


yt = YouTube('https://www.youtube.com/watch?v=zqXohGL36cw') #ссылка на видео.

# itag = 137
itag = 139

def Tags():
    for el in yt.streams:
        print(el)

def Vid():
    print(yt.streams.filter(file_extension='mp4')) 
    stream = yt.streams.get_by_itag(itag) #выбираем по тегу, в каком формате будем скачивать.
    stream.download(c) #загружаем видео.
    
def Audi():
    stream = yt.streams.get_by_itag(itag) #выбираем по тегу, в каком формате будем скачивать.
    stream.download(c) #загружаем видео.
    
Audi()