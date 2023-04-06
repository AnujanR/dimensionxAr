FROM python:3.9-alpine
ENV PYTHONUNBUFFERED=1

WORKDIR /EvoAR
COPY requirements.txt .
RUN pip install --upgrade pip
RUN apk add --no-cache git
RUN pip install -r requirements.txt -v
COPY . .
CMD python manage.py runserver 0.0.0.0:80