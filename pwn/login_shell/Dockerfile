FROM python:3.10-slim-buster
RUN apt update -y && apt install -y socat && rm -rf /var/lib/apt/lists/*

COPY src/ /app/
WORKDIR /app
CMD ["socat", "tcp4-listen:1337,reuseaddr,fork", "system:/app/vuln"]
