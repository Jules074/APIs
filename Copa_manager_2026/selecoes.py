from persistencia import open_file_selecoes #copia das selecoes
from utils import *
#id;nome;confederacao;grupo;ranking_fifa;titulos 


def list_selecoes(selecoes):
    for selecao in selecoes:
        print(f'Seleção: {selecao['nome']}, ID: {selecao['id']}')



def achar_maior_id(selecoes):
    maior_id = 0
    for selecao in selecoes:
        if selecao['id'] > maior_id:
            maior_id = selecao['id']
    return maior_id



def cadastrar_selecao(selecoes):
    lista_selecoes_temp = selecoes

    nova_selecao_nome = input('''
    Digite o nome da nova seleção:
                            
    >> ''')
    
    for selecao in lista_selecoes_temp:
        if nova_selecao_nome == selecao['nome']:
            return 0
        
        for i in nova_selecao_nome:
            if ord(i) not in range(97,123):
                return 1
    
    maior_id = achar_maior_id(lista_selecoes_temp)
    novo_id = maior_id + 1

    dados = [novo_id, nova_selecao_nome.strip().lower()]

    nova_selecao = {'id':dados[0],'nome':dados[1]}
    lista_selecoes_temp.append(nova_selecao)

    print(f'Nova seleção {nova_selecao['nome']} de ID {nova_selecao['id']} adicionada!')

    return lista_selecoes_temp

    

            

def excluir_selecao(selecoes):
    lista_selecoes_temp = selecoes

    try:
        id = int(input('''
    * Indique o ID da seleção que deseja excluir:
                    
    >> '''))
        
        lista_ids_selecoes = []
        for selecao in selecoes:
            lista_ids_selecoes.append(selecao['id'])

            if selecao['id'] == id:
                print(f'A seleção de {selecao['nome']} foi excluida!')
                lista_selecoes_temp.remove(selecao)
        
        if id not in lista_ids_selecoes:
            return 0


        return lista_selecoes_temp
    
    except:
        return 0



def buscar_por_nome_selecoes(selecoes): #ex: verificar se um país está na seleção
    nome = input('''
* Digite o nome da seleção:
                 
>> ''')
    
    selecoes_encontradas = []
    
    for selecao in selecoes:
        if nome.lower() in selecao['nome'].lower():
            selecoes_encontradas.append(selecao)

    if len(selecoes_encontradas) == 0:
        print('Não há seleções cadastradas com esse nome!')
    else:
        print('Seleções encontradas: '+'\n')
        for selecao in selecoes_encontradas:
            print(f'''
    - Nome: {selecao['nome']}, ID: {selecao['id']}\n''')




def ordenar_por_atributo_selecoes(selecoes):
    menu = menu_ordem_selecao()
    
    while True:
        
        comandos = [0,1,2,3,4]

        if menu not in comandos:
            print('Insira um comando válido!')
            break
            
        elif menu == 0: #sair
            print('Cancelado!')
            break

        elif menu == 1: #alfabetica
            ordenados = sorted(selecoes,key=alfabetica)
            for i in ordenados:
                print(f'Nome: {i['nome']}, ID: {i['id']}')
            break
        
        elif menu == 2: #econtralfabetica
            ordenados = sorted(selecoes,key=alfabetica,reverse=True)
            for i in ordenados:
                print(f'Nome: {i['nome']}, ID: {i['id']}')
            break

        elif menu == 3: #por id
            ordenados = sorted(selecoes,key=por_id)
            for i in ordenados:
                print(f'Nome: {i['nome']}, ID: {i['id']}')
            break

        elif menu == 4: #por id reversa
            ordenados = sorted(selecoes,key=por_id,reverse=True)
            for i in ordenados:
                print(f'Nome: {i['nome']}, ID: {i['id']}')
            break




def alfabetica(selecao):
    return selecao['nome']

def por_id(selecao):
    return selecao['id']