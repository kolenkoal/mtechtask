FROM python:3.9

RUN apt-get update && apt-get install -y postgresql-client

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

COPY ./core/schemas/scripts/db.sql /docker-entrypoint-initdb.d/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
