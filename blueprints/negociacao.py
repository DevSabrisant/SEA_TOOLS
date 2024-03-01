import csv
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
import calendar
from blueprints.planos import *

def Calculo_negociacao(pAtual, Data_Solicitacao):
    data_hoje = datetime.strptime(Data_Solicitacao, "%Y-%m-%d").date() if (Data_Solicitacao != "") and (Data_Solicitacao != None) else date.today()
    Data_SolicitacaoBr = data_hoje.strftime("%d-%m-%Y")
    
    
    plano_atual = (globals()[f"plan{pAtual}"]())
    
    data_calc = date.today() - data_hoje
        
    ProxAtual = (data_hoje.month % 12) + 1
    
    multa  = plano_atual * 0.02 
    
    juros = plano_atual * 0.00033 * data_calc.days
    
    valor_total = plano_atual + multa + juros
    
    r = f"Data Simulada:{Data_SolicitacaoBr}\nPlano Atual:{plano_atual}\nResultado:{valor_total:.2f} "

    with open('arquivo_dados.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['OI'])
    return r

