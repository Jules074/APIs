def main():
    n = int(input('numero de funcionarios analisados: '))

    for i in range(1,n+1):
        nome = input(f'nome {i}°: ')
        salario = float(input(f'salario bruto {i}°: '))
        extras = int(input(f'quant horas extras {i}°: '))

        h_normal = salario / 220 
        h_extra = (h_normal + h_normal/2)*extras #não dá o valor certo

        inss = salario*0.11

        if salario > 2000:
            v_refeicao = 150
        else:
            v_refeicao = 0

        s_liquido = salario - (inss + v_refeicao) + h_extra

        print(f'''
              ------EXTRATO: {nome}
              salario bruto = R${salario}
              horas extras = R${h_extra:.2f}  ({extras}h)
              inss = R${inss}
              vale refeição = R${v_refeicao}
              salario liquido = R${s_liquido:.2f}
              ''')
main()