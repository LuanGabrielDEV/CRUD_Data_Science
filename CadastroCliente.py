from itertools import count

contatos = [
    {"id": 1,
    "nome": "Reginaldo",
    "telefone": "9999-9999",
    "email": "reginaldo@email.com"
    },
    {"id": 2,
     "nome": "Brena",
     "telefone": "8888-8888",
     "email": "brena@email.com"
     }
]

# Gerador de IDs automáticos
id_generator = count(start=max(c["id"] for c in contatos) + 1 if contatos else 1)

while True:
    menuPrincipal = input("""
------- MENU PRINCIPAL -------
1 - Cadastrar contato
2 - Listar contatos
3 - Atualizar contato
4 - Excluir contato
5 - Sair
Opção: """)

    #--------------------------------------
    # CADASTRAR CONTATOS
    if menuPrincipal == "1":
        novo_id = next(id_generator)
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("Email: ")

        contatos.append({
            "id": novo_id,
            "nome": nome,
            "telefone": telefone,
            "email": email
        })

        print("Contato adicionado com sucesso!\n")

    # --------------------------------------
    # LISTAR CONTATOS
    elif menuPrincipal == "2":
        for c in contatos:
            print(f"ID: {c['id']} - Nome: {c['nome']} - Tel: {c['telefone']} - Email: {c['email']}\n")

    # --------------------------------------
    # ATUALIZAR CONTATOS
    elif menuPrincipal == "3":
        try:
            id_contato = int(input("Digite o ID do contato que deseja alterar: "))
            # Encontra o contato pelo ID
            contato = next((c for c in contatos if c["id"] == id_contato), None)

            if not contato:
                print("Contato não encontrado!\n")
                continue  # Volta ao menu principal

            while True:
                opcao = input("""Qual dado você deseja alterar? 
            1 - Nome
            2 - Telefone
            3 - Email
            4 - Todos os dados
            5 - Voltar ao menu principal
            Opção: """)

                if opcao == "1":
                    contato["nome"] = input("Novo Nome: ")
                    print("Nome atualizado com sucesso!\n")
                    break

                elif opcao == "2":
                    contato["telefone"] = input("Novo Telefone: ")
                    print("Telefone atualizado com sucesso!\n")
                    break

                elif opcao == "3":
                    contato["email"] = input("Novo Email: ")
                    print("Email atualizado com sucesso!\n")
                    break

                elif opcao == "4":
                    contato.update({
                        "nome": input("Novo Nome: "),
                        "telefone": input("Novo Telefone: "),
                        "email": input("Novo Email: ")
                    })
                    print("Todos os dados atualizados com sucesso!\n")
                    break

                elif opcao == "5":
                    print("Voltando ao menu principal...\n")
                    break

                else:
                    print("Opção inválida. Tente novamente.\n")

        except ValueError:
            print("Erro: O ID deve ser um número inteiro!\n")

    #--------------------------------------
    # EXCLUIR CONTATOS
    elif menuPrincipal == "4":
        try:
            id_excluir = int(input("Digite o ID do contato que deseja excluir: "))
            contato = next((c for c in contatos if c["id"] == id_excluir), None)

            if contato:
                contatos.remove(contato)
                print(f"Contato ID {id_excluir} excluído com sucesso!\n")
            else:
                print(f"Contato ID {id_excluir} não encontrado.\n")

        except ValueError:
            print("Erro: O ID deve ser um número inteiro!\n")

    # --------------------------------------
    # SAIR
    elif menuPrincipal == "5":
        print("\nSaindo do sistema...")
        print("Obrigado por usar nosso gerenciador de contatos!")
        break  # This will exit the main program loop

    else:
        print("\nOpção inválida! Por favor, digite um número entre 1 e 5.\n")