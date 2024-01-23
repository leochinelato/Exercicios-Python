from modelos.eletronicos import Eletronico

eletronico_celular = Eletronico("iPhone 15", "Celular")

eletronico_celular.alternar_estado()
# academia_smart.receber_avaliacao("Leo",5)
# academia_smart.receber_avaliacao("Luan",4)
# academia_smart.receber_avaliacao("Joao",6)


def main():
    Eletronico.listar_eletronicos()


if __name__ == "__main__":
    main()
