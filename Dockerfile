FROM python:alpine3.22

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /app/src

CMD ["python", "src/app.py"]
