FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install streamlit requests

CMD ["streamlit", "run", "hitl_app.py", "--server.port=8501", "--server.enableCORS=false"]
