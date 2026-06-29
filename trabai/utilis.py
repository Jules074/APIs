def menu():
    menu = int(input('''
-------------PATROCARS--------------
- Listar Vetores (1)
- Criar vetor (2)
- Atualizar vetor (3)
- Filtrar vetor (4)
- Remover item
                     
- sair (0)
                     
>> '''))
    return menu

def abrir_arquivo():
    vetor = []
    arquivo = open('vetores_carros.txt')

    lines = arquivo.readlines()

    for line in lines:
        dados = line.strip().split(',')
        carro = {'nome':dados[0],'ano':int(dados[1]),'preco':float(dados[2])}
        vetor.append(carro)

    arquivo.close()

    return vetor #retorna dicionario

def listar_vetores(v):
    arquivo = open('vetores_carros.txt')

    lines = arquivo.readlines()

    for line in lines:
        dados = line.strip().split(',')
        print(dados)

    arquivo.close()

def criar_carro(v):
    vetor_antigo = v
    dados = input('''
>> Digite os dados do novo carro separados por vírgula:
                  
>> ''')
    dados_separados = dados.split(',')
    novo_carro = {'nome':dados_separados[0],'ano':dados_separados[1],'preco':dados_separados[2]}
    vetor_antigo.append(novo_carro)

    return vetor_antigo

def salvar(v):
    vetor = v
    arquivo = open('vetores_carros.txt')
    
    lista_vetores = vetor.split(',')
    for i in lista_vetores:
        arquivo.write(str(i))

    arquivo.close()
    
