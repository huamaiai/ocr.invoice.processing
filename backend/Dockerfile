FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    poppler-utils \
    tesseract-ocr \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Set up working directory
WORKDIR /app

# Copy only requirements.txt first to leverage Docker cache
COPY ../requirements.txt /app/requirements.txt

# Copy backend app source code
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
