FROM python:3-slim

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY hotsauce.py /app

ENV FLASK_APP=hotsauce.py

CMD [ "flask", "run", "--host=0.0.0.0" ]
