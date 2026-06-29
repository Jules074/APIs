def main():
    num1 = int(input('digite um numero: '))
    num2 = int(input('digite outro numero: '))

    '''show_divisores(num1)
    show_divisores(num2)'''

    mdc(num1,num2)

def eh_divisor(x,i):
    if x % i == 0:
        return i

'''def show_divisores(x): 
    print(f'---DIVISORES DO NUMERO {x}---')
    for i in range(1,x+1):
        a = eh_divisor(x,i)
        if a != None:
            print(a)'''#essa só printa a mensagem

def mdc(x,y):
    maior_numero = 0
    if x > y:
        maior_numero = x
    else:
        maior_numero = y

    '''for i in range(1,maior_numero+1):
        if eh_divisor(x,i) and eh_divisor(y,i):
            print(i)'''#essa printa todos os divisores comuns

    mdc = 0

    for i in range(1,maior_numero+1):
        if eh_divisor(x,i) and eh_divisor(y,i):
            if i > mdc:
                mdc = i
    print(mdc)
            
main()