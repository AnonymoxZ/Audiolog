# Audiolog - Interface Grafica | testes v0.1
import PySimpleGUI as tela
import settings
from dwd_mps import *

# configuraçoes de tela
titulo = 'Audiolog'
tela.theme('NeonBlue1')

# Interface principal
def Interface():
    definiçoes_tela = [[tela.Text('Insira o link para download:')],
                    [tela.Input(size=30,key='-URL-')],
                    [tela.Text('Escolha um formato para download:')],
                    [tela.Button('Baixar MP4',button_color='black', mouseover_colors='yellow'),tela.Button('Baixar M4A',mouseover_colors='blue')]]

    janela = tela.Window(titulo, definiçoes_tela)
    # loop da janela
    while True:
        event, values = janela.read()
        if event == tela.WIN_CLOSED:
            settings.NoteClose()
            quit()
            break
        elif event == 'Baixar MP4':
            # Baixando mp4 com sucesso
            if values['-URL-'] == '':
                print('Link vazio')
            else:
                link = values['-URL-']
                BaixarMP4(link)
                janela['-URL-'].update('')
        elif event == 'Baixar M4A':
            # Baixando mp3 com sucesso
            if values['-URL-'] == '':
                print('Link vazio')
            else:
                link = values['-URL-']
                BaixarM4A(link)
                janela['-URL-'].update('')
    janela.close()
