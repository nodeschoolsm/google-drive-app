FROM python:3.8

WORKDIR /code

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 4000

COPY . .

CMD ["python3", "app.py"]