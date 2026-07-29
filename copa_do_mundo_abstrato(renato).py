from abc import ABC, abstractmethod

class ClubeParticipante(ABC):
    def __init__(self, nome, pais, confederacao, ranking_fifa, gols_marcados, vitorias):
        self.nome = nome
        self.pais = pais
        self.confederacao = confederacao
        self.ranking_fifa = ranking_fifa
        self.gols_marcados = gols_marcados
        self.vitorias = vitorias

    def exibir_dados(nome, pais, confederacao):
        print("\nDados do clube:\n")
        print(f"Nome: {nome}")
        print(f"País: {pais}")
        print(f"Confederação: {confederacao}")

    @abstractmethod
    def calcular_desempenho_uefa(gols_marcados, vitorias):
        desempenho = vitorias * 3 + gols_marcados * 0.5

    @abstractmethod
    def calcular_desempenho_conmebol(gols_marcados, vitorias):
            desempenho = vitorias * 3 + gols_marcados * 0.7

    #def gerar_relatorio_tecnico()

def main():
    pass
if __name__ == "__main__":
    main()
                