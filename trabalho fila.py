lass Fila:
    def _init_(self):
        self.__fila = []

    def inserir(self, item):
        self.__fila.append(item)
        print(f"Inserido: {item}")

    def remover(self):
        if not self.esta_vazia():
            removido = self.__fila.pop(0)
            print(f"Removido: {removido}")
        else:
            print("Fila vazia! Nada para remover.")


    def atualizar(self, nome, novo):
        for i, item in enumerate(self.__fila):
            dados = item.split(",")
            if dados[0].strip().lower() == nome.lower():
                self.__fila[i] = novo
                print(f"Atualizado: {nome} → {novo}")
                return
        print(f"Estudante '{nome}' não encontrado.")


fila_estudantes = Fila()

while True:
    print("\n===== SISTEMA DE GESTÃO DA FILA =====")
    print("1 - Inserir Pessoa")
    print("2 - Remover Pessoa")
    print("3 - Atualizar Registro")
    print("4 - Mostrar Fila")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome: ")
        idade = input("Digite a idade: ")
        data = input("Digite a data de cadastro: ")
        registro = f"{nome}, IDADE:{idade}, DATA:{data}"
        fila_estudantes.inserir(registro)

    elif opcao == "2":
        fila_estudantes.remover()

    
    elif opcao == "3":
        nome = input("Digite o nome que deseja atualizar: ")
        novo_nome = input("Novo nome: ")
        nova_idade = input("Nova idade: ")
        nova_data = input("Nova data: ")
        novo_registro = f"{novo_nome}, IDADE:{nova_idade}, DATA:{nova_data}"
        fila_estudantes.atualizar(nome, novo_registro)

    elif opcao == "4":
        print("\n*** LISTA ATUAL ***")
        print(fila_estudantes)

    elif opcao == "0":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida! Tente novamente.")
