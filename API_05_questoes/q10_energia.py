#O valor individual do KWh padrão é de R$ 0,89.
#b. Entretanto, famílias com consumo de até 30 KWh/mês tem redução de 100% no
#valor do KWh.
#c. Já as famílias com consumo superior a 200 KWh/mês pagam 30% mais caro por
#cada KWh.
#d. A tarifa de iluminação também vem integrada com o talão de energia, e na
#XPTO, custa 3% do valor do consumo (sem impostos e taxas), cobrada apenas
#de famílias com valor a pagar acima de R${}
#e. Uma vez calculado o valor da fatura, calcule-se então os impostos da seguinte
#forma: ICMS 25% e PIS/COFINS 3,75%. Assim a soma de tudo tem o valor a
#pagar pelo consumidor.
#f. Leia nome e consumo de N famílias, peça N e então os dados
#g. Escreva na tela todos os extratos calculados no padrão abaixo:

def main():
    quant_familias = int(input('quantas familias? '))
    get_dados(quant_familias)
    
#Bandeira Tarifária: R${} (valor por 100KWh: R${})

def get_dados(qf):
    for i in range(qf):
        nome = input('insira seu nome: ')
        consumo_klwt = int(input('consumo de kilowatts: '))
        vk = valor_klwt(consumo_klwt)
        ti = taxa_iluminacao(vk)
        fatura = vk + ti
        f_impostos = icms(fatura) + piscofins(fatura)

        print(f'''      ****** TALÃO MENSAL XPTO ********
        Consumidor: {nome}
        Consumo (KWh): {consumo_klwt}
        Consumo (R$): R${vk} (valor por KWh: R$0.89)
        Total sem Impostos: R${fatura}
        ICMS: R${icms(fatura)}
        PIS/COFINS: R${piscofins(fatura)}
        Iluminação Pública: R${ti}
        —-----------—-----------—-----------—-----------
        Total a Pagar: R${f_impostos}
        ''')

def valor_klwt(ck):
    valor = 0
    if ck < 30:
        return valor
    elif valor > 200:
        valor = ck * 0.89 + ((ck * 0.89) * 0.3)
        return valor
    else:
        valor = ck * 0.89
        return valor

def taxa_iluminacao(v):
    if v == 0:
        return 0
    elif v > 0:
        return v * 0.03
    
def icms(f):
    icms = f * 0.25
    return icms

def piscofins(f):
    pis_cofins = f * 0.375
    return pis_cofins

main()