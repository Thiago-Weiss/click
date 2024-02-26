class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_recursivamente(valor, self.raiz)

    def _inserir_recursivamente(self, valor, no_atual):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(valor)
            else:
                self._inserir_recursivamente(valor, no_atual.esquerda)
        elif valor > no_atual.valor:
            if no_atual.direita is None:
                no_atual.direita = No(valor)
            else:
                self._inserir_recursivamente(valor, no_atual.direita)
        # Ignoramos valores duplicados

    def em_ordem(self, no=None):
        if no is None:
            no = self.raiz
        if no is not None:
            if no.esquerda is not None:
                self.em_ordem(no.esquerda)
            print(no.valor)
            if no.direita is not None:
                self.em_ordem(no.direita)


# Exemplo de uso
arvore = ArvoreBinaria()
arvore.inserir(5)
arvore.inserir(10)
arvore.inserir(2)
arvore.inserir(20)
arvore.inserir(55)
arvore.inserir(1)


print("Percurso em ordem:")
arvore.em_ordem()

