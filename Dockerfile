FROM python:3.9.9-slim-bullseye

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "--chdir", "api/src", "--bind", "0.0.0.0:$PORT", "app:app"]