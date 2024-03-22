FROM python:3.10.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./api .

EXPOSE 5050

CMD ["flask", "run", "--host=0.0.0.0", "--port=5050"]