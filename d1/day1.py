# Criar um programa que lê varias linhas de input,
# e cria um inteiro de dois digitos usando o primeiro e o ultimo número que aparecem. se só exisir um número repete ele.
def checagem(puzzle: str):
    aux = []
    for i in puzzle:
        if i.isnumeric():
            aux.append(i)
    if len(aux) == 1:
        res = aux[0] + aux[0]
        return int(res)
    else:
        res = aux[0] + aux[-1]
        return int(res)


input_file = open("input.txt", "r")
input_lines = input_file.readlines()

aux = []

for i in input_lines:
    aux.append(checagem(i))

resultado = sum(aux)
print(resultado)
