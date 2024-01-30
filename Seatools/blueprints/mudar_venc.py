from Seatools.blueprints.planos import *
from datetime import date
import calendar


data_hoje = date.today()  ##PEGANDO LOGO A DATA DE HOJE PRA SAPORRA TODA

def MudarVen(vAtual, vNovo,vPlano,checkA):

    global r
    if not checkA:

        MensagemFatura = f"Não possui pagamento proximo, Proporcional irá para proxima fatura."

        # QUANTIDADE DE DIAS NO MÊS

        quantidade_dias = calendar.monthrange(date.today().year, date.today().month)[1]

        # PROXIMO MÊS

        ProxAtual = (data_hoje.month % 12) + 1

        # CICLO DE 1 ATÉ 10
        IniVenc01 = date(data_hoje.year, data_hoje.month, 1)
        IniVenc01Br = IniVenc01.strftime("%d/%m/%Y")
        FinalVenc30 = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, data_hoje.month, quantidade_dias)
        FinalVenc30Br = FinalVenc30.strftime("%d/%m/%Y")

        # CICLO DE 11 ATÉ 10
        IniVenc11 = date(data_hoje.year, data_hoje.month, 11)
        IniVenc11Br = IniVenc11.strftime("%d/%m/%Y")
        FinalVenc10 = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, (data_hoje.month % 12) + 1, 10)
        FinalVenc10Br = FinalVenc10.strftime("%d/%m/%Y")

        # CICLO DE 21 ATÉ 20
        IniVenc21 = date(data_hoje.year, data_hoje.month, 21)
        IniVenc21Br = IniVenc21.strftime("%d/%m/%Y")
        FinalVenc20 = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, (data_hoje.month % 12) + 1, 20)
        FinalVenc20Br = FinalVenc20.strftime("%d/%m/%Y")

        # CONDIÇÕES DE TROCA DE VENCIMENTO

        if (vAtual == '5' or vAtual == '10') and (vNovo == '5' or vNovo == '10'):
            r = f"Plano: {vPlano}Megas\nVencimento: {vAtual} para {vNovo}\n\nNÃO TERÁ MUDANÇA NO VALOR DA FATURA"
            return r
        elif (vAtual == '5' or vAtual == '10') and (vNovo == '15' or vNovo == '20'):
            Qtd = quantidade_dias + FinalVenc10.day
            Valor = Qtd * globals()[f"plan{vPlano}"]()
            ValorDiferenca = (Qtd-30) * globals()[f'plan{vPlano}']()
            r = f"Plano: {vPlano}Megas\nVencimento: {vAtual} para {vNovo}\n\n{IniVenc01Br} -- {FinalVenc10Br}. São {Qtd} dias -- totalizando: {Valor:.2f}\nCom desconto de 10%: {Valor - Valor * 0.1:.2f}\nDesconto de: {Valor * 0.1:.2f}\n\nVencimento mais próximo:\n{IniVenc01Br} -- {date(data_hoje.year, data_hoje.month, 10).strftime('%d/%m/%Y')}. São {Qtd - 30} dias -- Proporcional: {ValorDiferenca:.2f}\nCom desconto de 10%: {ValorDiferenca - (ValorDiferenca * 0.1):.2f}\nDesconto de: {ValorDiferenca * 0.1:.2f}  1" if (ValorDiferenca > 50) and (data_hoje.day <= 10)                             else f"Plano: {vPlano}Megas\nVencimento: {vAtual} para {vNovo}\n\n{IniVenc01Br} -- {FinalVenc10Br}. São {Qtd} dias -- totalizando: {Valor:.2f}\nCom desconto de 10%: {Valor - Valor * 0.1:.2f}\nDesconto de: {Valor * 0.1:.2f}\n\nProporcional de {Qtd - 30} dias: {ValorDiferenca:.2f}\n\n{MensagemFatura}"
            return r

        elif (vAtual == '5' or vAtual == '10') and (vNovo == '25' or vNovo == '30'):
            Qtd = quantidade_dias + FinalVenc20.day
            Valor = Qtd * globals()[f"plan{vPlano}"]()
            ValorDiferenca = (Qtd-30) * globals()[f'plan{vPlano}']()
            r = f"Plano: {vPlano}Megas\nVencimento: {vAtual} para {vNovo}\n\n{IniVenc01Br} -- {FinalVenc20Br}. São {Qtd} dias -- totalizando: {Valor:.2f}\nCom desconto de 10%: {Valor - Valor * 0.1:.2f}\nDesconto de: {Valor * 0.1:.2f}\n\nVencimento mais proximo:\n{IniVenc01Br} -- {date(data_hoje.year,data_hoje.month,20).strftime('%d/%m/%Y')}. São {Qtd-30} dias -- Proporcional: {ValorDiferenca:.2f}\nCom desconto de 10%: {ValorDiferenca - (ValorDiferenca * 0.1):.2f}\nDesconto de: {ValorDiferenca * 0.1:.2f}  1" if (ValorDiferenca > 50) and (data_hoje.day <= 20)                                else f"Plano: {vPlano}Megas\nVencimento: {vAtual} para {vNovo}\n\n{IniVenc01Br} -- {FinalVenc10Br}. São {Qtd} dias -- totalizando: {Valor:.2f}\nCom desconto de 10%: {Valor - Valor * 0.1:.2f}\nDesconto de: {Valor * 0.1:.2f}\n\nProporcional de {Qtd - 30} dias: {ValorDiferenca:.2f}\n\n{MensagemFatura}"
            return r

        # VENCIMENTO 15 OU 20

        elif (vAtual == '15' or vAtual == '20') and (vNovo == '15' or vNovo == '20'):
            r = f"Plano: {vPlano}Megas\nVencimento: {vAtual} para {vNovo}\n\nNÃO TERÁ MUDANÇA NO VALOR DA FATURA"
            return r

        elif (vAtual == '15' or vAtual == '20') and (vNovo == '25' or vNovo == '30'):
            Qtd = (quantidade_dias - 10) + FinalVenc20.day
            Valor = Qtd * globals()[f"plan{vPlano}"]()
            ValorDiferenca = (Qtd-30) * globals()[f'plan{vPlano}']()
            r = f"Plano: {vPlano}Megas\nVencimento: {vAtual} para {vNovo}\n\n{IniVenc11Br} -- {FinalVenc20Br}. São {Qtd} dias -- totalizando: {Valor:.2f}\nCom desconto de 10%: {Valor - Valor * 0.1:.2f}\nDesconto de: {Valor * 0.1:.2f}\n\nVencimento mais proximo:\n{IniVenc11Br} -- {date(data_hoje.year,data_hoje.month,20).strftime('%d/%m/%Y')}. São {Qtd-30} dias -- Proporcional:  {ValorDiferenca:.2f}\nCom desconto de 10%: {ValorDiferenca - (ValorDiferenca * 0.1):.2f}\nDesconto de: {ValorDiferenca * 0.1:.2f}  1" if (ValorDiferenca > 50) and (data_hoje.day <= 20)                              else f"Plano: {vPlano}Megas\nVencimento: {vAtual} para {vNovo}\n\n{IniVenc11Br} -- {FinalVenc20Br}. São {Qtd} dias -- totalizando: {Valor:.2f}\nCom desconto de 10%: {Valor - Valor * 0.1:.2f}\nDesconto de: {Valor * 0.1:.2f}\n\nProporcional de {Qtd-30} dias: {ValorDiferenca:.2f}\n\n{MensagemFatura}"
            return r

        elif (vAtual == '15' or vAtual == '20') and (vNovo == '5' or vNovo == '10'):
            Qtd = (quantidade_dias - 10)
            Valor = Qtd * globals()[f"plan{vPlano}"]()
            Valo_plan_completo = 30 * globals()[f"plan{vPlano}"]()
            Mes_anterior = date(data_hoje.year-1 if (data_hoje.month == 1) else data_hoje.year,(data_hoje.month % 12) + 1 if data_hoje.month != 1 else 12, 11)
            Mes_anteriorBr = Mes_anterior.strftime("%d/%m/%Y")
            Mes_atual = date(data_hoje.year,data_hoje.month, 10)
            Mes_atualBr = Mes_atual.strftime("%d/%m/%Y")
            r = f"Plano: {vPlano}Megas\nVencimento: {vAtual} para {vNovo}\n\n{IniVenc11Br} -- {FinalVenc30Br}. São {Qtd} dias -- Proporcional: {Valor:.2f}\nCom desconto de 10%: {Valor - Valor * 0.1:.2f}\nDesconto de: {Valor * 0.1:.2f}\n\nVencimento deste mês:\n{Mes_anteriorBr} -- {Mes_atualBr}. São 30 dias -- totalizando:  {Valo_plan_completo:.2f}\nCom desconto de 10%: {Valo_plan_completo - (Valo_plan_completo * 0.1):.2f}\nDesconto de: {Valo_plan_completo * 0.1:.2f}"
            return r

        # VENCIMENTO 25 OU 30

        elif (vAtual == '25' or vAtual == '30') and (vNovo == '25' or vNovo == '30'):
            r = f"Plano: {vPlano}Megas\nVencimento: {vAtual} para {vNovo}\n\nNÃO TERÁ MUDANÇA NO VALOR DA FATURA"
            return r

        elif (vAtual == '25' or vAtual == '30') and (vNovo == '15' or vNovo == '20'):
            Qtd = (quantidade_dias - 20) + FinalVenc10.day
            Valor = Qtd * globals()[f"plan{vPlano}"]()
            Valo_plan_completo = 30 * globals()[f"plan{vPlano}"]()
            Mes_anterior = date(data_hoje.year-1 if (data_hoje.month == 1) else data_hoje.year,(data_hoje.month % 12) + 1 if data_hoje.month != 1 else 12, 21)
            Mes_anteriorBr = Mes_anterior.strftime("%d/%m/%Y")
            Mes_atual = date(data_hoje.year,data_hoje.month, 20)
            Mes_atualBr = Mes_atual.strftime("%d/%m/%Y")
            r = f"Plano: {vPlano}Megas\nVencimento: {vAtual} para {vNovo}\n\n{IniVenc21Br} -- {FinalVenc10Br}. São {Qtd} dias -- Proporcional: {Valor:.2f}\nCom desconto de 10%: {Valor - Valor * 0.1:.2f}\nDesconto de: {Valor * 0.1:.2f}\n\nVencimento deste mês:\n{Mes_anteriorBr} -- {Mes_atualBr}. São 30 dias -- totalizando:  {Valo_plan_completo:.2f}\nCom desconto de 10%: {Valo_plan_completo - (Valo_plan_completo * 0.1):.2f}\nDesconto de: {Valo_plan_completo * 0.1:.2f}"
            return r

        elif (vAtual == '25' or vAtual == '30') and (vNovo == '5' or vNovo == '10'):
            Qtd = (quantidade_dias - 20)
            Valor = Qtd * globals()[f"plan{vPlano}"]()
            Valo_plan_completo = 30 * globals()[f"plan{vPlano}"]()
            Mes_anterior = date(data_hoje.year-1 if (data_hoje.month == 1) else data_hoje.year,(data_hoje.month % 12) + 1 if data_hoje.month != 1 else 12, 21)
            Mes_anteriorBr = Mes_anterior.strftime("%d/%m/%Y")
            Mes_atual = date(data_hoje.year,data_hoje.month, 20)
            Mes_atualBr = Mes_atual.strftime("%d/%m/%Y")
            r = f"Plano: {vPlano}Megas\nVencimento: {vAtual} para {vNovo}\n\n{IniVenc21Br} -- {FinalVenc30Br}. São {Qtd} dias -- Proporcional: {Valor:.2f}\nCom desconto de 10%: {Valor - Valor * 0.1:.2f}\nDesconto de: {Valor * 0.1:.2f}\n\nVencimento deste mês:\n{Mes_anteriorBr} -- {Mes_atualBr}. São 30 dias -- totalizando:  {Valo_plan_completo:.2f}\nCom desconto de 10%: {Valo_plan_completo - (Valo_plan_completo * 0.1):.2f}\nDesconto de: {Valo_plan_completo * 0.1:.2f}"
            return r
    else:
        if (vAtual == "30") or (vNovo == "30"):
            r = f"A CIDADE NÃO POSSUI ESSE VENCIMENTO!"
        else:

            # QUANTIDADE DE DIAS NO MÊS

            quantidade_dias = calendar.monthrange(date.today().year, date.today().month)[1]


            DadosVenA = [(6, 5) if vNovo == "5"
            else (11, 10) if vNovo == "10"
            else (16, 15) if vNovo == "15"
            else (21, 20) if vNovo == "20"
            else (26, 25) if vNovo == "25"
            else "None"]

            DadosVenB = [(6, 5, quantidade_dias, quantidade_dias+5, quantidade_dias+10, quantidade_dias+15, quantidade_dias+20) if vAtual == "5"
            else (11, 10, quantidade_dias-5, quantidade_dias, quantidade_dias+5, quantidade_dias+10, quantidade_dias+15) if vAtual == "10"
            else (16, 15, quantidade_dias-10, quantidade_dias-5, quantidade_dias, quantidade_dias+5, quantidade_dias+10) if vAtual == "15"
            else (21, 20, quantidade_dias-15, quantidade_dias-10, quantidade_dias-5, quantidade_dias, quantidade_dias+5) if vAtual == "20"
            else (26, 25, quantidade_dias-20, quantidade_dias-15, quantidade_dias-10, quantidade_dias-5, quantidade_dias) if vAtual == "25"
            else "None"]

            Contador = 2 if vNovo == "5" else 3 if vNovo == "10" else 4 if vNovo == "15" else 5 if vNovo == "20" else 6 if vNovo == "25" else "None"

            # PROXIMO MÊS

            ProxAtual = (data_hoje.month % 12) + 1

            IniVenc = date(date.today().year, date.today().month, DadosVenB[0][0])
            IniVencBr = IniVenc.strftime("%d/%m/%Y")
            FinalVenc = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, (date.today().month % 12) + 1,
                             DadosVenA[0][1])
            FinalVencBr = FinalVenc.strftime("%d/%m/%Y")

            Valor = DadosVenB[0][Contador] * globals()[f"plan{vPlano}"]()
            ValorDiferenca = (int(vNovo) - int(vAtual)) * globals()[f'plan{vPlano}']()
            MensagemFatura = f"Não possui pagamento proximo, Proporcional irá para proxima fatura."

            if vAtual == vNovo:
                r = f"NÃO TERÁ ALTERAÇÃO NA FATURA!"
            else:
                if int(vAtual) < int(vNovo):
                    FinalVencMaisProx = date(data_hoje.year, date.today().month, DadosVenA[0][1])

                    FinalVencMaisProxBr = FinalVencMaisProx.strftime("%d/%m/%Y")

                    if (IniVenc.day <= DadosVenA[0][1]):
                        if ValorDiferenca < 50:
                            r = f"Do {vAtual} para {vNovo}: \n{IniVencBr} -- {FinalVencBr}. São {DadosVenB[0][Contador]} dias -- totalizando: {Valor:.2f}\nCom desconto de 10%: {Valor - Valor * 0.1:.2f}\nDesconto de: {Valor * 0.1:.2f}\n\nProporcional de: {ValorDiferenca:.2f}\n\n{MensagemFatura}"
                        else:
                            r = f"Do {vAtual} para {vNovo}: \n{IniVencBr} -- {FinalVencBr}. São {DadosVenB[0][Contador]} dias -- totalizando: {Valor:.2f}\nCom desconto de 10%: {Valor - Valor * 0.1:.2f}\nDesconto de: {Valor * 0.1:.2f}\n\nVencimento mais proximo: \n{IniVencBr} -- {FinalVencMaisProxBr}. São {int(vNovo) - int(vAtual)} dias -- Proporcional: {ValorDiferenca:.2f}\nCom desconto de 10%: {ValorDiferenca - (ValorDiferenca * 0.1):.2f}\nDesconto de: {ValorDiferenca * 0.1:.2f}"
                else:
                    r = f"Do {vAtual} para {vNovo}: \n{IniVencBr} -- {FinalVencBr}. São {DadosVenB[0][Contador]} dias -- totalizando: {Valor:.2f}\nCom desconto de 10%: {Valor - Valor * 0.1:.2f}\nDesconto de: {Valor * 0.1:.2f}\n\nProporcional de: {ValorDiferenca*-1:.2f}\n\n{MensagemFatura}"

        return r
# FUNÇÃO PARA SABER QUAL CALCULO SE DEVE USAR