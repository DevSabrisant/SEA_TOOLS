from flask import Flask , render_template, request
import calendar
from datetime import date
app = Flask(__name__)


@app.route("/", methods=['POST','GET'])
def homepage():
    resultado = venc(pVen = request.form.get('vencimento'),pAtual= request.form.get('planoAtual'),pNovo= request.form.get('planoNovo'))

    return render_template("homepage.html",resultado=resultado)

@app.route("/homepage2",methods=['POST','GET'])
def homepage2():
    resultadoVencimento = MudarVen(vAtual = request.form.get('vencimentoAtual'), vNovo=request.form.get('vencimentoNovo'), vPlano= request.form.get('planoClinte'))

    return  render_template("homepage2.html", resultadoVencimento = resultadoVencimento)




# PLANOS - CRIA UMA FUNÇÃO NOVA PARA UM PLANO NOVO - SEGUE O PADRÃO K7
def plan250():
    return 110 / 30
def plan350():
    return 130 / 30
def plan450():
    return 160 / 30
def plan600():
    return 210 / 30

data_hoje = date.today()  ##PEGANDO LOGO A DATA DE HOJE PRA SAPORRA TODA

# FUNÇÕES DE CACULO DE PLANO -  AQUI ATÉ O PYTHON DEMORA INTERPRETAR
def Calcularven1(pAtual, pNovo):
    if data_hoje.day != 1:
            Day = data_hoje.day - 1
            DayPlAtual = globals()[f"plan{pAtual}"]() * (data_hoje.day - 1)
            RestanteDayNovo = 31 - data_hoje.day
            DayPlNovo = globals()[f"plan{pNovo}"]() * (31 - data_hoje.day)

            ValorTotal = DayPlAtual + DayPlNovo

            IniConsumo = date(date.today().year, date.today().month, 1)
            IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
            Ate = date(date.today().year, date.today().month, Day)
            AteBr = Ate.strftime("%d/%m/%Y")

            # SLA É A VARIAVEL QUE EU NÃO FAÇO A MENOR IDEIA DO QUE FAZ, MAIS EU SÓ PRECISO DA QUANTIDADE DE DIAS ENTT FDS
            SLA, quantidade_dias = calendar.monthrange(data_hoje.year, data_hoje.month)
            FinalConusmo = date(data_hoje.year, data_hoje.month, quantidade_dias)
            FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

            r = f"De {pAtual}mb para {pNovo}mb: \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} são totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}.\nDesconto de: {ValorTotal * 0.1:.2f} "

    else:
        RestanteDayNovo = 31 - data_hoje.day
        DayPlNovo = globals()[f"plan{pNovo}"]() * (31 - data_hoje.day)

        # SLA É A VARIAVEL QUE EU NÃO FAÇO A MENOR IDEIA DO QUE FAZ, MAIS EU SÓ PRECISO DA QUANTIDADE DE DIAS ENTT FDS
        SLA, quantidade_dias = calendar.monthrange(data_hoje.year, data_hoje.month)
        FinalConusmo = date(data_hoje.year, data_hoje.month, quantidade_dias)
        FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

        r = f"De {pAtual}mb para {pNovo}mb: \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} dias totalizando: {DayPlNovo:.2f}.\nO valor final será: {DayPlNovo:.2f}.\nCom 10% será: {DayPlNovo - (DayPlNovo * 0.1):.2f}.\nDesconto de: {DayPlNovo * 0.1:.2f} "


    return r
