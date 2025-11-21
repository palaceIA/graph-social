from graphs.graph_social import GrafoSocial


def exibir_menu():
    print("\n===== MENU - GRAFO SOCIAL =====")
    print("1 - Adicionar usuário")
    print("2 - Criar amizade")
    print("3 - Mostrar grafo")
    print("4 - Sugerir amigos")
    print("5 - Distância social")
    print("6 - Componentes conexas")
    print("0 - Sair")
    print("================================")


def main():
    grafo = GrafoSocial()

    print("Bem-vindo ao Sistema Interativo de Grafo Social!")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("Encerrando o sistema. Até logo!")
            break

        elif opcao == "1":
            usuario = input("Digite o nome do usuário: ").strip().lower()
            grafo.adicionar_usuario(usuario)
            print(f"Usuário '{usuario}' adicionado com sucesso!")

        elif opcao == "2":
            usuario_a = input("Usuário 1: ").strip().lower()
            usuario_b = input("Usuário 2: ").strip().lower()

            grafo.adicionar_usuario(usuario_a)
            grafo.adicionar_usuario(usuario_b)
            grafo.adicionar_amizade(usuario_a, usuario_b)

            print(f"Amizade criada entre '{usuario_a}' e '{usuario_b}'!")

        elif opcao == "3":
            print("\n===== GRAFO SOCIAL =====")
            print(grafo)

    
        elif opcao == "4":
            usuario = input("Digite o nome do usuário: ").strip().lower()

            if not grafo.possui_vertice(usuario):
                print("Usuário não encontrado no grafo.")
                continue

            quantidade = int(input("Quantidade de sugestões: "))
            sugestoes = grafo.sugerir_amigos(usuario, quantidade)

            print(f"\n===== Sugestões de amigos para '{usuario}' =====")
            if sugestoes:
                for candidato, score in sugestoes:
                    print(f" → {candidato} (vizinhos em comum: {score})")
            else:
                print("Nenhuma sugestão encontrada.")

        elif opcao == "5":
            origem = input("Usuário de origem: ").strip().lower()
            destino = input("Usuário de destino: ").strip().lower()

            resultado = grafo.distancia_social(origem, destino)

            if resultado:
                distancia, caminho = resultado
                print(f"\nDistância: {distancia}")
                print("Caminho:", " → ".join(caminho))
            else:
                print("Não há caminho entre esses usuários.")

        elif opcao == "6":
            print("\n===== Componentes Conexas =====")
            componentes = grafo.componentes_conexas()
            for indice, componente in enumerate(componentes, start=1):
                print(f"Componente {indice}: {sorted(componente)}")

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
