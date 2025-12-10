"""
arquivo: main.py
----------------
Arquivo principal que executa o sistema.

Responsável por:

• Criar e armazenar vários campi
• Permitir selecionar um campus para gerenciar seus cursos
• Exibir menus interativos
• Encaminhar ações para as classes do pacote campus_lista

Funciona como ponto de entrada do programa.
"""

from campus_lista.campus_lista import CampusLista

def menu():
    print("\n====== Sistema UFC ======")
    print("1 - Criar Campus")
    print("2 - Selecionar Campus")
    print("3 - Listar Campi")
    print("0 - Sair")
    return input("Escolha: ")

def menu_campus(campus):
    while True:
        print(f"\n--- Campus: {campus.nome} ---")
        print("1 - Cadastrar curso")
        print("2 - Listar cursos")
        print("3 - Atualizar curso")
        print("4 - Remover curso")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome do curso: ")
            ch = int(input("Carga horária: "))
            campus.cadastrar_curso(nome, ch)

        elif opcao == "2":
            campus.listar_cursos()

        elif opcao == "3":
            codigo = int(input("Código do curso: "))
            novo_nome = input("Novo nome (ou ENTER p/ manter): ")
            nova_ch = input("Nova CH (ou ENTER p/ manter): ")

            campus.atualizar_curso(
                codigo,
                novo_nome if novo_nome else None,
                int(nova_ch) if nova_ch else None
            )

        elif opcao == "4":
            codigo = int(input("Código do curso a remover: "))
            campus.remover_curso(codigo)

        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

def main():
    # Campus e cursos pré-definidos
    campi = []
    
    # Campus Itapajé
    campus_itapaje = CampusLista("Itapajé")
    campus_itapaje.cadastrar_curso("Analise e Desenvolvimento de Sistemas", 3200)
    campus_itapaje.cadastrar_curso("Ciências de Dados", 2800)
    campus_itapaje.cadastrar_curso("Segurança da Informação", 2400)
    campi.append(campus_itapaje)
    
    # Campus Pici
    campus_pici = CampusLista("Pici")
    campus_pici.cadastrar_curso("Ciências da Computação", 3200)
    campus_pici.cadastrar_curso("Matemática", 2880)
    campus_pici.cadastrar_curso("Sistemas e Mídias Digitais", 2880)
    campi.append(campus_pici)
    
    print("Sistema iniciado com 2 campi e cursos já cadastrados!\n")
    while True:
        opcao = menu()

        if opcao == "1":
            nome = input("Nome do novo campus: ")
            campus = CampusLista(nome)
            campi.append(campus)
            print(f"Campus '{nome}' criado com sucesso!")

        elif opcao == "2":
            if not campi:
                print("Nenhum campus cadastrado.")
                continue

            for i, c in enumerate(campi):
                print(f"{i+1} - {c.nome}")

            escolha = int(input("Escolha o campus: ")) - 1

            if 0 <= escolha < len(campi):
                menu_campus(campi[escolha])
            else:
                print("Campus inválido.")

        elif opcao == "3":
            if not campi:
                print("Nenhum campus cadastrado.")
            else:
                for c in campi:
                    print(c)

        elif opcao == "0":
            print("Encerrando...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