def Calcularven2(pAtual, pNovo):
    if data_hoje.day != 1:
        if data_hoje.month != 1:
            # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
            if data_hoje.day <= 10:
                Day = data_hoje.day + 19
                DayPlAtual = (data_hoje.day + 19) * globals()[f"plan{pAtual}"]()
                RestanteDayNovo = 31 - (data_hoje.day + 20)
                DayPlNovo = (31 - (data_hoje.day + 20)) * globals()[f"plan{pNovo}"]()

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(date.today().year, date.today().month - 1, 11)
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(date.today().year, date.today().month, data_hoje.day - 1)
                AteBr = Ate.strftime("%d/%m/%Y")

                FinalConusmo = date(data_hoje.year, data_hoje.month, 10)
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"De {pAtual}mb para {pNovo}mb: \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}.\nDesconto de: {ValorTotal * 0.1:.2f}  "

                return r
            # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
            elif data_hoje.day >= 10:
                Day = data_hoje.day - 10
                DayPlAtual = (data_hoje.day - 10) * globals()[f"plan{pAtual}"]()
                RestanteDayNovo = 30 - (data_hoje.day - 10)
                DayPlNovo = (30 - (data_hoje.day - 10)) * globals()[f"plan{pNovo}"]()

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(date.today().year, date.today().month, 11)
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(date.today().year, date.today().month, data_hoje.day - 1)
                AteBr = Ate.strftime("%d/%m/%Y")

                ProxAtual = (data_hoje.month % 12) + 1
                FinalConusmo = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, ProxAtual, 10)
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"De {pAtual}mb para {pNovo}mb: \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}.\nDesconto de: {ValorTotal * 0.1:.2f}"

                return r
        else:
            # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
            if data_hoje.day <= 10:
                Day = data_hoje.day + 19
                DayPlAtual = (data_hoje.day + 19) * globals()[f"plan{pAtual}"]()
                RestanteDayNovo = 31 - (data_hoje.day + 20)
                DayPlNovo = (31 - (data_hoje.day + 20)) * globals()[f"plan{pNovo}"]()

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(date.today().year, 12, 11)
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(date.today().year, date.today().month, data_hoje.day - 1)
                AteBr = Ate.strftime("%d/%m/%Y")

                FinalConusmo = date(data_hoje.year, data_hoje.month, 10)
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"De {pAtual}mb para {pNovo}mb: \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}.\nDesconto de: {ValorTotal * 0.1:.2f}  "

                return r
            # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
            elif data_hoje.day >= 10:
                Day = data_hoje.day - 10
                DayPlAtual = (data_hoje.day - 10) * globals()[f"plan{pAtual}"]()
                RestanteDayNovo = 30 - (data_hoje.day - 10)
                DayPlNovo = (30 - (data_hoje.day - 10)) * globals()[f"plan{pNovo}"]()

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(date.today().year, date.today().month, 11)
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(date.today().year, date.today().month, data_hoje.day - 1)
                AteBr = Ate.strftime("%d/%m/%Y")

                ProxAtual = (data_hoje.month % 12) + 1
                FinalConusmo = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, ProxAtual, 10)
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"De {pAtual}mb para {pNovo}mb: \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}.\nDesconto de: {ValorTotal * 0.1:.2f}"

                return r
    else:
        if data_hoje.month != 1:
            # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
                Day = data_hoje.day + 19
                DayPlAtual = (data_hoje.day + 19) * globals()[f"plan{pAtual}"]()
                RestanteDayNovo = 31 - (data_hoje.day + 20)
                DayPlNovo = (31 - (data_hoje.day + 20)) * globals()[f"plan{pNovo}"]()

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(date.today().year, date.today().month - 1, 11)
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(date.today().year, date.today().month, data_hoje.day)
                AteBr = Ate.strftime("%d/%m/%Y")

                FinalConusmo = date(data_hoje.year, data_hoje.month, 10)
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"De {pAtual}mb para {pNovo}mb: \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}.\nDesconto de: {ValorTotal * 0.1:.2f}  "

                return r
        else:
                Day = data_hoje.day + 19
                DayPlAtual = (data_hoje.day + 19) * globals()[f"plan{pAtual}"]()
                RestanteDayNovo = 31 - (data_hoje.day + 20)
                DayPlNovo = (31 - (data_hoje.day + 20)) * globals()[f"plan{pNovo}"]()

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(date.today().year, 12, 11)
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(date.today().year, date.today().month, data_hoje.day)
                AteBr = Ate.strftime("%d/%m/%Y")

                FinalConusmo = date(data_hoje.year, data_hoje.month, 10)
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"De {pAtual}mb para {pNovo}mb: \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}.\nDesconto de: {ValorTotal * 0.1:.2f}  "

                return r
