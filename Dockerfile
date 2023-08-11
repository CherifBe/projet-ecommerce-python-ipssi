FROM python:3.11.3

WORKDIR /usr/src/application

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

RUN export DATABASE_URL=mysql+aiomysql://root:testing@db/testing

COPY . .

RUN alembic upgrade head

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
