FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY main.py /app/main.py

CMD ["python", "main.py"]
