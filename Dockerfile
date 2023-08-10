FROM python:3.11.3

WORKDIR /usr/src/application

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["flask", "--app", "main", "run", "--reload"]