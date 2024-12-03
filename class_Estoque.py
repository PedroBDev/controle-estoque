import json
CAMINHO_ARQUIVO='estoque.json'

class Estoque:
    try:
        with open(CAMINHO_ARQUIVO, 'r+') as arquivo:
            lista_id = json.load(arquivo)
        id_counter=lista_id[-1]['id']
    except FileNotFoundError:
        id_counter = 0

    def __init__(self, nome_produto, quantidade):
        self.nome_produto = nome_produto
        self.quantidade = quantidade
        self.id = Estoque.id_counter


    def __salvar_json(self, estoque):

        with open(CAMINHO_ARQUIVO, 'w+') as arquivo:
            json.dump(estoque, arquivo, indent=2)

    def __validacao_dados(self):
        while True:
            codigo_produto = input('Informe o código do produto(Se não souber, [L] - listar):')
            print('-='*40 + '\n')
            #listando caso o usuário não saiba o código
            if codigo_produto in ['l', 'L']:
                Estoque.listar_produtos(self)
                print('-='*40 + '\n')
                continue
            else:
               #verificando se ele digitou um inteiro
                try:
                    codigo_produto = int(codigo_produto)

                except ValueError:
                    print('Por favor, digite um número inteiro!')
                    continue
            try:
                with open(CAMINHO_ARQUIVO, 'r+') as arquivo:
                    estoque = json.load(arquivo)
                    break

            except FileNotFoundError:
                print('Não há produtos cadastrados no estoque!')
                break

        return codigo_produto, estoque

    def cadastrar_produto(self):
        self.id=Estoque.id_counter + 1
        info_produtos = {'nome': self.nome_produto, 'quantidade' : self.quantidade, 'id' : self.id}


        #lendo arquivo json existente
        try:
            with open(CAMINHO_ARQUIVO, 'r+') as arquivo:
                estoque = json.load(arquivo)

        except FileNotFoundError:
            estoque = []

        #adicionando novo produto
        estoque.append(info_produtos)

        self.__salvar_json(estoque)
        print('Produto cadastrado com sucesso!')
        print('-='*40 + '\n')

    def listar_produtos(self):
        #carregando lista de produtos:
        with open (CAMINHO_ARQUIVO, 'r+') as arquivo:
            estoque = json.load(arquivo)

        #exibindo estoque:
        for info_estoque in estoque:
            print('Produto: {} | Quantidade: {} | Código do produto: {}'
                  .format(info_estoque['nome'], info_estoque['quantidade'], info_estoque['id']))
            print('\n')
        print('-='*40)

    def excluir_produto(self):
        counter = 0
        while True:
            codigo_produto, estoque =self.__validacao_dados()



            #verificando se o id passado corresponde
            try:
                for info_estoque in estoque:
                    if  codigo_produto== info_estoque['id']:
                        #removendo produto da lista por id
                        estoque.remove(info_estoque)

                        #salvando nova lista em json
                        with open(CAMINHO_ARQUIVO, 'w+') as arquivo:
                            json.dump(estoque, arquivo, indent=2)
                        print('Produto removido com sucesso')
                        print('-=' * 40 + '\n')
                        counter+=1
                        break


            except FileNotFoundError:
                print('Erro ao remover produto do estoque!' + '\n' + 'Tente Novamente!')
                print('-=' * 40 + '\n')

            if counter == 0:
                print('Produto não encontrado!' + '\n' + 'Por favor, digite um valor válido!')
                continue
            else:
                break






    def alterar_quantidade(self):
        #contador para validação
        counter = 0
        while True:
            codigo_produto, estoque=self.__validacao_dados()

            #verificando se o id passado corresponde
            for info_estoque in estoque:
                if codigo_produto==info_estoque['id']:

                    #recebendo a quantidade e verificando se é uma entrada válida
                    while True:
                        try:
                            nova_quantidade = input('Informe a nova quantidade:')
                            nova_quantidade = int(nova_quantidade)
                            info_estoque['quantidade']=nova_quantidade
                            counter+=1
                            self.__salvar_json(estoque)
                            break


                        except ValueError:
                            print('Você não digitou um inteiro!' + '\n' 'Por favor, Digite um valor válido!')


            if counter == 0:
                print('Produto não encontrado!' + '\n' + 'Por favor, digite um valor válido!')
                continue
            else:
                break

    def exbir_produto(self):
        # contador para validação
        counter = 0


        while True:
            codigo_produto, estoque=self.__validacao_dados()
            for info_estoque in estoque:
                if codigo_produto==info_estoque['id']:
                    print('Produto: {} | Quantidade: {} | Código do Produto: {}'
                            .format(info_estoque['nome'],info_estoque['quantidade'], info_estoque['id']))
                    counter+=1
            if counter == 0:
                print('Produto não encontrado!' + '\n' + 'Por favor, digite um valor válido!')
                continue
            else:
                break




Novo_estoque=Estoque(None, None)

