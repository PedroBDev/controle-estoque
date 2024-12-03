import json
CAMINHO_ARQUIVO='estoque.json'

def listar_produtos():
    # carregando lista de produtos:
    estoque = carregar_dados()

    # exibindo estoque:
    for info_estoque in estoque:
        print('Produto: {} | Quantidade: {} | Código do produto: {}'
              .format(info_estoque['nome'], info_estoque['quantidade'], info_estoque['id']))
        print('\n')
    print('-=' * 40)

def busca_por_id(codigo_produto):
    estoque = carregar_dados()
    for info_estoque in estoque:
        if info_estoque['id'] == codigo_produto:
            return info_estoque
    raise ValueError('Código não cadastrado!')



def carregar_dados():
    try:
        with open(CAMINHO_ARQUIVO, 'r') as arquivo:
            estoque = json.load(arquivo)
            return estoque

    except FileNotFoundError:
        print('Não há produtos cadastrados no estoque!')
        estoque = []
        return estoque


def salvar_dados(estoque):
    with open(CAMINHO_ARQUIVO, 'w+') as arquivo:
        json.dump(estoque, arquivo, indent=2)


def validacao_dados():
    while True:
        codigo_produto = input('Informe o código do produto(Se não souber, [L] - listar):')
        print('-=' * 40 + '\n')
        # listando caso o usuário não saiba o código
        if codigo_produto in ['l', 'L']:
            listar_produtos()
            print('-=' * 40 + '\n')
            continue
        else:
            # verificando se ele digitou um inteiro
            try:
                codigo_produto = int(codigo_produto)

            except ValueError:
                print('Por favor, digite um número inteiro!')
                continue

        estoque = carregar_dados()

        return codigo_produto, estoque