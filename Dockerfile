FROM python:3.13.3
WORKDIR /app
COPY . .
RUN pip install pandas scikit-learn firebase-admin
CMD ["python", "main.py"]
