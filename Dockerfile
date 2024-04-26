# Usa uma imagem base do Python 3.10
FROM python:3.10.7

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o conteúdo do diretório atual para o contêiner
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta da aplicação
EXPOSE 5000

# Comando para rodar a aplicação quando o contêiner for iniciado
CMD ["python", "app.py"]


