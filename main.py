# Classe funcionários
class Funcionario:
    def __init__(self, RegID: int, nome: str, cargo: str, salario: int):
        self.RegId: int = RegID
        self.nome: str = nome
        self.cargo: str = cargo
        self.salario: int = salario

    def MostraReg(self):
        print()
        print(f"Registro {self.RegId}")
        print(f"O Nome do Funcionário é: {self.nome}")
        print(f"O cargo do {self.nome} é: {self.cargo}")
        print(f"O Salário do {self.cargo}, {self.nome} são: R${self.salario}")
        print()


# Iniciando os objetos baseados na Classe Funcionario
# funcionario1 = Funcionario(nome="Geraldo Garninzé", cargo="Min. do Golpe do Prix", salario=5000)
# funcionario2 = Funcionario(nome="Mr. Wick", cargo="O cara que mandam para desviver o Baba Yaga", salario=4800)

# Método MostrarReg
# funcionario1.MostrarReg()
# funcionario2.MostrarReg()

# Main

registro = ["Zero"]  # armazenar instâncias da classe Funcionario
Reg_ID = 0  # Contador para gerar novos produtos

while True:
    opcao = input("\r\n Selecione uma Opção:" +
                  "\r\n1-Adicionar Funcionário" +
                  "\r\n2-Mostrar Registros Existentes" +
                  "\r\n3-Sair" +
                  "\r\n >>> ")
    if opcao == '1':
        Reg_ID += 1  # prepara o contador de registro para o registro do endereço do objeto

        # Manter o usuário ou sair
        while True:
            nomeReg = input("Inserir o nome do funcionário: >>")
            cargoReg = input("Inserir o cargo do funcionário: >>")

            while True:
                try:
                    salarioReg = int(input("Inserir o salario do funcionário: >> "))
                    break
                except:
                    print("Apenas números!")
                    continue

            regFunc = Funcionario(RegID=Reg_ID, nome=nomeReg, cargo=cargoReg, salario=salarioReg)
            registro.append(regFunc)
            print(f"Registro {registro}")
            registro[Reg_ID].MostraReg()  # mostra o cadastro armazenado
            break
    elif opcao == '2':
        for i in range(1, len(registro)):
            registro[i].MostraReg()
    elif opcao == '3':
        print("Nasa've been hacked successfully")
        break
    else:
        print("Opção inválida")
