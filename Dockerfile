FROM python:3.11.3

WORKDIR /usr/src/application

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DATABASE_URL=mysql+aiomysql://root:testing@db:3306/testing

RUN export DATABASE_URL=${DATABASE_URL}

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
