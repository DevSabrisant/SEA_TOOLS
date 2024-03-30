from flask import request, render_template, Blueprint, redirect , url_for, session
from blueprints.swich_calculo import *
from blueprints.mudar_venc import *
from blueprints.calculos import CalculoDesc
from blueprints.cancelar_client import Calculo_cancelamento
from blueprints.negociacao import Calculo_negociacao
from blueprints.indisponibilidades import *
from zipfile import BadZipFile
import pandas as pd
import plotly.graph_objs as go

from database.models.acess import User
from database.models.dash import Dash


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
                    objeto.logins += 1
                    objeto.save()

                return redirect("/")

            else:
                error = "Credenciais inválidas. Por favor, tente novamente."
                return render_template('login.html', error=error)

        except User.DoesNotExist:
            user = None
    return render_template('login.html')


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
            objeto.homepage += 1
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
            objeto.homepage2 += 1
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
            objeto.homepage3 += 1
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
            objeto.homepage4 += 1
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
                objeto.homepage5 += 1
                objeto.save()
            return render_template("homepage5.html", resultados=r)

        except ValueError:

            return render_template("homepage5.html", resultados= "!!!", error="Error no envio do formulario (Vazio)" )
    return render_template("homepage5.html", resultados="!!!")
@Telas.route("/homepage6", methods=['POST','GET'])
def homepage6():
    if 'username' not in session:
        return redirect(url_for('Telas.login'))

    username = session['username']
    user = User.get_or_none(User.username == username)
    permissoes = user.permissions.split(',')

    if 'homepage6' not in permissoes:
        return redirect(url_for('Telas.Home'))

    cidade = request.form.get('cidade')
    protocolo = request.form.get('protocolo')
    xls_files = request.files.getlist('xls_file')
    img_file = request.files.get('img_file')

    xls_data = []

    if img_file is not None and img_file != '':
        for xls_file in xls_files:
            try:
                xls_data.append(pd.read_excel(xls_file, engine='openpyxl'))
            except BadZipFile:
                pass
    r = lista_cliente(cidade, protocolo, xls_data)
    r_imagem = imagem_comunicado(img_file)

    return render_template("homepage6.html", r=r, r_imagem=r_imagem)

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