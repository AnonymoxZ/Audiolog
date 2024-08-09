# Audiolog - Settings | v0.1
from os import system

# Static
def cls():
    system('cls')
    system('clear')

# Notas do sistema
def Init():
    print(30*'=')
    print('Audiolog iniciado com sucesso')
    print(30*'=')
    print('\n')

def Close():
    cls()
    print(30*'=')
    print('Close Audiolog')
    print(30*'=')