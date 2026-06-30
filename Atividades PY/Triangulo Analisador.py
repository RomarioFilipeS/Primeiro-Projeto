retaA = float(input("Reta A: "))
retaB = float(input("Reta B: "))
retaC = float(input("Reta C: "))
if retaA + retaB < retaC or retaA + retaC < retaB or retaB +retaC < retaA:
    print("Triangulo Inválido")
else:
