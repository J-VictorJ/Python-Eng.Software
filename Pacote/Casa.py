class Casa:
    # def __init__(self, quartos=None, banheiro=None, garagem=False, jardim=False):
    def __init__(self):
        self.quartos = None
        self.banheiro = None
        self.garagem = False
        self.jardim = False

    def __str__(self):
        caracteristicas = []
        if self.quartos:
            caracteristicas.append(f"Número de quartos: {self.quartos}")
        if self.banheiro:
            caracteristicas.append(f"Número de banheiros: {self.banheiro}")
        if self.garagem:
            caracteristicas.append("Possui garagem")
        if self.jardim:
            caracteristicas.append("Possui jardim")
        return ", ".join(caracteristicas)


# Design Pattern Builder
class ConstruirCasa:
    def __init__(self):
        self.casa = Casa()

    def quartos(self, quartos):
        self.casa.quartos = quartos
        return self

    def banheiro(self, banheiro):
        self.casa.banheiro = banheiro
        return self

    def adicionar_garagem(self):
        self.casa.garagem = True
        return self

    def adicionar_jardim(self):
        self.casa.jardim = True
        return self

    def obter_casa(self):
        return self.casa


outra_casa = ConstruirCasa().quartos(4).banheiro(3).obter_casa()
print("Características da outra casa:", outra_casa)

# casa = Casa(quartos=3, banheiro=2, garagem=True, jardim=True)
# print(f"Características da casa: {casa}")


