#a. Receber texto
#b. Receber min e max caract

from utilitarios import int_positivo, inteiro

def main():
    texto = min_max_carac('insira um limite minimo:\n',\
                      'insira um limite maximo:\n',\
                      'insira um texto:\n')
    print(texto)

    #texto = receber_texto('insira um texto:\n')
    #print(texto)


"""def inteiro(label: str):
    while True:
        try:   
            n = int(input(label))
            return n
        except:
            print('o numero não é inteiro, tente novamente')

def int_positivo(label: str):
    n = inteiro(label)
    while 0 > n:
        print('numero negativo, tente novamente')
        n = inteiro(label)
    return n"""


def receber_texto(label: str):
    while True:
        try:   
            n = input(label)
            return n
        except:
            print('algo deu errado, tente novamente')

def min_max_carac(label1: str, label2: str, label3: str):
    limite_min = int_positivo(label1)
    limite_max = int_positivo(label2)
    n = receber_texto(label3)
    while not(limite_min <= len(n) <= limite_max):
        print('texto não está entre os limites de caracteres')
        n = receber_texto(label3)
    return n
    
main()
