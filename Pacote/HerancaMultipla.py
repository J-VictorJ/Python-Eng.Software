# Herança múltipla
class Pai:
    def metodo_pai(self):
        print("Classe Pai")


class Mae:
    def metodo_mae(self):
        print("Não é a mamãe")


class Filho(Pai, Mae):
    pass


filho = Filho()
print(filho.metodo_mae())
print(filho.metodo_pai())

# A classe Filho herda as classes Pai e Mae
