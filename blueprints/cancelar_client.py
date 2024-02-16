from datetime import date, datetime
import calendar
#
def Calculo_cancelamento(pAtual, pVen, Data_Solicitacao,data_ati):

    data_hoje = datetime.strptime(Data_Solicitacao, "%Y-%m-%d").date() if (Data_Solicitacao != "") and (Data_Solicitacao != None) else date.today()
    Data_SolicitacaoBr = data_hoje.strftime("%d-%m-%Y")

    #Ant_IniVenc = date(data_hoje.year - 1 if data_hoje.month == 1 else data_hoje.year, data_hoje.month - 1 if data_hoje.month != 1 else 12, 1)
    #Ant_IniVencBr = Ant_IniVenc.strftime("%d/%m/%Y")
    #Atu_FinalVenc = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, data_hoje.month, quantidade_dias)
    #Atu_FinalVencBr = Atu_FinalVenc.strftime("%d/%m/%Y")

    #IniVenc = date(data_hoje.year, data_hoje.month, 1)
    #IniVencBr = IniVenc01.strftime("%d/%m/%Y")
    #FinalVenc = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, ProxAtual, Prox_quantidade_dias)
    #FinalVencBr = FinalVenc.strftime("%d/%m/%Y")

    Ant_quantidade_dias = calendar.monthrange(data_hoje.year - 1 if data_hoje.month == 1 else data_hoje.year, data_hoje.month - 1 if data_hoje.month != 1 else 12)[1]

    quantidade_dias = calendar.monthrange(data_hoje.year, data_hoje.month)[1]

    DadosVen = [
        (11, 10) if pVen == "15"
        else (11, 10) if pVen == "20"
        else (21, 20) if pVen == "25"
        else (21, 20) if pVen == "30"
        else None]


    if data_hoje <= DadosVen[1]:
        r = f""
        return r
    else:
        r = f""
        return r

    r = f"Data Simulada: {Data_SolicitacaoBr}\nVencimento: {pVen}\nPlano: {pAtual}\n\n"
    return r