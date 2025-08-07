FROM python:3.11-slim

# Prevent prompts from popping up
ENV DEBIAN_FRONTEND=noninteractive

# Install required system packages
RUN apt-get update && apt-get install -y \
    chromium-driver \
    chromium \
    curl \
    unzip \
    gnupg \
    && apt-get clean

# Set environment variables for Chromium
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy source code
COPY . /app
WORKDIR /app

# Start the Flask server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]
