def main():
    nome = input('insira seu nome: ') #sara, juliana
    tamanho = len(nome) #4
    if tamanho % 2 == 0:
        for i in range(2, tamanho+2): #mostrar proximos quatro multiplos de 4
            print(tamanho * i)
    else: #mostrar divisores de Tamanho até 1
        for i in range(1, tamanho+1):
            if tamanho % i == 0:
                print(tamanho / i)

main()