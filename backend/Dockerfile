FROM python:3.10.7

WORKDIR /fastapi-app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./backend ./backend

CMD ["python", "./backend/main.py"]