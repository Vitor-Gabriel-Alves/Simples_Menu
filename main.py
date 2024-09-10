import os


def limpar():
    os.system("clear")


def aste():
    print("-" * 40)


def menu():
    print("[1] Cadastrar")
    aste()
    print("[2] Listar")
    aste()
    print("[3] Pesquisar")
    aste()
    print("[4] Remover pelo nome")
    aste()
    print("[5] Remover pela posição")
    aste()
    print("[6] excluir tudo")
    aste()
    print("[7] Sair")


resp = ""
nomes = []
while resp != "7":
    menu()
    resp = input("O que deseja fazer? ")
    if resp == "1":
        aste()
        print("Cadastro")
        aste()
        limpar()
        nome = input("Adicione um nome: ").upper()
        if nome.isdigit() == True:
            print("Apenas NOMES são aceitos na lista. ")
        else:
            print(f"{nome} foi cadastrado(a) \n")
            aste()
            nomes.append(nome)

    elif resp == "2":
        limpar()
        aste()
        print(f"{nomes} Há um total de, {len(nomes)} nomes na lista\n")
        aste()
    elif resp == "3":
        limpar()
        P_L = input("Qual nome deseja pesquisar na lista? ").upper()
        if P_L.isdigit() == True:
            aste()
            print(
                f"{P_L} É um número, informe o (nome) do\nusuário(a) que está procurando"
            )
            aste()
        elif P_L in nomes:
            posi = int(nomes.index(P_L)) + 1
            aste()
            print(f"{P_L} Está na lista! sua posição é de\nnúmero {[posi]}\n")
            aste()
        else:
            aste()
            print(f"{P_L} Não está na lista!\n")
            aste()
    elif resp == "4":
        limpar()
        aste()
        print("Excluir pelo nome")
        aste()
        E_L = input("Qual nome deseja excluir da lista? ").upper()
        if E_L.isdigit() == True:
            limpar()
            aste()
            print(
                "Número detectado!!! Informe o (Nome)\ndo usuário(a) que deseja remover."
            )
            aste()
        elif E_L in nomes:
            nomes.remove(E_L)
            aste()
            print(f"{E_L} Foi removido(a)!\n")
            aste()
        else:
            limpar()
            aste()
            print(
                "Por favor verifique se o nome informado\nestá na lista, você pode usar [2] para\nlistar os nomes ou [3] para pesquisar"
            )
            aste()
    elif resp == "5":
        limpar()
        aste()
        print("Remover pela posição")
        aste()
        posi = input(
            "Começando em 1, informe a posição do nome\nque deseja remover: ")
        if posi.isdigit() == False:
            limpar()
            aste()
            print("Informe a (Posição) do usuário(a) \n")
            aste()
        else:
            posi = int(posi) - 1

            if 0 <= posi < len(nomes):
                limpar()
                N_R = nomes.pop(posi)
                aste()
                print(f"{N_R} foi removido(a) \n")
                aste()
            else:
                limpar()
                aste()
                print(
                    "O usuário(a) não foi encontrado(a),\n verifique a lista! "
                )
                aste()
    elif resp == "6":
        limpar()
        aste()
        aste()
        r = input("Deseja realmente apagar toda a lista, s/n?: ").upper()
        if r == "S":
            limpar()
            aste()
            print("Lista apagada!")
            aste()
            nomes.clear()
        else:
            limpar()
            aste()
            print("Operação cancelada!")
            aste()
    elif resp == "7":
        limpar()
        print("Até a próxima vez, Adeus!")
        break
    else:
        limpar()
        aste()
        print(
            "Erro detectado! Por favor escolha o NÚMERO correspondente à opção desejada.\n"
        )
        aste()
