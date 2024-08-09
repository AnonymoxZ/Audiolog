# Instalador de pacotes
from os import system
from time import sleep

system('py -m venv .env')
sleep(8)
system('cd .env')
system('cd scripts')
system('activate.bat')
system('activate.ps1')
system('pip install pytubefix pysimplegui')