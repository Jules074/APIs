#250 -- 5%
#250 a 500 -- 7%
#500 a 750 -- 8%
#750+ -- 20% e 25% ao valor acima de 750

def main():
    nome = input('nome: ')
    quant_compras = int(input('quant compras: '))
    total_faturado = 0
    total_cash = 0

    for i in range(1, quant_compras+1):
        v = valor_compra(i)
        total_faturado += v
        total_cash += cashback(v)
    
    print(f'''----COMPRAS----\n
            nome - {nome}\n
            total faturado pela loja (sem cash): {total_faturado}\n
            total gasto com cashback: {total_cash}''')
    
def valor_compra(i):
    c = float(input(f'valor compra {i}: '))
    return c

def cashback(c):
    if 0 < c < 250:
        cashback = c * 0.05
        return cashback
        
    elif 250 < c < 500:
        cashback = c * 0.07
        return cashback
        
    elif 500 < c < 750:
        cashback = c * 0.08
        return cashback
        
    else:
        acima = (c - 750) * 0.25
        cashback = 750 * 0.2 + acima
        return cashback



    
main()

