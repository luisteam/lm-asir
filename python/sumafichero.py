with open("suma.txt","r") as f:
	operaciones=f.readlines()

for operacion in operaciones:
	if "+" in operacion:
		operandos=operacion.split("+")
		operandos=list(map(int,operandos))
		resultados.append(str(operandos[0]+operandos[1])+"\n")
for operacion in operaciones:
	if "-" in operacion:
		operandos=operacion.split("-")
		operandos=list(map(int,operandos))
		resultados.append(str(operandos[0]-operandos[1])+"\n")

with open("resultados.txt","w") as f:
	f.writelines(resultados)