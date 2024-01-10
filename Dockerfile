FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY . /app

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]