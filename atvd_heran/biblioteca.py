class Animal():
    def __init__(self,nome,cor):
        self.nome=nome
        self.cor=cor

        def emitir_som(self):
            print(f"O {self.nome} emitiu um som...")

        def comer(self):
            print(f"O {self.nome} foi comer...")

class Gato(Animal):

    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def emitir_som(self):
        print(f"A {self.nome} foi miando...")

    def comer(self):
        print(f"A {self.nome} foi comer...")

class Cachorro(Animal):

    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def emitir_som(self):
        print(f"O {self.nome} foi latindo...")

    def comer(self):
        print(f"O {self.nome} foi comer...")


class Coelho(Animal):

    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def emitir_som(self):
        print(f"O {self.nome} foi pulando...")

    def comer(self):
        print(f"O {self.nome} foi comer...")


class Vaca(Animal):

    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def emitir_som(self):
        print(f"O {self.nome} foi mugindo...")

    def comer(self):
        print(f"O {self.nome} foi comer...")