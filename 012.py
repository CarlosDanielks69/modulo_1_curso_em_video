
produto = float(input("Qual o valor do produto? R$"))
desconto = float(input("Qual a porcentagem? "))
print(f"O produto que custava {produto} com o desconto de {desconto} vai custar {produto - (desconto * produto)/100:.1f}")
