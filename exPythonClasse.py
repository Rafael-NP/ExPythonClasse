class Produto:
    def __init__ (self, codigo, nome, qtd, precoUni):
        self.codigo = codigo
        self.nome = nome
        self.qtd = qtd
        self.precoUni = precoUni
    def mostrar(self):
        print(f"Produto: {self.nome} | Código: {self.codigo} | Quantidade : {self.qtd} | Preço Unitário: R${self.precoUni}")

produto1 = Produto(1, "Escova", 5, 6.7)
produto1.mostrar()