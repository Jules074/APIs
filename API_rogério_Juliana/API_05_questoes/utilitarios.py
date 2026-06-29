def inteiro(label: str):
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
    return n

def min_num(label1: str, label3: str):
    limite = inteiro(label1)
    n = inteiro(label3)
    while n < limite:
        print('numero fora do limite minimo...')
        n = inteiro(label3)
    return n

def max_num(label2: str, label3: str):
    limite = inteiro(label2)
    n = inteiro(label3)
    while n > limite:
        print('numero fora do limite maximo...')
        n = inteiro(label3)
    return n

def min_max(label1: str, label2: str, label3: str):
    menor = inteiro(label1)
    maior = inteiro(label2)
    n = inteiro(label3)
    while not(menor < n < maior):
        print('valor não está entre os limites')
        n = inteiro(label3)
    return n