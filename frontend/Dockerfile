FROM python:3.11

# define pasta dentro do container
WORKDIR /app

# copia dependências
COPY requirements.txt .

# instala libs
RUN pip install --no-cache-dir -r requirements.txt

# copia código
COPY . .

# comando que roda o app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7560"]