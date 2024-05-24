from flask import request, render_template, Blueprint, redirect , url_for, session
from blueprints.swich_calculo import *
from blueprints.mudar_venc import *
from blueprints.calculos import CalculoDesc
from blueprints.cancelar_client import Calculo_cancelamento
from blueprints.negociacao import Calculo_negociacao
from blueprints.indisponibilidades import salvar_dados, listar_indisponibilidades,detalhes, Deletar
from zipfile import BadZipFile
import pandas as pd
import plotly.graph_objs as go
from peewee import IntegrityError, DoesNotExist
from database.models.acess import User
from database.models.dash import Dash
import base64

from database.models.indispinibilidades import Indisponibilidade

Telas = Blueprint('Telas', __name__)
@Telas.route("/", methods=['GET', 'POST'])
def Home():

    if 'username' not in session:
        return redirect(url_for('Telas.login'))

    username = session['username']
    user = User.get_or_none(User.username == username)
    permissoes = user.permissions.split(',')

    return render_template('Home.html', permissoes=permissoes, session=username )

@Telas.route("/login", methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect('/')

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        try:
            user = User.get(User.username == username)

            if user and user.password == password:
                session['username'] = username
                objetos = Dash.select()
                for objeto in objetos:
                    objeto.logins = objeto.logins + 1 if objeto.logins is not None else 1

                    objeto.save()

                return redirect("/")

            else:
                error = "Credenciais inválidas. Por favor, tente novamente."
                return render_template('login.html', error=error)

        except User.DoesNotExist:
            user = None
    return render_template('login.html')

@Telas.route('/logout',methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect(url_for('Telas.login'))

@Telas.route("/homepage", methods=['POST', 'GET'])
def homepage():

    if 'username' not in session:
        return redirect(url_for('Telas.login'))

    if request.method == 'POST':
        resultado = S_venc(pVen=request.form.get('vencimento'), pAtual=request.form.get('planoAtual'), pNovo=request.form.get('planoNovo'), checkA=request.form.get('cidadeAnanindeua'), Data_Solicitacao = request.form.get("dataSolicitacao"))

        objetos = Dash.select()
        for objeto in objetos:
            objeto.homepage = objeto.homepage + 1 if objeto.homepage is not None else 1

            objeto.save()


        return render_template("homepage.html", resultado=resultado)
    return render_template("homepage.html")

@Telas.route("/homepage2", methods=['POST','GET'])
def homepage2():
    if 'username' not in session:
        return redirect(url_for('Telas.login'))

    if request.method == 'POST':
        resultadoVencimento = MudarVen(vAtual=request.form.get('vencimentoAtual'), vNovo=request.form.get('vencimentoNovo'), vPlano=request.form.get('planoCliente'), checkA=request.form.get('cidadeAnanindeua'), Data_Solicitacao = request.form.get("dataSolicitacao"))

        objetos = Dash.select()
        for objeto in objetos:
            objeto.homepage2 = objeto.homepage2 + 1 if objeto.homepage2 is not None else 1
            objeto.save()


        return  render_template("homepage2.html", resultadoVencimento = resultadoVencimento)
    return render_template("homepage2.html")

@Telas.route("/homepage3", methods=['POST','GET'])
def homepage3():
    if 'username' not in session:
        return redirect(url_for('Telas.login'))

    if request.method == 'POST':
        resultadoDesc =  CalculoDesc(Plano = request.form.get('Plano'),D = request.form.get('D'), M = request.form.get('M'), Data_Solicitacao = request.form.get("dataSolicitacao"))

        objetos = Dash.select()
        for objeto in objetos:
            objeto.homepage3 = objeto.homepage3 + 1 if objeto.homepage3 is not None else 1

            objeto.save()

        return render_template("homepage3.html", resultadoDesc = resultadoDesc)
    return render_template("homepage3.html")

@Telas.route("/homepage4", methods=['POST','GET'])
def homepage4():
    if 'username' not in session:
        return redirect(url_for('Telas.login'))

    if request.method == 'POST':
        resultado_cancelamento = Calculo_cancelamento(pAtual = request.form.get("Plano_cancelamento"), pVen = request.form.get("vencimento_cancelamento"), Data_Solicitacao = request.form.get("dataSolicitacao"),data_ati = request.form.get("data_ati"),multa=request.form.get("multa"))
        objetos = Dash.select()
        for objeto in objetos:
            objeto.homepage4 = objeto.homepage4 + 1 if objeto.homepage4 is not None else 1

            objeto.save()

        return render_template("homepage4.html", resultado_cancelamento=resultado_cancelamento)
    return render_template("homepage4.html")

@Telas.route("/homepage5", methods=['POST','GET'])
def homepage5():
    if 'username' not in session:
        return redirect(url_for('Telas.login'))

    if request.method == 'POST':
        campos_adicionais = []
        for key, value in request.form.items():
            if key.startswith('data') or key.startswith('valor') or key.startswith('dias') or key.startswith('multa') or key.startswith('juros') or key.startswith('cobrar'):
                campos_adicionais.append(value)
        try:
            r = Calculo_negociacao(campos_adicionais)
            objetos = Dash.select()
            for objeto in objetos:
                objeto.homepage5 = objeto.homepage5 + 1 if objeto.homepage5 is not None else 1

                objeto.save()
            return render_template("homepage5.html", resultados=r)

        except ValueError:

            return render_template("homepage5.html", resultados= "!!!", error="Error no envio do formulario (Vazio)" )
    return render_template("homepage5.html", resultados="!!!")

@Telas.route("/homepage6", methods=['GET', 'POST'])
def homepage6():
    if 'username' not in session:
        return redirect(url_for('Telas.login'))

    username = session['username']
    user = User.get_or_none(User.username == username)
    permissoes = user.permissions.split(',')


    indisponibilidades = listar_indisponibilidades()

    return render_template("homepage6.html", indisponibilidades = indisponibilidades, permissoes=permissoes)

@Telas.route("/dashboard", methods=['GET', 'POST'])
def dashboard():

    if 'username' not in session:
        return redirect(url_for('Telas.login'))

    username = session['username']
    user = User.get_or_none(User.username == username)
    permissoes = user.permissions.split(',')

    if 'homepage6' not in permissoes:
        return redirect(url_for('Telas.Home'))
    dados_dash = Dash.select().first()

    if dados_dash is None:
        return "Nenhum dado encontrado na tabela Dash"

    dados = {
        'titulo': 'SEATOOLS',
        'T/Plano': dados_dash.homepage,
        'T/Vencimento': dados_dash.homepage2,
        'Desconto':dados_dash.homepage3,
        'Negociação':dados_dash.homepage5,
        'Cancelamento':dados_dash.homepage4,
        'Acessos':dados_dash.logins
    }

    x = ['Plano', 'Vencimento','Desconto','Negociação', 'Cancelamento', 'Acessos']
    y = [dados_dash.homepage, dados_dash.homepage2,dados_dash.homepage3,dados_dash.homepage5,dados_dash.homepage4,dados_dash.logins]  # Usando os valores do banco de dados diretamente

    grafico = go.Figure(data=[go.Bar(x=x, y=y)])

    grafico.update_layout(title='Requisições')

    grafico_html = grafico.to_html(full_html=False)

    return render_template('dashboard.html', dados=dados_dash, grafico_html=grafico_html)

@Telas.route("/criar_indisponiblidades", methods=['POST','GET'])
def criar_indisponiblidades():
    if 'username' not in session:
        return redirect(url_for('Telas.login'))

    username = session['username']
    user = User.get_or_none(User.username == username)
    permissoes = user.permissions.split(',')

    if 'homepage6' not in permissoes:
        return redirect(url_for('Telas.Home'))



    if request.method == 'POST':
        cidade = request.form.get('cidade')
        protocolo = request.form.get('protocolo')
        xls_files = request.files.getlist('xls_file')
        img_file = request.files.get('img_file')
        status = request.form.get('status')

        if status == 'ativo':
            status = True
        else:
            status = False

        xls_data = []

        '''if img_file is not None and img_file != '':
            for xls_file in xls_files:
                try:
                    xls_data.append(pd.read_excel(xls_file, engine='openpyxl'))
                except BadZipFile:
                    pass'''

        for xls_file in xls_files:
            try:
                xls_data.append(pd.read_excel(xls_file, engine='openpyxl'))
            except BadZipFile:
                pass
        try:
            salvar_dados(xls_data, img_file, cidade, protocolo,status, img_file.filename)

            return render_template("criar_indisponiblidades.html")
        except IntegrityError:
            error = "Protocolo já existente!"
            return render_template("criar_indisponiblidades.html",mensagem_erro=error)

    return render_template("criar_indisponiblidades.html")

@Telas.route("/detalhes_indisponibilidade", methods=['POST','GET'])
def detalhes_indisponibilidade():
    if 'username' not in session:
        return redirect(url_for('Telas.login'))

    protocolo = request.form.get('protocolo')

    try:
        dados, foto, mimetype = detalhes(protocolo)

        tamanho = len(dados[:-4])

        foto = base64.b64encode(foto).decode('utf-8')

        return render_template("detalhes_indisponibilidade.html", Status=dados[-1], foto=foto, Cidade=dados[-2],
                               Protocol=dados[-3], lista_clientes=dados[:-3], len=tamanho,
                               extensao=mimetype.split('/')[-1].split(';')[0])

    except DoesNotExist:
        return render_template("homepage6.html")

@Telas.route('/excluir/<protocolo>', methods=['POST'])
def excluir_indisponibilidade(protocolo):
    if 'username' not in session:
        return redirect(url_for('Telas.login'))

    username = session['username']
    user = User.get_or_none(User.username == username)
    permissoes = user.permissions.split(',')

    if 'homepage6' not in permissoes:
        return redirect(url_for('Telas.Home'))

    try:

        Deletar(protocolo)

        return redirect(url_for('Telas.homepage6'))
    except Indisponibilidade.DoesNotExist:
        return redirect(url_for('Telas.homepage6'))

@Telas.route('/homepage7', methods=['GET', 'POST'])
def homepage7():
    if 'username' not in session:
        return redirect(url_for('Telas.login'))

    if request.method == 'POST':

        relato_cliente = request.form['relato_cliente']
        potencia = request.form['potencia']
        canal = request.form['canal']
        banda = request.form['banda']
        dns = request.form.getlist('dns')
        upnp = request.form['upnp']
        sntp = request.form['sntp']
        ipv6 = request.form['ipv6']
        observacoes = request.form['observacoes']

        return render_template('homepage7.html', relato_cliente=relato_cliente, potencia=potencia, canal=canal,
                               banda=banda, dns=dns, upnp=upnp, sntp=sntp, ipv6=ipv6, observacoes=observacoes)
    return render_template('homepage7.html')

@Telas.route('/homepage8', methods=['GET', 'POST'])
def homepage8():
    if 'username' not in session:
        return redirect(url_for('Telas.login'))

    if request.method == 'POST':
        tipo_os = request.form['tipoos']
        endereco = request.form['endereco']
        prioridade = request.form['prioridade']
        responsavel = request.form['responsavel']
        horario = request.form['horario']
        relato = request.form['relato']
        causa = request.form['causa']
        orientacao = request.form['orientacao']
        validador = request.form['validador']

        campoPotenciaOnu = request.form.get('potencia-onu')
        modelo = request.form.get('modelo')
        pppoe = request.form.get('pppoe')
        gpon = request.form.get('gpon')
        potenciaOlt = request.form.get('potenciaOlt')
        Outros = request.form.get('Outros')
        Temp = request.form.get('Temp')
        dispositivos_sem_nternet = request.form.get('dispositivos-sem-internet')
        alarmes_equipamento = request.form.get('alarmes-equipamento')

        print(campoPotenciaOnu)

        return render_template('homepage8.html', tipo_os=tipo_os, endereco=endereco, prioridade=prioridade,
                               responsavel=responsavel, horario=horario, relato=relato, causa=causa,
                               orientacao=orientacao, validador=validador, campoPotenciaOnu= campoPotenciaOnu, modelo=modelo,
                               gpon = gpon, pppoe =pppoe, potenciaOlt=potenciaOlt, Outros=Outros,Temp=Temp, dispositivos_sem_nternet=dispositivos_sem_nternet, alarmes_equipamento=alarmes_equipamento  )
    else:
        return render_template('homepage8.html')



