#a. Receber número inteiro
#b. Receber número inteiro positivo
#c. Receber número inteiro de no mínimo X
#d. Receber número inteiro de no máximo X
#e. Receber número inteiro numa faixa min X e max Y

from utilitarios import min_max

def main():
    num_int = min_max('insira um limite minimo:\n',\
                      'insira um limite maximo:\n',\
                      'insira um valor inteiro:\n')
    print(num_int)
main()
   
"""if __name__ == '__main__':
    main()"""
