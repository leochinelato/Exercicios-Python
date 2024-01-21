print("Esse programa converte metros em centímetros e milimetros")

metros = int(input("Para converter, primeiro digite os metros que deseja realizar a conversão: "))

print("A conversão está pronta: ")
print("Metros: {}".format(metros))
print("Centímetros: {}".format( (metros*100) ))
print("Milimetros: {}".format( (metros*1000) ))