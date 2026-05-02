def main():
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    n5 = 0
    b0 = 0
    vencedor = 0
    vencedor_nome = ''

    while True:
        menu = int(input('''
    ------------MENU------------
    - votar (1);
    - ver resultado (2)
    - encerrar (3)
    -----------------------------
    > 
    '''))
    
        if menu == 3:
            break
        elif menu == 1:
            voto = int(input('''
    --------ELEIÇÃO--------
    - candidado 01 (1);
    - candidato 02 (2);
    - candidato 03 (3);
    - candidato 04 (4);
            
    - voto em branco (0);
    - volo nulo (5)
    ------------------------
    '''))
            if voto == 1:
                c1 += 1
                if c1 > vencedor:
                    vencedor = c1
                    vencedor_nome = 'candidato 01'
            elif voto == 2:
                c2 += 1
                if c2 > vencedor:
                    vencedor = c2
                    vencedor_nome = 'candidato 02'
            elif voto == 3:
                c3 += 1
                if c3 > vencedor:
                    vencedor = c3
                    vencedor_nome = 'candidato 03'
            elif voto == 4:
                c4 += 1
                if c4 > vencedor:
                    vencedor = c4
                    vencedor_nome = 'candidato 04'
            elif voto == 5:
                n5 += 1
                if n5 > vencedor:
                    vencedor = n5
                    vencedor_nome = 'sem vencedor'     #resolver dps
            elif voto == 0:
                b0 += 1
                if b0 > vencedor:
                    vencedor = b0
                    vencedor_nome = 'sem vencedor'
            else:
                print('valor inválido, vote corretamente')

        elif menu == 2:
            print(f'''
-----------RESULTADO-----------
- candidado 01: {c1} votos
- candidato 02: {c2} votos
- candidato 03: {c3} votos
- candidato 04: {c4} votos

- votos brancos: {b0} votos
- votos nulos: {n5} votos

- VENCEDOR: {vencedor_nome}
''')

main()