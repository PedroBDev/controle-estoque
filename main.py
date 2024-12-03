from class_Estoque import Estoque, Novo_estoque

#iniciando classe
estoque=Novo_estoque

while True:
    print('Bem Vindo ao Sistema de Estoque. Por favor, escolha uma das opções abaixo:'+ '\n')

    escolha_usuario = input('[C] - Cadastar Novo Produto | [L] - Listar Estoque |'
                            ' [I] - Exibir Info Produto | [A] - Alterar quantidade |'
                            ' [E] - Excluir Produto | [S] - Sair: ').upper()

    if escolha_usuario == 'C':
        #recebendo informações do produto
        nome = input('Informe o nome do produto:')
        quantidade = input('informe a quantidade do produto:')

        while True:
            #validando a quantidade informada pelo usuário
            try:
                quantidade = int(quantidade)
                break
            except ValueError:
                print('Por favor, informe um valor válido para quantidade')
                quantidade = input('informe a quantidade do produto:')

        estoque = Estoque(nome, quantidade)
        estoque.cadastrar_produto()

    elif escolha_usuario == 'L':
        estoque.listar_produtos()

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