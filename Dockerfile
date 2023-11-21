# Verwende das offizielle Python-Image als Basis
FROM python:3.8-slim

# Setze das Arbeitsverzeichnis innerhalb des Containers
WORKDIR /app

# Kopiere die Anwendungsdateien in das Arbeitsverzeichnis des Containers
COPY doner_service.py /app/
COPY templates /app/templates

# Installiere die erforderlichen Python-Pakete
RUN pip install Flask

# Setze Umgebungsvariable für Flask
ENV FLASK_APP=doner_service.py

# Öffne den gewünschten Port
EXPOSE 5000

# Starte die Anwendung beim Start des Containers
CMD ["flask", "run", "--host=0.0.0.0"]
