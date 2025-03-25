
# Dockerfile for Streamlit app
FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["streamlit", "run", "app/streamlit_predictflowai.py", "--server.port=8501", "--server.address=0.0.0.0"]
