FROM python:3.11-slim

RUN apt-get update && apt-get install -y     chromium chromium-driver &&     pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]