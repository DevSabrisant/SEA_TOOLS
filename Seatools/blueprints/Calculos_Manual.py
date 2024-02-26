from datetime import datetime, timedelta
import calendar

def Cal(pVen, plano, Data_Simulada):
    DadosVen = [
        (11, 10, 19, 20) if pVen == "15"
        else (11, 10, 19, 20) if pVen == "20"
        else (21, 20, 9, 10) if pVen == "25"
        else (21, 20, 9, 10) if pVen == "30"
        else None]

    data = datetime.strptime(Data_Simulada, '%Y-%m-%d')

    quantidade_de_dias = calendar.monthrange(data.year, data.month)[1]

    Mes_que_vem = data + timedelta(days=30 if quantidade_de_dias == 30 else 31)

    r = f"Plano: {plano}\nVencimento: {pVen}\nData Simulada: {Data_Simulada}\nProximo Mês: {Mes_que_vem}"
    print(pVen, plano, Data_Simulada,Mes_que_vem)

    return r


