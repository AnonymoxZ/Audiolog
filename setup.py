# Audiolog - Instalacao e criacao de ambiente
from os import system
from time import sleep

# Ambiente venv
system('py -m venv env')
sleep(5)
system('cd env')
system('cd scripts')
system('activate')

# Instalacao de bibliotecas
system('pip install pytubefix pysimplegui')