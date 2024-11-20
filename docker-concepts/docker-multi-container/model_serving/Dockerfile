FROM python:3.9-slim
WORKDIR /app
COPY app.py model.pkl ./
RUN pip install flask scikit-learn
CMD ["python", "app.py"]
