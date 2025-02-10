from Usuario import Usuario
from Produto import Produto

usu1 = Usuario()
prod1 = Produto()

while True:
    print("", "Bem-vindo ao servidor", "", sep="___")
    print("\nEscolha a opção")
    print("1 - Usuário")
    print("2 - Produto")
    opcao = int(input("Digite sua preferência: "))

    if opcao == 1:
        print("\n", "Você está no usuário", "", sep="___")
        print("O que gostaria de executar?")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Excluir")
        opcao_user = int(input("Digite: "))

        if opcao_user == 1:
            usu1.nome = input("\nDigite seu nome: ")
            usu1.cpf = input("Digite seu CPF: ")
            usu1.email = input("Digite seu email: ")
            usu1.senha = input("Digite sua senha: ")
            usu1.cadastrar()

        elif opcao_user == 2:
            print("\n1 - Listar todos")
            print("2 - Listar um específico")
            opcao_listar = int(input("Digite: "))

            if opcao_listar == 1:
                for i in usu1.listar():
                    print(i)

            elif opcao_listar == 2:
                chave_user = int(input("Digite a chave do usuário: "))
                print(usu1.lista_por_id(chave_user))

        elif opcao_user == 3:
            for i in usu1.listar():
                print(i)

            id = int(input("\nDigite a chave (id) que deseja atualizar: "))
            nome = input("Nome: ")
            cpf = input("CPF: ")
            email = input("Email: ")
            senha = input("Senha: ")
            atualizada_user = [id, nome, cpf, email, senha]
            usu1.atualizar(atualizada_user)

        elif opcao_user == 4:
            deletar_user = int(input("\nDigite a chave do usuário para deletar: "))
            usu1.excluir(deletar_user)

        else:
            print("Erro!. Por favor, digite o número de acordo com o menu.")

    elif opcao == 2:
        print("\n", "Você está no produto", "", sep="___")
        print("O que gostaria de executar?")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Excluir")
        opcao_produto = int(input("Digite: "))

        if opcao_produto == 1:
            prod1.nome = input("\nDigite o nome do produto: ")
            prod1.descricao = input("Digite a descrição do produto: ")
            prod1.marca = input("Digite a marca do produto: ")
            prod1.modelo = input("Digite o modelo do produto: ")
            prod1.preco = input("Digite o preço do produto: ")
            prod1.qte = input("Digite a quantidade do produto: ")
            prod1.cor = input("Digite a cor do produto: ")
            prod1.peso = input("Digite o peso do produto: ")
            prod1.cadastrar_prod()

        elif opcao_produto == 2:
            print("\n1 - Listar todos")
            print("2 - Listar um específico")
            opcao_listarprod = int(input("Digite: "))

            if opcao_listarprod == 1:
                for i in prod1.listar_prod():
                    print(i)

            elif opcao_listarprod == 2:
                chave_prod = int(input("Digite a chave do produto: "))
                print(prod1.listar_por_idprod(chave_prod))

        elif opcao_produto == 3:
            for i in prod1.listar_prod():
                print(i)

            id_prod = int(input("\nDigite a chave (id) que deseja atualizar: "))
            nome = input("Nome: ")
            descricao = input("Descrição: ")
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            preco = float(input("Preco: "))
            qte = int(input("Quantidade: "))
            cor = input("Cor: ")
            peso = input("Peso: ")
            atualizada_prod = [id_prod, nome, descricao, marca, modelo, preco, qte, cor, peso]
            prod1.atualizar_prod(atualizada_prod)

        elif opcao_produto == 4:
            deletar_prod = int(input("\nDigite a chave do produto para deletar: "))
            prod1.excluir_prod(deletar_prod)

        else:
            print("Erro!. Por favor, digite o número de acordo com o menu.")

    else:
        print("Erro!. Por favor, digite o número de acordo com o menu.")