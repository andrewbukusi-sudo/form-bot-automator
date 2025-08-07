FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive

# Install Chromium and ChromeDriver
RUN apt-get update && apt-get install -y \
    chromium-driver \
    chromium \
    curl \
    unzip \
    gnupg \
    && apt-get clean

# Set environment variables for Selenium
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy app files
COPY . /app
WORKDIR /app

# Start the app
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]
