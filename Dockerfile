FROM python:3.10

# Insecure: running as root
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

CMD ["python", "app/main.py"]