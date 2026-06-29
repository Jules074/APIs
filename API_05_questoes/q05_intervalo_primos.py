from q02_funcoes import inteiro

def main():
    num = get_intervalo('insira um limite minimo:\n', 
                        'insira um limite maximo:\n')
    print(num) 

#1
#10
#
def get_primo(n):
    contador = 0
    for i in range(1,n+1):
        if n % i != 0:
            contador += 1
            if contador > 2:
                return n

def get_intervalo(label1: str, label2:str):
    menor = inteiro(label1) ###
    maior = inteiro(label2) ###

    for i in range(menor,maior+1):
        return get_primo(i)
    


            
    
        


main()