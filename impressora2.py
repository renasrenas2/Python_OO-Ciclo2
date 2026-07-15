# criar novo documento
# imprimir documento
# listar documentos
class Documento:
    def __init__(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo
        self.documentos = []
    
    def criar_documento(self, titulo, conteudo):
        d = Documento(titulo, conteudo)
        self.documentos.append(d)
        return d

    def listar_documentos(self):
        print("\nLista de documentos: ")
        for i, documento in enumerate (self.documentos):
            print(f"{i+1} - {documento}")
        print()
        
class Impressora:
    def imprimir(self, titulo, conteudo):
        print(f"Exibindo informações do documento: {titulo}")
        print(f"{conteudo}")


def main():
    while True:
        print("\n===MENU IMPRESSORA===\n")
        print("1 - Criar Novo Documento")
        print("2 - Imprimir documento")
        print("3 - Listar Documentos")
        print("4 - Sair\n")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("\nTítulo do Documento: ")
            conteudo = input("\nConteúdo do Documento: ")
            d = Documento(titulo, conteudo)
            d.criar_documento()

        elif opcao == "2":
            d.imprimir()

        elif opcao == "3":
            d.listar_documentos()

        elif opcao == "4":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida! Digite novamente.")
        
    
if __name__ == "__main__":
    main()