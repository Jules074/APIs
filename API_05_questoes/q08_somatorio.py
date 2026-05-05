#numero perfeito = soma de todos os seus divisores, exceto ele mesmo

def main():
    num1 = int(input('insira limite minimo: '))
    num2 = int(input('insira limite maximo: '))

    for i in range(num1,num2+1):
        print(somatorio(i))


def eh_divisor(x,i): #ve se 1 numero é divisor de outro
    if x % i == 0:
        return i
    
def somatorio(a):
    soma = 0
    for i in range(1,a): #todos os divisores desse numero, exceto ele mesmo
        b = eh_divisor(a,i)
        if b != None:
            soma += b
    if a == soma:
        return f'{a} - perfeito'
    else:
        return f'{a} - não perfeito'



    
main() 