import math

#n1 = float(input("Comprimento do cateto oposto: "))
#n2 = float(input("Comprimento do cateto adjacente: "))
#n3 = math.pow(n1,2)
#n2 = math.pow(n2,2)
#n3 = math.sqrt(n1 + n2)
#print(f"A hipotenusa vai medir {n3:.2f}")

n1 = float(input("Comprimento do cateto oposto: "))
n2 = float(input("Comprimento do cateto adjacente: "))

n3 = math.hypot(n1, n2)

print(f"A hipotenusa vau medir {n3:.2f}")
