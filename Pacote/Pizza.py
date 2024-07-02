class Pizza:
    def preparare(self):
        pass

    def cuocere(self):
        pass

    def tagliare(self):
        pass

    def inscatolare(self):
        pass


class Napolitana(Pizza):  # Na Itália se chama somente "Pizza"
    def preparare(self):
        print("Preparazione della Pizza ")

    def cuocere(self):
        print("Cucinando la Pizza")

    def tagliare(self):
        print("Tagliando la Pizza")

    def inscatolare(self):
        print("Inscatolando la Pizza")


class Margherita(Pizza):
    def preparare(self):
        print("Preparazione della Pizza Margherita")

    def cuocere(self):
        print("Cucinando la Pizza Margherita")

    def tagliare(self):
        print("Tagliando la Pizza Margherita")

    def inscatolare(self):
        print("Inscatolando la Pizza Margherita")


class Pizzeria:
    def criar_pizza(self, tipo_pizza):
        if tipo_pizza == "Napolitana":
            return Napolitana()
        elif tipo_pizza == "Margherita":
            return Margherita()
        else:
            raise ValueError("We don't speak americano")


fabrica = Pizzeria()

pizza1 = fabrica.criar_pizza("Napolitana")
pizza1.preparare()
pizza1.cuocere()
pizza1.tagliare()
pizza1.inscatolare()

print()
pizza2 = fabrica.criar_pizza("Margherita")
pizza2.preparare()
pizza2.cuocere()
pizza2.tagliare()
pizza2.inscatolare()

