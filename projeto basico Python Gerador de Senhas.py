import random

senha = ""

caracteres = "agkelsitwqrx12986!$#@*&çn05d"

for digito in range(8):
    aleatorio = random.choice(caracteres)
    senha += aleatorio

print("-" * 20)
print("senha")
print("-" * 20)

