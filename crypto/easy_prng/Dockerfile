FROM python:3.10-slim-buster
RUN apt update -y && apt install -y socat && rm -rf /var/lib/apt/lists/*

RUN pip3 install pycryptodome
COPY src/ /app/
CMD ["socat", "tcp4-listen:1337,reuseaddr,fork", "system:python3 /app/challenge.py"]
