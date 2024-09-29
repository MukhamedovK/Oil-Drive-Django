FROM python:latest

# Установите переменные среды
ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY . /code/

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]