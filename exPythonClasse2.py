class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def exibir(self):
        print(f"Nome: {self.nome} | Preço: R${self.preco:.2f} \n")

produtos = []

def cadastrarProduto():
    print("\nCADASTRO DE PRODUTO")
    while True:
        try:
            nome = input("Digite o nome do produto: ")
            if nome == "":
                print("O nome do produto não pode ficar vazio.")
                continue
            preco = float(input("Digite o preço do produto: R$ "))
            if preco <= 0:
                print("O preço deve ser maior que zero.")
                continue
            produto = Produto(nome, preco)
            produtos.append(produto)
            print("Produto cadastrado com sucesso!")
            return
        except ValueError:
            print("Erro: valor de dado incorreto, cadastre novamente.")

def listarProdutos():
    i = 1
    print("\nLISTA DE PRODUTOS CADASTRADOS")
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return
    for produto in produtos:
        print(f"Produto: {i}")
        i += 1
        produto.exibir()

def comprarProduto():
    print("\nCOMPRA DE PRODUTO")
    if len(produtos) == 0:
        print("Não existem produtos cadastrados.")
        return
    listarProdutos()
    try:
        i = int(input("\nDigite o índice do produto que deseja comprar: "))
        if i < 0 or i > len(produtos):
            print("Erro: produto inexistente.")
            return
        qtd = int(input("Digite a quantidade: "))
        if qtd <= 0:
            print("A quantidade deve ser maior que zero.")
            return
        produto = produtos[i - 1]
        total = produto.preco * qtd

        print(f"\nRESUMO DA COMPRA\n Produto: {produto.nome} \n Preço unitário: R$ {produto.preco:.2f} \n Quantidade: {qtd} \n Total a pagar: R$ {total:.2f}")

        if total >= 100:
            print("Desconto disponível!")
        else:
            print("Sem desconto.")
    except ValueError:
        print("Erro: digite apenas números válidos.")


def menu():
    while True:
        print("\nSISTEMA DE PRODUTOS")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Comprar produto")
        print("4 - Sair\n")
        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                cadastrarProduto()
            elif opcao == 2:
                listarProdutos()
            elif opcao == 3:
                comprarProduto()
            elif opcao == 4:
                print("\nPrograma encerrado. Obrigado!")
                break
            else:
                print("Opção inválida. Escolha uma opção de 1 a 4.")
        except ValueError:
            print("Opção inválida. Escolha uma opção de 1 a 4.")
menu()