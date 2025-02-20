# Usa una imagen base con Python 3.13.1
FROM python:3.11-slim

# Instalar cliente de PostgreSQL
RUN apt update && apt install -y postgresql-client

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt /app/

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos del proyecto al contenedor
COPY . /app/

# Expone el puerto 5002, que es el puerto donde Flask escuchará
EXPOSE 5012

# Comando para ejecutar la aplicación Flask cuando el contenedor se inicie
CMD ["python", "app.py"]