def Calcularven3(pAtual, pNovo):
    if data_hoje.day != 1:
        if data_hoje.month != 1:
            # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
            if data_hoje.day <= 20:
                Day = data_hoje.day + 9
                DayPlAtual = (data_hoje.day + 9) * globals()[f"plan{pAtual}"]()
                RestanteDayNovo = 31 - (data_hoje.day + 10)
                DayPlNovo = (31 - (data_hoje.day + 10)) * globals()[f"plan{pNovo}"]()

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(date.today().year, date.today().month - 1, 21)
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(date.today().year, date.today().month, data_hoje.day - 1)
                AteBr = Ate.strftime("%d/%m/%Y")

                FinalConusmo = date(data_hoje.year, data_hoje.month, 20)
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"De {pAtual}mb para {pNovo}mb: \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}.\nDesconto de: {ValorTotal * 0.1:.2f}  "

                return r
            # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
            elif data_hoje.day >= 20:
                Day = data_hoje.day - 20
                DayPlAtual = (data_hoje.day - 20) * globals()[f"plan{pAtual}"]()
                RestanteDayNovo = 30 - (data_hoje.day - 20)
                DayPlNovo = (30 - (data_hoje.day - 20)) * globals()[f"plan{pNovo}"]()

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(date.today().year, date.today().month, 21)
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(date.today().year, date.today().month, data_hoje.day - 1)
                AteBr = Ate.strftime("%d/%m/%Y")

                ProxAtual = (data_hoje.month % 12) + 1
                FinalConusmo = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, ProxAtual, 20)
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"De {pAtual}mb para {pNovo}mb: \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}.\nDesconto de: {ValorTotal * 0.1:.2f} "

                return r
        else:
            # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
            if data_hoje.day <= 20:
                Day = data_hoje.day + 9
                DayPlAtual = (data_hoje.day + 9) * globals()[f"plan{pAtual}"]()
                RestanteDayNovo = 31 - (data_hoje.day + 10)
                DayPlNovo = (31 - (data_hoje.day + 10)) * globals()[f"plan{pNovo}"]()

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(date.today().year, 12, 21)
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(date.today().year, date.today().month, data_hoje.day - 1)
                AteBr = Ate.strftime("%d/%m/%Y")

                FinalConusmo = date(data_hoje.year, data_hoje.month, 20)
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"De {pAtual}mb para {pNovo}mb: \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}.\nDesconto de: {ValorTotal * 0.1:.2f}  "

                return r
            # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
            elif data_hoje.day >= 20:
                Day = data_hoje.day - 20
                DayPlAtual = (data_hoje.day - 20) * globals()[f"plan{pAtual}"]()
                RestanteDayNovo = 30 - (data_hoje.day - 20)
                DayPlNovo = (30 - (data_hoje.day - 20)) * globals()[f"plan{pNovo}"]()

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(date.today().year, 12, 21)
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(date.today().year, date.today().month, data_hoje.day - 1)
                AteBr = Ate.strftime("%d/%m/%Y")

                ProxAtual = (data_hoje.month % 12) + 1
                FinalConusmo = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, ProxAtual, 20)
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"De {pAtual}mb para {pNovo}mb: \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}.\nDesconto de: {ValorTotal * 0.1:.2f} "

                return r
    else:
        if data_hoje.month != 1:
            if data_hoje.day <= 20:
                Day = data_hoje.day + 9
                DayPlAtual = (data_hoje.day + 9) * globals()[f"plan{pAtual}"]()
                RestanteDayNovo = 31 - (data_hoje.day + 10)
                DayPlNovo = (31 - (data_hoje.day + 10)) * globals()[f"plan{pNovo}"]()

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(date.today().year, date.today().month - 1, 21)
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(date.today().year, date.today().month, data_hoje.day)
                AteBr = Ate.strftime("%d/%m/%Y")

                FinalConusmo = date(data_hoje.year, data_hoje.month, 20)
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"De {pAtual}mb para {pNovo}mb: \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}.\nDesconto de: {ValorTotal * 0.1:.2f}  "

                return r
        else:
            Day = data_hoje.day + 9
            DayPlAtual = (data_hoje.day + 9) * globals()[f"plan{pAtual}"]()
            RestanteDayNovo = 31 - (data_hoje.day + 10)
            DayPlNovo = (31 - (data_hoje.day + 10)) * globals()[f"plan{pNovo}"]()

            ValorTotal = DayPlAtual + DayPlNovo

            IniConsumo = date(date.today().year, 12, 21)
            IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
            Ate = date(date.today().year, date.today().month, data_hoje.day)
            AteBr = Ate.strftime("%d/%m/%Y")

            FinalConusmo = date(data_hoje.year, data_hoje.month, 20)
            FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

            r = f"De {pAtual}mb para {pNovo}mb: \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}.\nDesconto de: {ValorTotal * 0.1:.2f}  "

            return r

