aluno = list()
alunos = list()
for c in range(int(input("Digite a quantidade de alunos: "))):
    aluno.append(str(input(f"Digite o nome do {c+1}° aluno: ").strip()))
    aluno.append(float(input(f"Digite a primeira nota do aluno {aluno[0]}: ")))
    aluno.append(float(input(f"Digite a segunda nota do aluno {aluno[0]}: ")))
    alunos.append(aluno[:])
    aluno.clear()
    print("=" * 40)
    print("ALUNO CADASTRADO".center(40))
    print("=" * 40)
for pos, a in enumerate(alunos):
    print(f"[{pos}] {a[0]} -> Média: {(a[1]+a[2])/2}")
indiceALuno = int(input("Qual aluno deseja ver a nota? Digite o número dele: "))
print(
    f"Aluno: {alunos[indiceALuno][0]}, Nota1: {alunos[indiceALuno][1]}, Nota2: {alunos[indiceALuno][2]}"
)
