FROM python:3.8

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python3"]

CMD ["app.py"]