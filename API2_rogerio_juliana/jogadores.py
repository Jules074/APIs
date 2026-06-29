from persistencia import open_file_jogadores #copia dos jogadores
from persistencia import open_file_selecoes #copia das selecoes
from utils import *


def list_jogadores(jogadores,selecoes):
    for jogador in jogadores:
        for selecao in selecoes:
            if jogador['id'] == selecao['id']:
                print(f'Jogador: {jogador['nome']}, ID: {jogador['jogador_id']}, Seleção: {selecao['nome']}')



def achar_maior_id(jogadores):
    maior_id = 0
    for jogador in jogadores:
        if jogador['jogador_id'] > maior_id:
            maior_id = jogador['jogador_id']
    return maior_id



def cadastrar_jogador(jogadores,selecoes):
    lista_jogadores_temp = jogadores
    lista_selecoes_temp = selecoes #verificar_id_selecao

    novo_jogador_nome = input('''
    Digite o nome do novo jogador:
                            
    >> ''')

    if verificar_nome(lista_jogadores_temp,novo_jogador_nome) == 0:
        return 0
    
    while True:
        try:       
            selecao_jogador = int(input('''
            * Digite o ID da seleção do jogador:
            
            >> '''))

            if verificar_selecao(selecao_jogador,lista_selecoes_temp) == 3:
                return 3



            posicao_jogador = input('''
            * Digite a posição do jogador:
            
            >> ''')

            if verificar_posicao(posicao_jogador) == 3:
                return 3



            idade = int(input('''
            * Digite a idade do jogador:
            
            >> '''))

            quant_gols = int(input('''
            * Digite a quantidade de gols do jogador:
            
            >> '''))


            maior_id = achar_maior_id(lista_jogadores_temp)
            novo_id = maior_id + 1

            dados = [novo_id, novo_jogador_nome.strip(),selecao_jogador,posicao_jogador,idade,quant_gols]

            novo_jogador = {'jogador_id':dados[0],'nome':dados[1],'id':dados[2],'posicao':dados[3],'idade':dados[4],'gols':dados[5]}
            lista_jogadores_temp.append(novo_jogador)

            print(f'Novo jogador {novo_jogador['nome']} de ID {novo_jogador['id']} adicionado!')

            return lista_jogadores_temp    

        except:
            print('Dados inválidos!')
            break



def verificar_nome(lista_jogadores_temp,novo_jogador_nome):
    for jogador in lista_jogadores_temp:
        if novo_jogador_nome.lower() == jogador['nome'.lower()]:
            return 0
        
        for i in novo_jogador_nome.lower():
            if ord(i) not in range(97,123): #alfabeto minusculo
                if ord(i) == 32:
                    pass
                else:
                    return 1

def verificar_posicao(posicao):
    posicoes = ['atacante','goleiro','zagueiro','volante','meia','ponta']

    if posicao not in posicoes:
        return 3
    
def verificar_selecao(selecao_jogador, selecoes):
    lista_ids_selecoes = []
    for i in selecoes:
        lista_ids_selecoes.append(i['id'])
    
    if selecao_jogador not in lista_ids_selecoes:
        return 3
        

    
def excluir_jogador(jogadores):
    lista_jogadores_temp = jogadores

    try:
        id = int(input('''
    * Indique o ID do jogador que deseja excluir:
                    
    >> '''))
        
        lista_ids_jogadores = []
        for jogador in jogadores:
            lista_ids_jogadores.append(jogador['jogador_id'])

            if jogador['jogador_id'] == id:
                print(f'O jogador {jogador['nome']} foi excluido!')
                lista_jogadores_temp.remove(jogador)
        
        if id not in lista_ids_jogadores:
            return 0


        return lista_jogadores_temp
    
    except:
        return 0



def buscar_por_nome_jogadores(jogadores): #ex: verificar se um jogador está em alguma seleção e qual
    nome = input('''
* Digite o nome do jogador:
                 
>> ''')
    
    jogadores_encontrados = []
    
    for jogador in jogadores:
        if nome.lower() in jogador['nome'].lower():
            jogadores_encontrados.append(jogador)

    if len(jogadores_encontrados) == 0:
        print('Não há jogadores cadastrados com esse nome!')
    else:
        print('Jogadores encontrados: '+'\n')
        for jogador in jogadores_encontrados:
            print(f'''
    - Nome: {jogador['nome']}, ID: {jogador['id']}\n''') #colocar o nome da seleção tbm



