Saldoahorros = 1000
Saldocorriente = 800
Saldocdt = 0

def EstadoAhorros():
    return (Saldoahorros*0.006)+Saldoahorros

def EstadoCorriente():
    return Saldocorriente

def EstadoCDT():
    return Saldocdt

def inversioncdt():
    global Saldocdt
    montoinvertir= int(input("Cuánto desea invertir en su CDT? (Ej: 5000): "))
    interes = float(input("Cual es el interés mensual: "))
    meses = int(input("Ingrese los meses: "))
    Saldocdt = montoinvertir*(1.0+(interes/100))**meses
    return Saldocdt

def cerrarcdt():
    global Saldocorriente, Saldocdt
    Saldocorriente = Saldocdt + Saldocorriente
    Saldocdt = 0
    return "Cerrado!"

def ConsignarCorriente():
    global Saldocorriente
    mcc = float(input("Ingrese el monto a consignar en su cuenta corriente: "))
    Saldocorriente = Saldocorriente + mcc
    return Saldocorriente

def RetirarCorriente():
    mrc= float(input("Ingrese el monto a retirar: "))
    Saldocorriente = Saldocorriente - mrc
    return Saldocorriente

def ConsignarAhorros():
    global Saldoahorros
    mca = float(input("Ingrese un monto a consignar en su cuenta de ahorros: "))
    Saldoahorros= Saldoahorros + mca
    return Saldoahorros

def RetirarAhorros():
    mra = float(input("Cuánto dinero desea retirar: "))
    Saldoahorros = Saldoahorros - mra
    return Saldoahorros

def Terminar():
    return exit()