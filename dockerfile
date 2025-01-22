# Use uma imagem Python como base
FROM python:3.10

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie os arquivos do projeto para o contêiner
COPY . .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Comando para rodar a aplicação
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]