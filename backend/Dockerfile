FROM python:3.10-slim

WORKDIR /app

# Copy only requirements.txt first to leverage Docker cache
COPY ../requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

# Copy backend app source code
COPY . /app

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
