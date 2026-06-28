def open_file_selecoes():
    arquivo = open('selecoes.txt')

    linhas = arquivo.readlines()

    collection = []

    for linha in linhas:
        dados = linha.strip().split(';')
        selecao = {'id': int(dados[0]), 'nome': dados[1]}
        collection.append(selecao)
    
    arquivo.close()

    return collection #devolve uma lista de dicionarios



#jogador_id;nome;id;posicao;idade;gols
def open_file_jogadores():
    arquivo = open('jogadores.txt')

    linhas = arquivo.readlines()

    collection = []

    for linha in linhas:
        dados = linha.strip().split(';')
        jogador = {'jogador_id': int(dados[0]), 'nome': dados[1], 'id': int(dados[2]),
                'posicao': dados[3], 'idade': int(dados[4]), 'gols': int(dados[5])}
        collection.append(jogador)
    
    arquivo.close()

    return collection #devolve uma lista de dicionarios



def open_file_partidas():
    arquivo = open('partidas.txt')

    linhas = arquivo.readlines()

    collection = []

    for linha in linhas: 
        dados = linha.strip().split(';')
        partida = {'id': int(dados[0]), 'id_casa': int(dados[1]), 'id_fora': int(dados[2]), 
                   'gols_casa': int(dados[3]), 'gols_fora': int(dados[4]), 'fase': dados[5]}
    
    arquivo.close()

    return collection #devolve uma lista de dicionarios



def salvar_selecoes(selecoes):
    lines = []
    for selecao in selecoes: #cada dicionario dentro da lista
        lines.append(f'{selecao['id']};{selecao['nome']};'+'\n') 
        
    file = open('selecoes.txt', 'w')
    file.writelines(lines)
    file.close()



def salvar_jogadores(jogadores):
    lines = []
    for jogador in jogadores: #cada dicionario dentro da lista
        lines.append(f'{jogador['jogador_id']};{jogador['nome']};{jogador['id']};{jogador['posicao']};{jogador['idade']};{jogador['gols']}'+'\n') 
        
    file = open('jogadores.txt', 'w')
    file.writelines(lines)
    file.close()
    


def salvar_partida(partidas):
    lines = []
    for partida in partidas: #cada dicionario dentro da lista
        lines.append(f'{partida['id']};{partida['id_casa']};{partida['id_fora']};{partida['gols_casa']};{partida['gols_fora']};{partida['fase']};'+'\n') 
        
    file = open('selecoes.txt', 'w')
    file.writelines(lines)
    file.close()

