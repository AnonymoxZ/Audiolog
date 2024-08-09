# Audiolog - Downloader MP3 | v0.1
from pytubefix import YouTube
from settings import *

# Diretorio de saída de download
diretorio = 'C:\\Users\\User\\OneDrive\\Área de Trabalho\\baixados'

def BaixarMP3(link):
    try:
        video = YouTube(link)
        musica = video.streams.get_audio_only()
        musica.download(mp3=True)
        NoteSucess(video.title)
    except:
        NoteError()

def BaixarMP4(link):
    try:
        video = YouTube(link)
        vd = video.streams.get_highest_resolution()
        vd.download()
        NoteSucess(video.title)
    except:
        NoteError()
