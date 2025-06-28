# Usa Python 3.10
FROM python:3.10-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos al contenedor
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Expone el puerto que usará Uvicorn
EXPOSE 10000

# Comando para iniciar la API y el bot
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]

