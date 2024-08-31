# Audiolog - Downloader MP3 | v0.1
from pytubefix import YouTube
from settings import *

# Diretorio de saída de download
musicas = 'C:\\Users\\User\\OneDrive\\Área de Trabalho\\musicas'
videos = 'C:\\Users\\User\\OneDrive\\Área de Trabalho\\videos'

def BaixarMP3(link):
    try:
        video = YouTube(link)
        musica = video.streams.get_audio_only()
        musica.download(mp3=True,output_path=musicas)
        NoteSucess(video.title)
    except:
        NoteError()

def BaixarMP4(link):
    try:
        video = YouTube(link)
        vd = video.streams.get_highest_resolution()
        vd.download(output_path=videos)
    except:
        NoteError()
