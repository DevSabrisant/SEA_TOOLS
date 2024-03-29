import pandas as pd
from io import BytesIO
import base64

def lista_cliente(cidade, protocolo, xls_data):
    clientes = []
    idade = []

    for xls_file in xls_data:
        if 'nome' in xls_file.columns:
            clientes.extend(xls_file['nome'].tolist())
        if 'idade' in xls_file.columns:
            idade.extend(xls_file['idade'].tolist())


    df = pd.DataFrame({
        'Nome': clientes,
        'Idade': idade
    })

    df = df.sort_values(by='Nome', ascending=True)

    return df

def imagem_comunicado(img_file):
    if (img_file is not None and img_file != ''):
        img_content = img_file.read()
        img_base64 = base64.b64encode(img_content).decode('utf-8')

        return img_base64