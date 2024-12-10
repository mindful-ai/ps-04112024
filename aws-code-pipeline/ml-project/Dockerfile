FROM python:3.8-slim
COPY model.pkl /app/
COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "-m", "http.server", "8080"]
