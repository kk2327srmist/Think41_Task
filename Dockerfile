FROM python:3.10-slim
WORKDIR /app
COPY backend/ ./
RUN pip install -r requirements.txt
CMD ["python", "app.py"]

