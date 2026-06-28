#id;selecao_casa_id;selecao_fora_id;gols_casa;gols_fora;fase

from persistencia import open_file_partidas
from persistencia import open_file_selecoes
from utils import clearscreen


copia_partidas = open_file_partidas()
copia_selecoes = open_file_selecoes()

def list_partidas(partidas):
    for partida in partidas:
        for selecao in copia_selecoes:
            if partida['casa_id'] == selecao['id']:
                casa = selecao['nome']
            if partida['fora_id'] == selecao['id']:
                fora = selecao['nome']
            print(f'Partida: {partida['id']}, Casa: {casa}, Fora: {fora}')



def achar_maior_id(partidas):
    maior_id = 0
    for partida in partidas:
        if partida['id'] > maior_id:
            maior_id = partida['id']
    return maior_id



def cadastrar_partida(partidas):
    lista_partidas_temp = partidas

    novo_partida_nome = input('''
    Digite o nome da nova seleção:
                            
    >> ''')
    
    for partida in partidas:
        if novo_partida_nome == partida['nome']:
            print('Este partida já está cadastrado!')
            return None
    
    maior_id = achar_maior_id(partidas)
    novo_id = maior_id + 1

    dados = [novo_id, novo_partida_nome.strip()]

    novo_partida = {'id':dados[0],'nome':dados[1]}

    lista_partidas_temp.append(novo_partida)

    clearscreen()
    return lista_partidas_temp

            

def excluir_partida(partidas):
    lista_partidas_temp = partidas

    id = int(input('''
* Indique o ID do partida que deseja excluir:
                   
>> '''))
    
    for partida in partidas:
        if partida['id'] == id:
            print(f'O partida {partida['nome']} foi excluido!')
            lista_partidas_temp.remove(partida)
            
    return lista_partidas_temp


