#Peça ao usuário Renda Mensal, Valor Empréstimo e Prazo
#desejados, valide os dados a serem recebidos.
# Calcule e escreva na tela:
#a. Valor do IOF
#b. Valor dos Juros a pagar
#c. Valor Total a pagar (ex.: "R$ 5148,00")
#d. Valor da Parcela Mensal (ex.: "16x de R$ 321,75")
#e. Se Empréstimo APROVADO ou NEGADO (se a renda
#mensal suporta a parcela)

def main():
    renda_mensal = float(input('insira sua renda mensal: '))
    vemp = emprestimo()
    pm = parcelas(vemp,renda_mensal)
    print(f'R${pm}')

def emprestimo():
    valor_emprestimo = float(input('insira o valor do emprestimo: '))
    while valor_emprestimo < 1518.0:
        print('valor abaixo do minimo para emprestimos')
        valor_emprestimo = float(input('insira o valor do emprestimo: '))
    return valor_emprestimo

def juros(c,t):
    i = 14.75 / 100 #SELIC?
    juros = c*i*t
    return juros

def parcelas(vemp,rm):
    p = int(input('''---PRAZOS DISPONIVEIS---\n
          - 2x (minimo)
          - 24x (maximo)\n...'''))
    
    parcela_mensal = vemp / p

    while parcela_mensal > (rm * 30/100):
        print('valor da parcela não suportado por renda mensal, escolha outro prazo')
        p = int(input('''---PRAZOS DISPONIVEIS---\n
          - 2x (minimo)
          - 24x (maximo)\n...'''))
        
    parcela_juros = parcela_mensal + juros(parcela_mensal,p)
    return parcela_juros

main()