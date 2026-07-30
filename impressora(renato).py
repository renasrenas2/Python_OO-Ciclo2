class Impressora:
    def imprimir(self, documento):
        print("\n---Imprimindo Documento---\n")
        print(f"{documento.titulo}")
        print(f"\n{documento.conteudo}")

class Documento:
    def __init__(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo

def main():
    documentos = []
    impressora = Impressora()
    print("\nBem-Vindo ao Super Sistema de Impressão\n")

    while True:
        print("Me diga o que você deseja agora: \n")
        print("A - Quero Imprimir um Documento")
        print("B - Quero Adicionar um Documento")
        print("C - Finalizar\n")
        escolha = input("Digite qual a sua opção: ")

        if escolha == "A" or escolha == "a":
            if not documentos:
                print("\nPara imprimir você precisa ter pelo menos um documento adicionado.\n")
            else:
                print("\nDocumentos disponíveis para impressão:\n")

                for i, doc in enumerate(documentos):
                    print(f"{i + 1}. {titulo}")
                print()

                opcao = int(input("Digite o número do documento que vocÊ deseja imprimir: "))
                
                impressora.imprimir(documentos[opcao - 1])

        elif escolha == "B" or escolha == "b":
            titulo = input("\nDigite o título do seu documento: ")
            conteudo = input("Digite o conteúdo do seu documento: ")
            d = Documento(titulo, conteudo)
            documentos.append(d)
            print("\nSeu documento foi criado com sucesso!\n")


        elif escolha == "C" or escolha == "c":
            print("Saindo do programa...")
            break
        else:
            print("\nOpção Inválida!\n")

if __name__ == "__main__":
    main()