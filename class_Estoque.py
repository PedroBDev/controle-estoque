import json
from utils import carregar_dados, salvar_dados, validacao_dados, busca_por_id, parse_input

CAMINHO_ARQUIVO='estoque.json'

class Estoque:

    def __init__(self, nome_produto, quantidade):
        if not nome_produto or not isinstance(nome_produto, str):
            raise ValueError('Nome do Produto deve ser uma string não vazia!')
        if quantidade<0:
            raise ValueError('A Quantidade não deve ser negativa!')

        self.nome_produto = nome_produto
        self.quantidade = quantidade
        self.id = None


    def cadastrar_produto(self):

        try:
            with open(CAMINHO_ARQUIVO, 'r+') as arquivo:
                lista_id = json.load(arquivo)
            id_counter = lista_id[-1]['id']
        except FileNotFoundError:
            id_counter = 0

        self.id= id_counter + 1
        info_produtos = {'nome': self.nome_produto, 'quantidade' : self.quantidade, 'id' : self.id}

        #carregando dados
        estoque = carregar_dados()

        #adicionando novo produto
        estoque.append(info_produtos)

        salvar_dados(estoque)
        print('Produto cadastrado com sucesso!')
        print('-='*40 + '\n')

    def excluir_produto(self):
        counter = 0
        while True:
            codigo_produto, estoque = validacao_dados()



            #verificando se o id passado corresponde
            try:
                info_estoque = busca_por_id(codigo_produto)
                estoque.remove(info_estoque)

                #salvando nova lista em json
                salvar_dados(estoque)
                print('Produto removido com sucesso')
                print('-=' * 40 + '\n')
                counter+=1
                break


            except FileNotFoundError:
                print('Erro: Não foi possivel remover produto do estoque!' + '\n' + 'Verifique com o admnistrador')
                print('-=' * 40 + '\n')

            if counter == 0:
                print('Erro: Produto não encontrado!' + '\n' + 'Por favor, digite um valor válido!')
                continue
            else:
                break


    def alterar_quantidade(self):
        #contador para validação
        counter = 0
        while True:
            codigo_produto, estoque = validacao_dados()

            tipo_produto = parse_input('O Produto é estocado por KG(granel)[S - SIM | N - NÃO]?')

                    #verificando se o id passado corresponde
            for info_estoque in estoque:
                if codigo_produto == info_estoque['id']:
                    if not tipo_produto:
                        #recebendo a quantidade e verificando se é uma entrada válida
                        while True:
                            try:
                                nova_quantidade = input('Informe a nova quantidade:')
                                nova_quantidade = int(nova_quantidade)
                                info_estoque['quantidade']=nova_quantidade
                                counter+=1
                                salvar_dados(estoque)
                                print('Quantidade alterada com sucesso!')
                                break


                            except ValueError:
                                print('O produto só aceita valor inteiro' + '\n' +
                                      'Por favor, Digite um valor válido!')

                    else:
                            # recebendo a quantidade e verificando se é uma entrada válida
                            while True:
                                try:
                                    nova_quantidade = input('Informe a nova quantidade:')
                                    nova_quantidade = float(nova_quantidade.replace(',', '.'))
                                    info_estoque['quantidade'] = nova_quantidade
                                    counter += 1
                                    salvar_dados(estoque)
                                    print('Quantidade alterada com sucesso!')
                                    break


                                except ValueError:
                                    print('Por favor, Digite um valor válido!')


            if counter == 0:
                print('Produto não encontrado!' + '\n' + 'Por favor, digite um valor válido!')
                continue
            else:
                break

    def exbir_produto(self):
        # contador para validação
        counter = 0

        while True:
            #validando dados
            codigo_produto, estoque= validacao_dados()

            #buscando por id
            try:
                info_estoque=busca_por_id(codigo_produto)
                print('Produto: {} | Quantidade: {} | Código do Produto: {}'
                            .format(info_estoque['nome'],info_estoque['quantidade'], info_estoque['id']))
                counter+=1

            except ValueError:
                print('Erro: Código não cadastrado! Insira um código válido.')
            if counter == 0:
                print('Produto não encontrado!' + '\n' + 'Por favor, digite um valor válido!')
                continue
            else:
                break




Novo_estoque=Estoque('a', 1)

