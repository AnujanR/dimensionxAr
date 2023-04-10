FROM python:3.8-slim
ENV PYTHONUNBUFFERED=1
EXPOSE 8000

WORKDIR /EvoAR
COPY requirements.txt .
RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y git
RUN pip install -r requirements.txt -v
COPY . .
CMD python manage.py runserver 0.0.0.0:8000
