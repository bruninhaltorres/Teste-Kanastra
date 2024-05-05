FROM python:3.10

# Define variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copia o código fonte do backend
COPY ./backend ./backend

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY ./backend/requirements.txt ./

# Instalação das dependências do backend
RUN pip install Django==5.0.4
RUN pip install gunicorn
RUN pip install -r requirements.txt

# Copia o código fonte do frontend
COPY ./frontend/app /frontend/app

# Prepara o ambiente do frontend e instala as dependências
RUN apt-get update && apt-get install -y nodejs npm
RUN npm install --prefix /frontend/app

# Compilação do frontend
RUN npm run build --prefix /frontend/app

# Expose a porta 8000 para o servidor web do backend
EXPOSE 8000

# Comando para iniciar o aplicativo usando Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.setup.wsgi"]
