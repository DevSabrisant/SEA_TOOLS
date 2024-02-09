from flask import request, render_template, Blueprint
from blueprints.swich_calculo import *
from blueprints.mudar_venc import *
from blueprints.calculos import *

Telas = Blueprint('Telas', __name__)

@Telas.route("/", methods=['POST','GET'])
def Home():
    return render_template('index.html')

@Telas.route("/homepage", methods=['POST', 'GET'])
def homepage():
    resultado = venc(pVen=request.form.get('vencimento'), pAtual=request.form.get('planoAtual'), pNovo=request.form.get('planoNovo'), checkA=request.form.get('cidadeAnanindeua'))

    return render_template("homepage.html", resultado=resultado)
@Telas.route("/homepage2", methods=['POST','GET'])

def homepage2():
    resultadoVencimento = MudarVen(vAtual=request.form.get('vencimentoAtual'), vNovo=request.form.get('vencimentoNovo'), vPlano=request.form.get('planoCliente'), checkA=request.form.get('cidadeAnanindeua'))

    return  render_template("homepage2.html", resultadoVencimento = resultadoVencimento)
@Telas.route("/homepage3", methods=['POST','GET'])

def homepage3():
    resultadoDesc =  CalculoDesc(Plano = request.form.get('Plano'),D = request.form.get('D'), M = request.form.get('M'))
    return render_template("homepage3.html", resultadoDesc = resultadoDesc)
