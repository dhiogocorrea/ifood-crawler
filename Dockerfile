FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

COPY requirements.txt .

RUN  apt-get update && \
     pip install -r requirements.txt

COPY ./app /app

