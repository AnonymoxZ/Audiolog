# Audiolog - Downloader MPS | v0.1
from pytubefix import YouTube
from pytubefix.cli import on_progress
from settings import *

# Diretorio de saída de download
musicas = 'C:\\Users\\Vitor\\OneDrive\\Área de Trabalho\\musicas'
videos = 'C:\\Users\\User\\OneDrive\\Área de Trabalho\\videos'

def BaixarMP3(link):
    try:
        audio = YouTube(link,on_progress_callback = on_progress)
        musica = audio.streams.get_audio_only()
        musica.download(mp3=True)
        NoteSucess(audio.title)
    except:
        NoteError()

def BaixarMP4(link):
    try:
        video = YouTube(link)
        vd = video.streams.get_highest_resolution()
        vd.download()
    except:
        NoteError()
