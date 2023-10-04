from math import trunc
n = float(input("Digite um numero: "))

print(f"O numero {n} tem a parte inteira {trunc(n)}")

#ou

n = float(input("Digite um numero: "))

print(f"O numero {n} tem a parte inteira {n:.0f}")

#ou

n = float(input("Digite um numero: "))

print(f"O numero {n} tem a perte inteira {int(n)}")
