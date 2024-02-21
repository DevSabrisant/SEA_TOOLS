import numpy as np

# Supondo que as funções plan1, plan2, etc., estejam definidas ou importadas
def plan1():
    return 110

def plan2():
    return 150

# Variáveis de entrada
Plano = 1
D = 2
M = 180

# Cálculo usando NumPy
Valor_dia = (globals()[f"plan{Plano}"]() / 30)
d =  float(Valor_dia * D)
m =  float((Valor_dia / 1440) * M)
Valor_Desc = d + m
Valor_Total = round((globals()[f"plan{Plano}"]() - Valor_Desc),2)


print(f"Valor_dia: {Valor_dia}")
print(f"Valor_Desc: {Valor_Desc}")
print(f"Valor_Total: {Valor_Total}")
