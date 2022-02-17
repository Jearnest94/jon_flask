FROM python:3.9

WORKDIR /app

ADD . /app

# Installera requirments från requirements.txt
RUN pip install -r requirements.txt

CMD ["uwsgi", "app.ini"]
