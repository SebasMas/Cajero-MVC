import logicaFunciones as logica



menu = """
1) Saldo Cuenta de Ahorros
2) Saldo Cuenta Corriente
3) Saldo CDT
4) Invertir CDT
5) Cerrar CDT
6) Consignar Cuenta Corriente
7) Retirar Cuenta Corriente
8) Consignar Ahorros
9) Retirar ahorros
10) Avanzar un mes
11) Salir
"""

print(" ")
print(" ")
print(menu)




continuar = True
while continuar:
    option = int(input("Ingrese una opción: "))
    if option == 1:
        print(logica.EstadoAhorros())
    elif option == 2:
        print(logica.EstadoCorriente())
    elif option == 3:
        print(logica.EstadoCDT())
    elif option == 4:
        print(logica.inversioncdt())
    elif option == 5:
        print(logica.cerrarcdt())
    elif option == 6:
        print(logica.ConsignarCorriente())
    elif option == 7:
        print(logica.RetirarCorriente())
    elif option == 8:
        print(logica.ConsignarAhorros())
    elif option == 9:
        print(logica.RetirarAhorros())
    elif option == 11:
        logica.Terminar
        
