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

    for i in range(1,n+1):
        somatorio = 0

        somatorio += obter_respostas(pergunta1)
        somatorio += obter_respostas(pergunta2)
        somatorio += obter_respostas(pergunta3)
        somatorio += obter_respostas(pergunta4)
        somatorio += obter_respostas(pergunta5)
        somatorio += obter_respostas(pergunta6)
        somatorio += obter_respostas(pergunta7)
        somatorio += obter_respostas(pergunta8)
        somatorio += obter_respostas(pergunta9)

        
        

main()

def obter_respostas(x):
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
    return resposta
    
def calcular_scores(s):
    media = s / 9
    return media

    