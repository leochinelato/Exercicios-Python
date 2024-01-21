from modelos.academias import Academia

academia_smart = Academia("Smart Fit")

academia_smart.alternar_estado()
# academia_smart.receber_avaliacao("Leo",5)
# academia_smart.receber_avaliacao("Luan",4)
# academia_smart.receber_avaliacao("Joao",6)


def main():
    Academia.listar_academias()


if __name__ == "__main__":
    main()