# FUNÇÃO PARA SABER QUAL CALCULO SE DEVE USAR


# FUNÇÃO DE MUDANÇA DE VENICMENTO - TEM NADA HAVER COM OS CAULOS ACIMA
def MudarVen(vAtual, vNovo,vPlano):

    # QUANTIDADE DE DIAS NO MÊS

    quantidade_dias = calendar.monthrange(date.today().year, date.today().month)[1]

    # PROXIMO MÊS

    ProxAtual = (data_hoje.month % 12) + 1

    # CICLO DE 01 ATÉ 30

    IniVenc01 = date(date.today().year, date.today().month, 1)
    IniVenc01Br = IniVenc01.strftime("%d/%m/%Y")
    FinalVenc30 = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, date.today().month, quantidade_dias)
    FinalVenc30Br = FinalVenc30.strftime("%d/%m/%Y")

    # CICLO DE 11 ATÉ 10

    IniVenc11 = date(date.today().year, date.today().month, 11)
    IniVenc11Br = IniVenc11.strftime("%d/%m/%Y")
    FinalVenc10 = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, (date.today().month % 12) + 1, 10)
    FinalVenc10Br = FinalVenc10.strftime("%d/%m/%Y")

    # CICLO DE 21 ATÉ 20

    IniVenc21 = date(date.today().year, date.today().month, 21)
    IniVenc21Br = IniVenc21.strftime("%d/%m/%Y")
    FinalVenc20 = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, (date.today().month % 12) + 1, 20)
    FinalVenc20Br = FinalVenc20.strftime("%d/%m/%Y")

    # CONDIÇÕES DE TROCA DE VENCIMENTO

    if (vAtual == '5' or vAtual == '10') and (vNovo == '5' or vNovo == '10'):
        r = f"Do {vAtual} para {vNovo}: \nNÃO TERÁ MUDANÇA NO VALOR DA FATURA"
        return r

    if (vAtual == '5' or vAtual == '10') and (vNovo == '15' or vNovo == '20'):
        QtdDias = FinalVenc10 - IniVenc01
        Valor = QtdDias.days * globals()[f"plan{vPlano}"]()
        r = f"Do {vAtual} para {vNovo}: \n{IniVenc01Br} -- {FinalVenc10Br}. São {QtdDias.days} dias -- totalizando: {Valor:.2f}\nVencimento mais proximo:\n{IniVenc01Br} -- {date(data_hoje.year,data_hoje.month,10).strftime('%d/%m/%Y')}. São {QtdDias.days-30} dias -- totalizando: {(QtdDias.days-30) * globals()[f'plan{vPlano}']():.2f}"
        return r

    elif (vAtual == '5' or vAtual == '10') and (vNovo == '25' or vNovo == '30'):
        QtdDias = FinalVenc20 - IniVenc01
        Valor = QtdDias.days * globals()[f"plan{vPlano}"]()
        r = f"Do {vAtual} para {vNovo}: \n{IniVenc01Br} -- {FinalVenc20Br}. São {QtdDias.days} dias -- totalizando: {Valor:.2f}\nVencimento mais proximo:\n{IniVenc01Br} -- {date(data_hoje.year,data_hoje.month,20).strftime('%d/%m/%Y')}. São {QtdDias.days-30} dias -- totalizando: {(QtdDias.days-30) * globals()[f'plan{vPlano}']():.2f}"
        return r

    # VENCIMENTO 15 OU 20

    elif (vAtual == '15' or vAtual == '20') and (vNovo == '15' or vNovo == '20'):
        r = f"Do {vAtual} para {vNovo}: \nNÃO TERÁ MUDANÇA NO VALOR DA FATURA"
        return r

    elif (vAtual == '15' or vAtual == '20') and (vNovo == '25' or vNovo == '30'):
        Qtd = 40
        Valor = Qtd * globals()[f"plan{vPlano}"]()
        r = f"Do {vAtual} para {vNovo}: \n{IniVenc11Br} -- {FinalVenc20Br}. São {Qtd} dias -- totalizando: {Valor:.2f}\nVencimento mais proximo:\n{IniVenc11Br} -- {date(data_hoje.year,data_hoje.month,20).strftime('%d/%m/%Y')}. São {Qtd-30} dias -- totalizando:  {(Qtd-30) * globals()[f'plan{vPlano}']():.2f}"
        return r

    elif (vAtual == '15' or vAtual == '20') and (vNovo == '5' or vNovo == '10'):
        Qtd = 20
        Valor = Qtd * globals()[f"plan{vPlano}"]()
        r = f"Do {vAtual} para {vNovo}: \n{IniVenc11Br} -- {FinalVenc30Br}. São {Qtd} dias -- totalizando: {Valor:.2f}"
        return r

    # VENCIMENTO 25 OU 30

    elif (vAtual == '25' or vAtual == '30') and (vNovo == '25' or vNovo == '30'):
        r = f"Do {vAtual} para {vNovo}: \nNÃO TERÁ MUDANÇA NO VALOR DA FATURA"
        return r

    elif (vAtual == '25' or vAtual == '30') and (vNovo == '15' or vNovo == '20'):
        Qtd = 20
        Valor = Qtd * globals()[f"plan{vPlano}"]()
        r = f"Do {vAtual} para {vNovo}: \n{IniVenc21Br} -- {FinalVenc10Br}. São {Qtd} dias -- totalizando: {Valor:.2f}"
        return r


    elif (vAtual == '25' or vAtual == '30') and (vNovo == '5' or vNovo == '10'):
        Qtd = 10
        Valor = Qtd * globals()[f"plan{vPlano}"]()
        r = f"Do {vAtual} para {vNovo}: \n{IniVenc21Br} -- {FinalVenc30Br}. São {Qtd} dias -- totalizando: {Valor:.2f}"
        return r

def venc(pVen, pAtual, pNovo):
        if pVen in ["5", "10"]:
            return Calcularven1(pAtual, pNovo)  # VENCIMENTO 5 OU 10
        elif pVen in ["15", "20"]:
            return Calcularven2(pAtual, pNovo)  # VENCIMENTO 15 OU 20
        elif pVen in ["25", "30"]:
            return Calcularven3(pAtual, pNovo)  # VENCIMENTO 25 OU 30
        else:
            return "Opção de vencimento inválida"

if __name__ == "__main__":
    app.run(debug=True)


