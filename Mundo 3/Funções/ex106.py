C = {
    "default": "\033[m",
    "branco": "\033[7m",
    "vermelho": "\033[41m",
    "verde": "\033[42m",
    "azul": "\033[44m",
}


def ajuda(com):
    titulo(f"Acessando o manual do comando '\{com}\'", "branco")
    help(com)


def titulo(msg, cor="default"):
    tam = len(msg)
    print(C[cor], end="")
    print("=" * tam)
    print(msg)
    print("=" * tam)
    print(C["default"], end="")


titulo("SISTEMA DE AJUDA PYHELP", "vermelho")
comando = str(input("Função ou biblioteca> ")).strip()
while True:
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
titulo("ATÉ LOGO", "azul")