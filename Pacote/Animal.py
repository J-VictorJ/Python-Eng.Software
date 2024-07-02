from abc import ABC, abstractmethod

# Classe abstrata somente a capa


class Animal(ABC):
    @abstractmethod
    def fazer_som(self):
        pass

# Classes herdadas da classe Animal onde agora eu uso o "fazer_som()"


class Cachorro(Animal):
    def fazer_som(self):
        return "Au Au"


class Gato(Animal):
    def fazer_som(self):
        return "Monday left me broken"


cachorro = Cachorro()
gato = Gato()

print(gato.fazer_som())
print(cachorro.fazer_som())

