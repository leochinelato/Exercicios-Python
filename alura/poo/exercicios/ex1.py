class Restaurante:
    nome = ""
    categoria = ""
    ativo = False

restaurante_praca = Restaurante()

restaurante_praca.categoria = "Italiana"
print("Restaurante Praça está Ativo.") if restaurante_praca.ativo == True else print("Restaurante Praça está Inativo.")

categoria = Restaurante.categoria

restaurante_praca.nome = "Bistrô"

restaurante_pizza = Restaurante()
restaurante_pizza.nome = "Pizza Place"
restaurante_pizza.categoria = "Fast Food"

print("É fast food.") if restaurante_pizza.categoria == "Fast Food" else print("Não é fast food.")

restaurante_pizza.ativo = True

print(f"Nome: {restaurante_praca.nome} | Categoria: {restaurante_praca.categoria}")