
a = input("Digite Algo: ")
print(f"O tipo primitivo desse valor é:{type(a)}")
print(f"Só possui espaços:{a.isspace()}")
print(f"É um numero:{a.isnumeric()}")
print(f"É alfabetico:{a.isalpha()}")
print(f"É alfanumerico:{a.isalnum()}")
print(f"Esta em maiusculas:{a.islower()}")
print(f"Esta em minuscula:{a.isupper()}")
print(f"Esta capitalizada:{a.istitle()}")