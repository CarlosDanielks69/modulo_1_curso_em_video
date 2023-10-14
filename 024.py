cidade = input("Em qual cidade você nasceu? ")
cidade = cidade.lower().split()
if "santo" in cidade:
    print("True")
else:
    print("False")
