# Audiolog - Settings | v0.1
from os import system

# Static
def cls():
    system('cls')
    system('clear')

# Notas do sistema
def NoteError   ():
    print(46*'=')
    print('Erro encontrado ao tentar realizar download!')
    print(46*'=')
    print('\n')

def NoteClose():
    cls()
    print(30*'=')
    print('Close Audiolog')
    print(30*'=')
