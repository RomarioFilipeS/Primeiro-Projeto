senha_correta = 123456
for i in range(3):
    senha_digitada = int(input(f"Digite a sua senha: "))
    if senha_digitada == senha_correta:
        print(f"Acesso permitido")
        break
else :
        print("conta bloqueada")