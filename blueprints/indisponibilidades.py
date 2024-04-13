import pandas as pd
import io
from database.models.indispinibilidades import Indisponibilidade
from database.database import db
from flask import send_file

def salvar_dados(xls_data, img_file, cidade, protocolo, status, filename):
    # Criar listas para armazenar os dados dos clientes, códigos e CTOs
    clientes = []
    codigo = []
    CTO = []
    codigo_cliente_ajustado = []
    for xls_file in xls_data:

        if 'Elemento de Conexão' in xls_file.columns and 'Cliente' in xls_file.columns:
            # Iterar sobre as linhas do DataFrame atual
            for xls_file in xls_data:
                if 'Elemento de Conexão' in xls_file.columns and 'Cliente' in xls_file.columns:
                    # Iterar sobre as linhas do DataFrame atual
                    for index, row in xls_file.iterrows():
                        # Extrair o dado da coluna 'Cliente'
                        cliente_info = row['Cliente']

                        # Encontrar a posição da palavra "Cliente:"
                        codigo_start = cliente_info.find('Cliente:') + len('Cliente:')  # Encontrar o início do código
                        nome_end = cliente_info.find('-')  # Encontrar o fim do nome

                        # Extrair o código do cliente
                        codigo_cliente = cliente_info[codigo_start:nome_end].strip()
                        codigo.append(codigo_cliente)  # Adicionar código do cliente à lista

                        # Extrair o nome do cliente
                        nome_cliente = cliente_info[nome_end + 1:].strip()
                        clientes.append(nome_cliente)  # Adicionar nome do cliente à lista

                        # Adicionar o CTO à lista
                        CTO.append(row['Elemento de Conexão'])

            # Ajustar códigos duplicados
            codigo_duplicado = set()
            for codigo_cliente in codigo:
                if codigo.count(codigo_cliente) > 1 and codigo_cliente not in codigo_duplicado:
                    codigo_cliente_ajustado.append(' - ' + codigo_cliente + ' - ')
                    codigo_duplicado.add(codigo_cliente)
                else:
                    codigo_cliente_ajustado.append(codigo_cliente)

    Indisponibilidade.create(
            nomes_clientes=clientes,
            codigos_clientes=codigo_cliente_ajustado,
            cto_clientes=CTO,
            foto=img_file.read(),
            cidade=cidade,
            protocolo=protocolo,
            status=status,
            nome_arquivo=filename
        )
def listar_indisponibilidades():

    dados = Indisponibilidade.select()

    lista_dados = []

    for dado in dados:
        lista_dados.append({
            'protocolo': dado.protocolo,
            'cidade': dado.cidade,
            'status': dado.status
        })

    return lista_dados

def detalhes(protocolo):
    indisponibilidade = Indisponibilidade.get_or_none(Indisponibilidade.protocolo == protocolo)

    if not indisponibilidade:
        return 'Indisponibilidade não encontrada'

    extensao = indisponibilidade.nome_arquivo.split('.')[-1]

    if extensao.lower() in ['jpg', 'jpeg']:
        mimetype = 'image/jpeg'
    elif extensao.lower() == 'png':
        mimetype = 'image/png'
    else:
        mimetype = 'image/png'

    dados_indis = [indisponibilidade.protocolo, indisponibilidade.cidade, indisponibilidade.status]

    dados_nome_clientes = indisponibilidade.nomes_clientes.strip("[]").replace("'", "").split(',')
    dados_cod_clientes = indisponibilidade.codigos_clientes.strip("[]").replace("'", "").split(',')

    dados_combinados = []
    for codigo, nome in zip(dados_cod_clientes, dados_nome_clientes):
        dados_combinados.extend([codigo, nome])

    dados_combinados.extend(dados_indis)

    return dados_combinados, indisponibilidade.foto, mimetype

def Deletar(protocolo):

    indisponibilidade = Indisponibilidade.get(Indisponibilidade.protocolo == protocolo)

    indisponibilidade.delete_instance()




