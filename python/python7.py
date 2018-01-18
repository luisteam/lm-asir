import math

C = int(input("Dime el dinerito:"))
x = int(input("Tipo de interes:"))
n = int(input("En cuantos años:"))

Cn = C * (1 + x/100) ** n

print("Vas a pagar %d" % Cn)
