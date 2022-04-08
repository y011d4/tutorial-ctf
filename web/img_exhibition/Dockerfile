FROM python:3.10-slim-buster
RUN apt update -y && apt install -y socat && rm -rf /var/lib/apt/lists/*

RUN pip3 install Flask selenium
COPY src/ /app/
CMD ["python3", "/app/app.py"]
