# Audiolog - Downloader MP3 | testes v0.1
from pytubefix import YouTube

# Diretorio de saída de download
diretorio = 'C:\\Users\\User\\OneDrive\\Área de Trabalho\\baixados'

def BaixarMP3(link):
    try:
        video = YouTube(link)
        musica = video.streams.get_audio_only()
        musica.download(mp3=True,output_path=diretorio)
        print(f'{video.title} baixado com sucesso!')
    except:
        print('Erro econtrado ao tentar realizar o download!')

def BaixarMP4(link):
    try:
        video = YouTube(link)
        vd = video.streams.get_highest_resolution()
        vd.download(output_path=diretorio)
    except:
        print('Erro econtrado ao tentar realizar o download!')