def main():
    n = int(input('numero de participantes: '))
    pergunta1 = '1. Sinto-me emocionalmente esgotado(a) pelos meus estudos/trabalho.'
    pergunta2 = '2. Sinto-me esgotado(a) ao final de um dia de estudos/trabalho.'
    pergunta3 = '3. Acordar de manhã e ter que enfrentar mais um dia me causa cansaço.'
    pergunta4 = '4. Sinto que me tornei mais indiferente com as pessoas ao meu redor.'
    pergunta5 = '5. Tenho me preocupado menos com o impacto do meu trabalho/estudo nas pessoas.'
    pergunta6 = '6. Sinto que as pessoas ao meu redor me culpam por alguns dos seus problemas.'
    pergunta7 = '7. Consigo lidar eficazmente com os problemas que surgem no meu dia a dia.'
    pergunta8 = '8. Sinto que estou tendo uma influência positiva na vida das pessoas.'
    pergunta9 = '9. Sinto-me estimulado(a) após trabalhar ou estudar com outras pessoas.'

    maior_exaustao = 0
    nome_maior_exaustao = ''
    menor_realizacao = 100000000
    nome_menor_realizacao = ''

    for i in range(1,n+1):
        sum_exaustao = 0
        sum_desper = 0
        sum_realizacao = 0
        nome = input('qual seu nome? ')

        sum_exaustao += obter_respostas(pergunta1)
        sum_exaustao += obter_respostas(pergunta2)
        sum_exaustao += obter_respostas(pergunta3)

        if sum_exaustao > maior_exaustao:
            maior_exaustao = sum_exaustao
            nome_maior_exaustao = nome

        sum_desper += obter_respostas(pergunta4)
        sum_desper += obter_respostas(pergunta5)
        sum_desper += obter_respostas(pergunta6)

        sum_realizacao += obter_respostas(pergunta7)
        sum_realizacao += obter_respostas(pergunta8)
        sum_realizacao += obter_respostas(pergunta9)

        if sum_realizacao < menor_realizacao:
            menor_realizacao = sum_realizacao
            nome_menor_realizacao = nome

        media_exaustao = calcular_scores(sum_exaustao)
        media_desper = calcular_scores(sum_desper)
        media_realizacao = calcular_scores(sum_realizacao)

        media_geral = round((sum_desper + sum_exaustao + sum_realizacao) / 9, 2)

        exibir_laudo(nome,media_exaustao,media_desper,media_realizacao)

    print(f'''
======= RESUMO DO ESTUDO =======
Respondentes : {n}
Maior Exaustão : {nome_maior_exaustao} ({maior_exaustao})
Menor Realização : {nome_menor_realizacao} ({menor_realizacao})
Média Geral Burnout : {media_geral}
''')

def obter_respostas(x):
    while True:
        resposta = int(input(f'''
        {x}
                                
        0 = Nunca 
        1 = Raramente 
        2 = Às vezes 
        3 = Regularmente
        4 = Frequentemente 
        5 = Quase sempre 
        6 = Sempre
        '''))

        if resposta not in range(1,7):
            print('insira um valor válido')
        return resposta

    
def calcular_scores(s):
    media = s / 3
    return round(media, 2)

def classificar_dimensao(a):
    if 4.0 <= a <= 6.0:
        return 'Alto 🔴'
        contador += 1
    elif 2.1 <= a <= 3.9:
        return 'Moderado ⚠️'
    elif 0.0 <= a <= 2.0:
        return 'Baixo ✅'
    
def classificar_realizacao(i):
    if 4.0 <= i <= 6.0:
        return 'Baixo 🔴'
        contador += 1
    elif 2.1 <= i <= 3.9:
        return 'Moderado ⚠️'
    elif 0.0 <= i <= 2.0:
        return 'Alto ✅'


def exibir_laudo(n,x,y,z):
    contador = 0
    print(f'''
========== LAUDO: {n} ==========
Exaustão Emocional : {x} → {classificar_dimensao(x)}
Despersonalização : {y} → {classificar_dimensao(y)}
Realização Pessoal : {z} → {classificar_realizacao(z)}
''')
    if classificar_dimensao(x) == 'Alto 🔴':
        contador += 1
    if classificar_dimensao(y) == 'Alto 🔴':
        contador += 1
    if classificar_realizacao(z) == 'Baixo 🔴':
        contador += 1
    
    if contador >= 1:
        print(f'''⚠️ Atenção: {contador} dimensão(ões) em nível crítico.
Recomenda-se acompanhamento profissional.''')

main() 