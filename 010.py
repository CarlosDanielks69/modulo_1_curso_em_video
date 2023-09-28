dinheiro = float(input("Quanto você tem na carteira? R$"))
dolar = float(input("Qual a cotação do Dolar? U$"))
euro = float(input("Qual a cotação do Euro? €"))
print(f"Com {dinheiro} você pode comprar U${dinheiro/dolar:.2f}\nE pode comprar €{dinheiro/euro:.2f}")
