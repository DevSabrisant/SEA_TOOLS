import csv
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
import calendar

'''data_hoje = datetime.strptime(Data_Solicitacao, "%Y-%m-%d").date() if (Data_Solicitacao != "") and (Data_Solicitacao != None) else date.today()
    Data_SolicitacaoBr = data_hoje.strftime("%d-%m-%Y")'''


def Calculo_negociacao(campos_adicionais):
    data_hoje = datetime.now().date()

    r = []
    total_a_cobrar = 0
    cobrar_index = 5

    for i in range(0, len(campos_adicionais), 2):
        data_str = campos_adicionais[i]
        valor = float((campos_adicionais[i + 1]).replace(",","."))

        data_hoje = datetime.combine(data_hoje, datetime.min.time())

        data_html = datetime.strptime(data_str, "%Y-%m-%d")
        data_htmlbr = data_html.strftime("%d/%m/%Y")

        dias = ((data_hoje - data_html).days)

        if dias < 0:
            continue

        multa = round(valor * 0.02,2)
        juros = round(valor * 0.00033 * dias,2)
        cobrar = round(valor + multa + juros,2)

        r.append(data_htmlbr)
        r.append(valor)
        r.append(dias)
        r.append(multa)
        r.append(juros)
        r.append(cobrar)
        total_a_cobrar = total_a_cobrar + cobrar

    r.append(str(round(total_a_cobrar / 3,2)).replace(".", ","))
    r.append(str(round(total_a_cobrar / 2,2)).replace(".", ","))
    r.append(str(round(float(total_a_cobrar),2)).replace(".", ","))

    return r












