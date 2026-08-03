from abc import ABC, abstractmethod

class Lutador(ABC):
    @abstractmethod
    def get_lutador(self):
        pass

    @abstractmethod
    def usar_ataque(self):
        pass

class Saiyajin(Lutador):
    def __init__(self, nome, poder):
        self.nome = nome
        self.poder = poder

    def get_lutador(self):
        print(f"Lutador: {self.nome}, Poder: {self.poder}")

    def usar_ataque(self):
        print(f"{self.nome} usa um kamehameha!")
    
class Androide(Lutador):
    def __init__(self, nome, poder):
        self.nome = nome
        self.poder = poder

    def get_lutador(self):
        print(f"Lutador: {self.nome}, Poder: {self.poder}")

    def usar_ataque(self):
        print(f"{self.nome} usa uma rajada de energia!")
        
class Namekuseijin(Lutador):
    def __init__(self, nome, poder):
        self.nome = nome
        self.poder = poder

    def get_lutador(self):
        print(f"Lutador: {self.nome}, Poder: {self.poder}")

    def usar_ataque(self):
        print(f"{self.nome} usa um mankeikonsappo!")

def main():
    # os nomes não estejam vazios e que o nível de
    # poder seja um valor numérico positivo.            
    torneio = []
    racas = ["Saiyajin", "Androide", "Namekuseijin"]

    while True:
        print("===Torneio Dragon Ball===")
        print("1 - Cadastrar Lutador")
        print("2 - Listar Lutadores inscritos")
        print("3 - Atacar com um lutador")
        print("4 - Sair")

        opcao = input("Escolha uma opção (1-4): ")

        if opcao == "1":
            for i, raca in enumerate(racas):
                print(f"{i} - {raca}")

            escolha = input("Escolha uma raça: ")
            
            nome = input("Nome: ")
            poder = input("Poder: ")
            veiculos.append(Onibus(placa, capacidade, consumo))
            torneio.append()



        
if __name__ == "__main__":
    main()
        