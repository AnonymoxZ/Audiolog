# Audiolog - Interface Grafica | testes v0.1
import PySimpleGUI as tela
from settings import *
from dwd_mps import *


# configuraçoes de tela
titulo = 'Audiolog'
tela.theme('Black')

# Interface principal
def Interface():
    definiçoes_tela = [[tela.Text('Insira o link para download:')],
                    [tela.InputText()],
                    [tela.Text('Escolha um formato para download:')],
                    [tela.Button('Baixar MP4',button_color='yellow'),tela.Button('Baixar MP3',button_color='blue')]]

    janela = tela.Window(titulo, definiçoes_tela)
    # loop da janela
    while True:
        event, values = janela.read()
        if event == tela.WIN_CLOSED or event == "Encerrar":
            quit()
            exit()
        elif event == 'Baixar MP4':
            # Baixando mp4 com sucesso
            if values[0] == '':
                print('Link vazio')
            else:
                link = values[0]
                BaixarMP4(link)
        elif event == 'Baixar MP3':
            # Baixando mp3 com sucesso
            if values[0] == '':
                print('Link vazio')
            else:
                link = values[0]
                BaixarMP3(link)

    janela.close()
    Close()
