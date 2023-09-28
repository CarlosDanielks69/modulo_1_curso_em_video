salario = float(input("Qual o salario do funcionario? R$ "))
aumento = float(input("Qual a porcentagem de aumento do salario?"))
print(f"Um funcionario que ganhava R${salario}, com {aumento}% de aumento, passa a receber R${(salario*aumento/100)+salario:.2f}")
