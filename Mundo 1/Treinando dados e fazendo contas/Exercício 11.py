larguraParede = float(input("Digite a largura da sua parede (m): "))
alturaParede = float(input("Digite a altura da sua parede (m): "))

areaParede = larguraParede * alturaParede # m2

quantTinta = areaParede / 2

print("A sua parede tem {} metros de altura e {} de largura".format(alturaParede,larguraParede))
print("Sendo assim ela possui área de {}m²".format(areaParede))

if areaParede > 1:
    print("Para pintar a sua parede serão necessários {} litros de tinta".format(quantTinta))
else:
    print("Para pintar a sua parede será necessário {} litro de tinta".format(quantTinta))