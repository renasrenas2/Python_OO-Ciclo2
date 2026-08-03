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
        print("\n===Torneio Dragon Ball===\n")
        print("1 - Cadastrar Lutador")
        print("2 - Listar Lutadores inscritos")
        print("3 - Atacar com um lutador")
        print("4 - Sair")

        opcao = input("\nEscolha uma opção (1-4): ")

        if opcao == "1":
            print()
            for i, raca in enumerate(racas):
                print(f"{i+1} - {raca}")
            print()

            escolha = int(input("Escolha uma raça (1-3): "))

            if escolha == 1:
                nome = input("Nome: ")
                poder = input("Poder: ")
                torneio.append(Saiyajin(nome, poder))
                print("Lutador adicionado com sucesso!")

            elif escolha == 2:
                nome = input("Nome: ")
                poder = input("Poder: ")
                torneio.append(Androide(nome, poder))
                print("Lutador adicionado com sucesso!")

            elif escolha == 3:
                nome = input("Nome: ")
                poder = input("Poder: ")
                torneio.append(Namekuseijin(nome, poder))
                print("Lutador adicionado com sucesso!")
        
        elif opcao == "2":
            print("\n===Lista de lutadores inscritos===\n")
            for l in torneio:
                print(f"Nome: {nome} - Poder: {poder}")
            print()
        
        elif opcao == "3":
            for i, l in enumerate(torneio):
                print(f"{i+1} - {l}")
            print()
            
            lutador = int(input("Escolha um lutador: "))

            lutador.usar_ataque()
        
        elif opcao == "4":
            print("Encerrando torneio...")
            break
        
        else:
            print("Opção inválida! Digite novamente.")

if __name__ == "__main__":
    main()
        