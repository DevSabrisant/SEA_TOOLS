from blueprints.calculos import *

def venc(pVen, pAtual, pNovo, checkA):
    if checkA:
        return CalculoA(pAtual, pNovo, pVen)  # VENCIMENTO DE ANANINDEUA
    elif pVen in ["5", "10"]:
        return Calcularven1(pAtual, pNovo, pVen)  # VENCIMENTO 5 OU 10
    elif pVen in ["15", "20"]:
        return Calcularven2(pAtual, pNovo, pVen)  # VENCIMENTO 15 OU 20
    elif pVen in ["25", "30"]:
        return Calcularven3(pAtual, pNovo, pVen)  # VENCIMENTO 25 OU 30
