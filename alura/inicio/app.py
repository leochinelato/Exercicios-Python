import os

habitos = []


def titulo(msg):
    """

    Essa função é utilizada para os títulos do nosso programa.
    Args:
        msg (_type_): _description_
    Outputs:
        - Limpa a tela do terminal
        - Faz uma impressão de uma mensagem centralizada com 40 "=" antes e depois

    """
    os.system("clear")
    print("=" * 40)
    print(msg.center(40))
    print("=" * 40)
    print()


def mostrar_opcoes():
    """

    Função para mostrar as opções do nosso menu.
    Outputs:
        - Opções do nosso menu de 1 a 5.

    """
    print("1. Criar hábito")
    print("2. Remover hábito")
    print("3. Ativar/Desativar Hábito")
    print("4. Listar hábitos")
    print("5. Sair\n")


def voltar_menu():
    """
    
    Função utilizada sempre que eu precisar voltar a Main, deixando o terminal mais limpo.
    
    Inputs:
        - Solicita que o usuário pressione o Enter para voltar ao menu.

    """
    input("\nPressione ENTER para voltar ao menu principal!")
    main()


def criar_habito():

    """
    
    Função de criar hábito, onde eu insiro os dados do hábito desejado.
    Inputs:
        - Nome do hábito
        - Frequência
    Outputs:
        - Adiciona um hábito a lista de hábitos
    
    """

    titulo("CADASTRO DE NOVO HÁBITO")
    nome_do_habito = input("Digite o nome do habito: ")
    freq_habito = int(input("Frequência semanal (dias): "))
    dados_habito = {"Nome": nome_do_habito, "Frequencia": freq_habito, "Ativo": False}
    habitos.append(dados_habito)
    print(f"\nHábito ({nome_do_habito}) criado com sucesso!")

    voltar_menu()


def remover_habito():

    """
    Função para remover um hábito a nossa lista de hábitos. (ainda não funciona)
    """
    habitos.pop(int(input("Digite o hábito que deseja remover: ")))
    print("Hábito removido com sucesso!")


def alternar_estado_habito():

    """
    
    Função para alternar o estado do hábito ATIVO/INATIVO

    Input:
        - Nome do hábito
    Output:
        - Altera o hábito de ativo para inativo e vice-versa

    """

    titulo("ALTERNAR ESTADO HABITO")
    nome_habito = input("Nome do hábito: ")
    habito_encontrado = False
    for habito in habitos:
        if nome_habito == habito["Nome"]:
            habito_encontrado = True
            habito["Ativo"] = not habito["Ativo"]
            mensagem = (
                f"O hábito {nome_habito} foi ativado com sucesso"
                if habito["Ativo"]
                else f"O hábito {nome_habito} foi desativado com sucesso"
            )
            print(mensagem)
    if not habito_encontrado:
        print("O Hábito não foi encontrado")
    voltar_menu()


def listar_habitos():
    """
    Função para listar os hábitos existentes na minha lista de hábitos
    """

    titulo("LISTA DE HÁBITOS")

    print("{:<12} | {:>12} | {}".format("Nome hábito","Frequência","Status"))
    for habito in habitos:
        habito_nome = habito["Nome"]
        frequencia = habito["Frequencia"]
        ativo = "Ativado" if habito["Ativo"] else "Desativado"
        print(f"{habito_nome:<12} | {frequencia:>12} | {ativo}")

    voltar_menu()


def sair_programa():
    """
    Função para sair do programa...
    """

    os.system("clear")
    print("Saindo do programa...")


def opcao_incorreta():

    """
    Função para quando digitamos a opcao incorreta e não queremos mostrar um erro na tela.
    """

    print("Opção incorreta.\n")
    input("Pressione ENTER para voltar ao menu principal!")
    main()


def escolher_opcao():
    
    """
    Função de escolha de opcão, onde o usuário irá inserir uma opção do menu.
    """

    try:
        opcao = int(input("Digite a sua opção: "))
        match opcao:
            case 1:
                criar_habito()
            case 2:
                remover_habito()
            case 3:
                alternar_estado_habito()
            case 4:
                listar_habitos()
            case 5:
                sair_programa()
            case default:
                opcao_incorreta()
    except:
        opcao_incorreta()


def main():
    titulo("HABIT TRACKER")
    mostrar_opcoes()
    escolher_opcao()


if __name__ == "__main__":
    main()
