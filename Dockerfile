FROM pytorch/pytorch:2.6.0-cuda11.8-cudnn9-runtime

WORKDIR /app

COPY requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "--chdir", "api/src", "--bind", "0.0.0.0:$PORT", "app:app"]