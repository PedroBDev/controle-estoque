from class_Estoque import Estoque, Novo_estoque
from utils import listar_produtos, parse_input

#iniciando classe
estoque=Novo_estoque
if __name__ == "__main__":
    while True:
        print("""
        Bem-vindo ao Sistema de Estoque!
        Escolha uma opção:
        [C] - Cadastrar Novo Produto
        [L] - Listar Estoque
        [I] - Exibir Informações de um Produto
        [A] - Alterar Quantidade
        [E] - Excluir Produto
        [S] - Sair
        """)
        escolha_usuario=input(':').upper()

        if escolha_usuario == 'C':
            #recebendo informações do produto
            nome = input('Informe o nome do produto:')
            tipo_produto = parse_input('O Produto é estocado por KG(granel)[S - SIM | N - NÃO]?')
            quantidade = input('informe a quantidade do produto:')

            if tipo_produto:  # validando a quantidade informada pelo usuário
                while True:

                    try:
                        quantidade = float(quantidade.replace(',' , '.'))
                        break
                    except ValueError:
                        print('Por favor, informe um valor válido para quantidade')
                        quantidade = input('informe a quantidade do produto:')
            else:
                while True:

                    try:
                        quantidade = int(quantidade)
                        break
                    except ValueError:
                        print('Este produto deve ser estocado com valor inteiro'+'\n'
                                        'Por favor, informe um valor válido para quantidade')
                        quantidade = input('informe a quantidade do produto:')

            estoque = Estoque(nome, quantidade)
            estoque.cadastrar_produto()

        elif escolha_usuario == 'L':
            listar_produtos()

        elif escolha_usuario == 'I':
            estoque.exbir_produto()

        elif escolha_usuario == 'A':
            estoque.alterar_quantidade()

        elif escolha_usuario == 'E':
            estoque.excluir_produto()

        elif escolha_usuario == 'S':
            break


        else:
            print('Opção inválida!' + '\n' + 'Por favor, informe uma opção válida')
            continue

    print('Obrigado por utilizar nosso Sistema de Controle de Estoque' + '\n' + 'Até a próxima!')

