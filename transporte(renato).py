from abc import ABC, abstractmethod

class VeiculoTransporte(ABC):
    def __init__(self, placa, capacidadePassageiros):
        self.placa = placa
        self.capacidadePassageiros = capacidadePassageiros

    @abstractmethod
    def calcularCustoOperacional(self): # retorna o custo por quilômetro
        pass

class Onibus(VeiculoTransporte):
    def __init__(self, placa, capacidadePassageiros, consumoPorKm): # (litros/km)
        super().__init__(placa, capacidadePassageiros)
        self.consumoPorKm = consumoPorKm

    # R$ 6,00 por litro de diesel 
    # R$ 0,80 por kWh
    def calcularCustoOperacional(self): 
        return self.consumoPorKm * 6
    
class Metro(VeiculoTransporte):
    def __init__(self, placa, capacidadePassageiros, consumoEnergiaPorKm): # (kWh/km)
        super().__init__(placa, capacidadePassageiros)
        self.consumoEnergiaPorKm = consumoEnergiaPorKm

    def calcularCustoOperacional(self): 
        return self.consumoEnergiaPorKm * 0.80

def main():
    while True:
        print("\n===Sistema Gerenciador de Veículos===\n")
        print("1 - Adicionar um ônibus")
        print("2 - Adicionar um Metrô")
        print("3 - Sair")

        opcao = input("\nEscolha uma opção (1-3): ")

        if opcao == "3":
            print("\nSaindo do sistema. Até logo!\n")
            break
        
        if opcao not in ["1", "2", "3"]:
            print("\nOpção inválida. Por favor, escolha entre 1 e 3.\n")
            continue
        try: 
            if opcao == "1":
                placa = input("Digite a placa do ônibus: ")
                capacidadePassageiros = input("Digite a capacidade do ônibus: ")
                consumoPorKm = input("Digite o consumo por km do ônibus: ")

                onibus = Onibus(placa, capacidadePassageiros, consumoPorKm)

            elif opcao == "2":
                placa = input("Digite a placa do metrô: ")
                capacidadePassageiros = input("Digite a capacidade do metrô: ")
                consumoEnergiaPorKm = input("Digite o consumo por kWh do metrô: ")
            
                metro = Metro(placa, capacidadePassageiros, consumoEnergiaPorKm)
        # placa não pode
        # ser vazia, e os valores numéricos devem ser positivos.
        except :
            pass

