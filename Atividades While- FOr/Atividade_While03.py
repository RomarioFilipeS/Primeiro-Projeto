import time

while True:
    opçao = int(input( """MENU
    1 - Somar
    2- subtrair
    3- multiplicar
    4- dividir
    5- sair
Digite sua opçao:"""))
    if opçao == 1:
        print("Somar")
    elif opçao == 2:
        print("Subtrair")
    elif opçao == 3:
        print("Multiplicar")
    elif opçao == 4:
        print("dividir")
    elif opçao == 5:
        print("Saindo")
        time.sleep(1)
        break
    else:
        print("Opçao Invalida")
