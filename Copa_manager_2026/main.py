from selecoes import *
from jogadores import *
from partidas import *
from utils import *
from persistencia import *

def main():

    lista_selecoes = open_file_selecoes()
    lista_jogadores = open_file_jogadores()
    lista_partidas = open_file_partidas()

    while True:
        
            comandos = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
            menu = show_menu()

            if menu not in comandos:
                print('Insira um comando válido!')
                clearscreen()


            elif menu == 0: #sair
                print('Saindo do programa...')
                salvar_selecoes(lista_selecoes)
                salvar_jogadores(lista_jogadores)
                #salvar_partidas(lista_partidas)
                print('Salvo!')
                clearscreen()
                break


            elif menu == 1: #cadastrar selecao
                verificacao = cadastrar_selecao(lista_selecoes)

                if verificacao == 1:
                    print('Insira um nome válido!!')
                    clearscreen()
                elif verificacao == 0:
                    print('Seleção já cadastrada!!')
                    clearscreen()
                else:
                    lista_selecoes = verificacao
                    clearscreen()


            elif menu == 2: #excluir selecao
                verificacao = excluir_selecao(lista_selecoes)

                if verificacao == 0:
                    print('Insira um ID válido!')
                    clearscreen()

                else:
                    lista_selecoes = verificacao
                    clearscreen()

            elif menu == 3: #listar seleções
                list_selecoes(lista_selecoes)
                clearscreen()

            elif menu == 4: #buscar por nome
                buscar_por_nome_selecoes(lista_selecoes)
                clearscreen()

            elif menu == 5: #ordenar por atributo
                ordenar_por_atributo_selecoes(lista_selecoes)
                clearscreen()
                



            elif menu == 6: #cadastrar jogador
                verificacao = cadastrar_jogador(lista_jogadores,lista_selecoes)

                if verificacao == 1:
                    print('Insira um nome válido!!')
                    clearscreen()

                elif verificacao == 0:
                    print('Jogador já cadastrado!!')
                    clearscreen()
                
                elif verificacao == 3:
                    print('Insira informações válidas!')
                    clearscreen()

                else:
                    lista_jogadores = verificacao
                    clearscreen()
                
            elif menu == 7: #excluir jogador
                verificacao = excluir_jogador(lista_jogadores)

                if verificacao == 0:
                    print('Insira um ID válido!')
                    clearscreen()

                else:
                    lista_jogadores = verificacao
                    clearscreen()
                
            elif menu == 8: #listar jogadores
                list_jogadores(lista_jogadores,lista_selecoes)
                clearscreen()
                
            elif menu == 9: #filtrar jogadores por atributo
                ordenar_por_atributo_jogadores(lista_jogadores,lista_selecoes)
                clearscreen()
                
            elif menu == 10: #artilheiros e estatisticas
                ...
                



            elif menu == 11: #cadastrar partida
                ...
            
            elif menu == 12: #excluir partida
                ...
            
            elif menu == 13: #listar partidas
                list_partidas(lista_partidas)
                clearscreen()

        

main()