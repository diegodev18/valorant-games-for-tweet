FROM python:3

WORKDIR /

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "index.py"]