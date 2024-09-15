# Audiolog - Downloader MPS | v0.1
from pytubefix import YouTube
from pytubefix.cli import on_progress
from settings import *

# Diretorio de saída de download
musicas = 'C:\\Users\\Vitor\\OneDrive\\Área de Trabalho\\projetos\\Audiolog\\musicas'
videos = 'C:\\Users\\User\\OneDrive\\Área de Trabalho\\videos'

def BaixarMP3(link):
    audio = YouTube(link)
    musica = audio.streams.get_audio_only()
    musica.download(mp3=True)
    NoteSucess(audio.title)

def BaixarMP4(link):
    try:
        video = YouTube(link)
        vd = video.streams.get_highest_resolution()
        vd.download(output_path=videos)
    except:
        NoteError()

BaixarMP3('https://youtube.com/shorts/Uw6WuuFOwlk?si=nsbiJuCXhNoog62c')