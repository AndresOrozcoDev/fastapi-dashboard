# Usa la imagen base de Python 3.9
FROM python:3.11

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo de requerimientos e instala las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todos los archivos de la aplicación al contenedor
COPY . .

# Exponer el puerto 80 para acceder al servidor web
EXPOSE 8000

# Especifica el comando de inicio para FastAPI
CMD ["bash", "-c", "python main.py"]
