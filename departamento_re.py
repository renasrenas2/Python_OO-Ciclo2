def criar_departamento(departamentos, nome):
    departamento = Departamento(nome)
    departamentos.append(departamento)
    return departamento

class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionarios(self, funcionario):
        self.funcionarios.append(funcionario)
    
    def calcular_media_salarial(self):
        for funcionario in self.funcionarios:


    def listar_funcionarios(self):
        if not self.funcionarios:
            print("Não há nenhum funcionário nesse departamento ainda.")
        else:
            print(f"Funcionários do departamento {self.nome}")
            for i, funcionario in enumerate(self.funcionarios):
                print(f"{i + 1} - {funcionario}")
            print()

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

def main():
    departamentos = []
    funcionarios = []

    while True:
        print("\n===MENU===")
        print("1 - Criar departamento")
        print("2 - Criar funcionário")
        print("3 - Adicionar um funcionário a um departamento")
        print("4 - Listar funcionários")
        print("5 - Mostrar a média salarial de funcionários de um departamento")
        print("6 - Sair")

        opcao = input("Escolha uma opção (1-6): ")

        if opcao == "1":
            nome = input("Digite o nome do departamento: ")
            criar_departamento(departamentos, nome)
            print("Departamento criado com sucesso!")

        elif opcao == "2":
            nome = input("Digite o nome do funcionário: ")
            salario = input("Digite o salário do funcionário: ")
            func = Funcionario(nome, salario)
            funcionarios.append(func)
            print("Funcionário adicionado com sucesso!")

        elif opcao == "3":  
                




if __name__ == "__main__":
    main()