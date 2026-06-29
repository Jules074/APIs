#id;selecao_casa_id;selecao_fora_id;gols_casa;gols_fora;fase
from utils import *

def list_partidas(partidas,selecoes):
    lista_fases = [{'2°s de final':32}, {'8°s de final':16}, {'4°s de final':8}, {'semifinais':4}, {'final':2}, {'3° lugar':3}]

    for partida in partidas:
        for fase in lista_fases:
            if partida['fase'] == fase.values():
                nome_fase = fase.keys()


        for selecao in selecoes:
            if partida['casa_id'] == selecao['id']:
                casa = selecao['nome']
            if partida['fora_id'] == selecao['id']:
                fora = selecao['nome']

            print(f'''
    ---- Partida: {partida['id']} ----, 
    * {casa} ( {partida['gols_casa']} X {partida['gols_fora']} ) {fora}
    * Fase: {nome_fase}

''')
    



def achar_maior_id(partidas): #cadastrar partidas
    maior_id = 0
    for partida in partidas:
        if partida['id'] > maior_id:
            maior_id = partida['id']
    return maior_id



def cadastrar_partida(partidas,selecoes):
    lista_partidas_temp = partidas

    selecao_casa_id = int(input('''
    Digite o ID da 1° seleção:
                            
    >> '''))

    selecao_fora_id = int(input('''
    Digite o ID da 2° seleção:
                            
    >> '''))

    
    for partida in partidas:
        if partida['selecao_casa_id'] == selecao_casa_id and partida['selecao_fora_id'] == selecao_fora_id:
            return 0

        elif partida['selecao_fora_id'] == selecao_casa_id and partida['selecao_casa_id'] == selecao_fora_id:
            return 0
        
        else:

            gols_casa = int(input('''
            Digite a quantidade de gols da 1° seleção:
                                    
            >> '''))

            gols_fora = int(input('''
            Digite a quantidade de gols da 2° seleção:
                                    
            >> '''))

            fase = menu_fases()
            
        
            maior_id = achar_maior_id(partidas)
            novo_id = maior_id + 1


            #id;selecao_casa_id;selecao_fora_id;gols_casa;gols_fora;fase
            dados = [novo_id, selecao_casa_id.strip(),selecao_fora_id.strip(),gols_casa.strip(),gols_fora.strip(),fase.strip()]

            nova_partida = {'id':dados[0],'selecao_casa_id':dados[1],'selecao_fora_id':dados[2],'gols_casa':dados[3],'gols_fora':dados[4],'fase':dados[5]}

            lista_partidas_temp.append(nova_partida)


            for selecao in selecoes:
                if partida['casa_id'] == selecao['id']:
                    casa = selecao['nome']
                if partida['fora_id'] == selecao['id']:
                    fora = selecao['nome']


            print(f'Nova partida cadastrada: {casa} X {fora} de ID {nova_partida['id']}.')


            clearscreen()
            return lista_partidas_temp

            

def excluir_partida(partidas,selecoes):
    lista_partidas_temp = partidas

    id = int(input('''
* Indique o ID do partida que deseja excluir:
                   
>> '''))
    
    for partida in partidas:
        for selecao in selecoes:
            if partida['casa_id'] == selecao['id']:
                casa = selecao['nome']
            if partida['fora_id'] == selecao['id']:
                fora = selecao['nome']

        if partida['id'] == id:
            print(f'A partida {casa} X {fora} foi excluida!')
            lista_partidas_temp.remove(partida)
        

    return lista_partidas_temp


