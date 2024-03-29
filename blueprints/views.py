from flask import request, render_template, Blueprint, redirect , url_for, session
from blueprints.swich_calculo import *
from blueprints.mudar_venc import *
from blueprints.calculos import CalculoDesc
from blueprints.cancelar_client import Calculo_cancelamento
from blueprints.negociacao import Calculo_negociacao
from blueprints.indisponibilidades import *
from zipfile import BadZipFile
from static.acess import *
import pandas as pd

Telas = Blueprint('Telas', __name__)

@Telas.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if (username in users) and (users[username]['senha'] == password):
            session['username'] = username
            return redirect("/")

    return render_template('login.html')

@Telas.route("/", methods=['GET', 'POST'])
def Home():
    if 'username' not in session:
        return redirect(url_for('Telas.login'))
    username = session['username']
    permissoes = users[username]['permissoes']

    return render_template('Home.html', permissoes=permissoes)

@Telas.route("/homepage", methods=['POST', 'GET'])
def homepage():
    if 'username' not in session:
        return redirect(url_for('Telas.login'))

    resultado = S_venc(pVen=request.form.get('vencimento'), pAtual=request.form.get('planoAtual'), pNovo=request.form.get('planoNovo'), checkA=request.form.get('cidadeAnanindeua'), Data_Solicitacao = request.form.get("dataSolicitacao"))

    return render_template("homepage.html", resultado=resultado)
@Telas.route("/homepage2", methods=['POST','GET'])
def homepage2():
    if 'username' not in session:
        return redirect(url_for('Telas.login'))

    resultadoVencimento = MudarVen(vAtual=request.form.get('vencimentoAtual'), vNovo=request.form.get('vencimentoNovo'), vPlano=request.form.get('planoCliente'), checkA=request.form.get('cidadeAnanindeua'), Data_Solicitacao = request.form.get("dataSolicitacao"))

    return  render_template("homepage2.html", resultadoVencimento = resultadoVencimento)
@Telas.route("/homepage3", methods=['POST','GET'])
def homepage3():
    if 'username' not in session:
        return redirect(url_for('Telas.login'))

    resultadoDesc =  CalculoDesc(Plano = request.form.get('Plano'),D = request.form.get('D'), M = request.form.get('M'), Data_Solicitacao = request.form.get("dataSolicitacao"))
    return render_template("homepage3.html", resultadoDesc = resultadoDesc)

@Telas.route("/homepage4", methods=['POST','GET'])
def homepage4():
    if 'username' not in session:
        return redirect(url_for('Telas.login'))

    resultado_cancelamento = Calculo_cancelamento(pAtual = request.form.get("Plano_cancelamento"), pVen = request.form.get("vencimento_cancelamento"), Data_Solicitacao = request.form.get("dataSolicitacao"),data_ati = request.form.get("data_ati"),multa=request.form.get("multa"))
    return render_template("homepage4.html", resultado_cancelamento=resultado_cancelamento)

@Telas.route("/homepage5", methods=['POST','GET'])
def homepage5():
    if 'username' not in session:
        return redirect(url_for('Telas.login'))

    campos_adicionais = []
    for key, value in request.form.items():
        if key.startswith('data') or key.startswith('valor') or key.startswith('dias') or key.startswith('multa') or key.startswith('juros') or key.startswith('cobrar'):
            campos_adicionais.append(value)
    try:
        r = Calculo_negociacao(campos_adicionais)
        return render_template("homepage5.html", resultados=r)
    except ValueError:

        return render_template("homepage5.html", resultados= "!!!", error="Error no envio do formulario (Vazio)" )

@Telas.route("/homepage6", methods=['POST','GET'])
def homepage6():
    if 'username' not in session:
        return redirect(url_for('Telas.login'))

    if 'homepage6' not in users[session['username']]['permissoes']:
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








