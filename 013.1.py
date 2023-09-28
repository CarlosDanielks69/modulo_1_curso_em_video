compra = float(input("Valor da compra? R$"))
desconto = float(input("Desconto em %: "))
print(f"Valor da compra parcelado é R${compra}, a vista com {desconto}% de desconto é R${compra-(compra*desconto/100)}")
