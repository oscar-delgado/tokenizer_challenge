# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN [ "python", "-c", "import nltk; nltk.download('stopwords'); nltk.download('punkt')" ]
COPY . /code/
CMD gunicorn tokenizer_challenge.wsgi:application --bind 0.0.0.0:$PORT