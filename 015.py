dias = float(input("Quantos dias alugados? "))
km = float(input("Quantos Km rodados? "))
total = dias * 60 + km * 0.15
print(f"Valor total a pagar: R${total:.2f}")
