from utilis import *

def main():
    vetor = abrir_arquivo()

    while True:
        opcao = menu()
        if opcao == 0:
            break
        elif opcao == 1:
            listar_vetores(vetor)
        elif opcao == 2:
            vetor = criar_carro(vetor)
            salvar(str(vetor))

            

main()