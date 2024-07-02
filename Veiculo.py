class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info_veiculo(self):
        return f"Veículo: {self.modelo}, {self.marca} "


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano):
        Veiculo.__init__(self, marca, modelo)
        self.ano = ano

    def exibir_info_carro(self):
        return f"Carro: {self.marca} {self.modelo} {self.ano}"


class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)  # não pode usar self se por o super
        self.cilindrada = cilindrada

    def exibir_info_moto(self):
        return f"Moto: {self.marca}, {self.modelo}, Cilindrada: {self.cilindrada} cc"


# objeto carro com herenças da classe Veiculo
carro = Carro(marca="Honda", modelo="Civic", ano=2002)
moto = Moto(marca="Honda", modelo="Fan", cilindrada=150)

# Método de impressão dos atributos da classe Veículo
print(carro.exibir_info_veiculo())

# Método de impressão dos atributos da classe Carro
print(carro.exibir_info_carro())

print(moto.exibir_info_moto())

# atributos em Veiculo
print(moto.exibir_info_veiculo())
