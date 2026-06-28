import os #clearscreen
from persistencia import open_file_selecoes
from persistencia import open_file_jogadores

copia_selecoes = open_file_selecoes() #status
copia_jogadores = open_file_jogadores() #status

def clearscreen():
    input('')
    os.system('cls' if os.name == 'nt' else 'clear')


def status(x):
    counter = len(x)+1
    return counter


def show_menu():
    menu = int(input(f'''
--------- COPA MANAGER ---------
                     
status: {status(copia_selecoes)} seleções | {status(copia_jogadores)}  jogadores | ? partidas 

--------- SELEÇÃO --------------
* Cadastrar seleção (1)
* Excluir seleção (2)
* Listar seleções (3)
* Buscar seleção por nome (4)
* Ordenar por atributo (5)

-------- JOGADORES -------------
* Cadastrar jogador (6)
* Excluir jogador (7)
* Listar jogadores (8)
* Filtrar jogadores (9)
* Artilheiros e estatisticas (10)

-------- PARTIDAS --------------
* Cadastrar partida (11)
* Excluir partida (12)
* Listar partidas (13)

--------------------------------
* Sair (0)

>> ''')) 
    return menu


def menu_ordem_selecao():
    menu = int(input('''
---------- TIPO DE ORDEM ----------
* Alfabética (1)
* Contra-alfabética (2)
* N° ID (3)
* N° ID reverso (4)
* Cancelar (0)

>> '''))
    return menu


def menu_ordem_jogadores():
    menu = int(input('''
---------- TIPO DE ORDEM ----------
* Nome (1)
* Idade (2)
* N° ID (3)
* Seleção (4)
* Posição (5)
* Mais gols (6)
                     
* Cancelar (0)

>> '''))
    return menu