def ordenar_por_atributo_jogadores(jogadores,selecoes):
    menu = menu_ordem_jogadores()
    
    while True:
        
        comandos = [0,1,2,3,4,5,6]

        if menu not in comandos:
            print('Insira um comando válido!')
            break
            
        elif menu == 0: #sair
            print('Cancelado!')
            break


        elif menu == 1: #nome
            achados = filtrar_por_nome(jogadores)
            
            if achados == 1:
                print('Não há jogadores com este nome...')
                break
            else:
                for i in achados:
                    print(f'Nome: {i['nome']}, ID: {i['id']}')
                break
        

        elif menu == 2: #idade
            achados = filtrar_por_idade(jogadores)

            if achados == 2:
                print('Não há jogadores com esta idade...')
                break
            else:
                for i in achados:
                    print(f'Nome: {i['nome']}, ID: {i['id']}, Idade: {i['idade']}')
                break


        elif menu == 3: #por id jogador
            achados = filtrar_por_id(jogadores)

            if achados == 3:
                print('Não há jogadores com este ID...')
                break
            else:
                for i in achados:
                    print(f'Nome: {i['nome']}, ID: {i['id']}')
                break


        elif menu == 4: #por id selecao
            achados = filtrar_por_selecao(jogadores) #recebe parametro

            if achados == 4:
                print('Não há jogadores com esta seleção...')
                break
            else:
                nome_selecao = ''

                for i in achados:
                    for selecao in selecoes:
                        if i['id'] == selecao['id']:
                            nome_selecao = selecao['nome']
                            break
                        break
                
                for i in achados:
                    print(f'Nome: {i['nome']}, ID: {i['id']}, Seleção: {nome_selecao}')
                        

        elif menu == 5: #por posicao
            achados = filtrar_por_posicao(jogadores)

            if achados == 5:
                print('Não há jogadores com esta posição...')
                break
            else:
                for i in achados:
                    print(f'Nome: {i['nome']}, ID: {i['id']}, Posição: {i['posicao']}')
                break


        elif menu == 6: #por mais gols
            achados = filtrar_por_gols(jogadores) #recebe parametro

            if achados == 6:
                print('Gols não achado... (???)')
                break
            else:
                for i in achados:
                    print(f'Nome: {i['nome']}, ID: {i['id']}, Gols: {i['gols']}')
                break

 
def filtrar_por_nome(jogadores):
    filtrados = []

    nome = input('''
* Insira o nome do jogador: 
>> ''')
    
    for jogador in jogadores:
        if nome in jogador['nome']:
            filtrados.append(jogador)

    if len(filtrados) == 0:
        return 1

    return filtrados



def filtrar_por_idade(jogadores):
    filtrados = []

    idade = int(input('''
* Insira a idade do jogador: 
>> '''))
    
    for jogador in jogadores:
        if jogador['idade'] == idade:
            filtrados.append(jogador)


    if len(filtrados) == 0:
        return 2
    
    return filtrados



def filtrar_por_id(jogadores):
    filtrados = []

    jogador_id = int(input('''
* Insira o ID do jogador: 
>> '''))

    for jogador in jogadores:
        if jogador['jogador_id'] == jogador_id:
            filtrados.append(jogador)

    return filtrados


def filtrar_por_selecao(jogadores):
    filtrados = []

    id_selecao = int(input('''
* Insira o ID da seleção do jogador: 
>> '''))
    
    for jogador in jogadores:
        if jogador['id'] == id_selecao:
            filtrados.append(jogador)

    if len(filtrados) == 0:
        return 4
    
    return filtrados



def filtrar_por_posicao(jogadores):
    filtrados = []

    posicao = input('''
* Insira a posicao do jogador: 
>> ''')

    for jogador in jogadores:
        if posicao in jogador['posicao']:
            filtrados.append(jogador)

    if len(filtrados) == 0:
        return 5
    
    return filtrados

    

def filtrar_por_gols(jogadores): #recebe parametro pra definir quem tem mais gols
    filtrados = []
    
    mais_gols = 0

    for jogador in jogadores:
        if jogador['gols'] > mais_gols:
            mais_gols = jogador['gols']
            
    for jogador in jogadores:
        if jogador['gols'] == mais_gols:
            filtrados.append(jogador)

    if len(filtrados) == 0:
        return 6
    
    return filtrados