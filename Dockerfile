FROM python:3.11-slim

# Definindo o diretório de trabalho dentro do container
WORKDIR /app

# Copiando os arquivos do projeto para o diretório de trabalho
COPY . /app

# Comando para rodar o CRUD 
CMD ["python", "crud_alunos.py"]
