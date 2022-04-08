FROM python:3.10-alpine
RUN apk add --update --no-cache chromium chromium-chromedriver build-base libffi-dev

RUN pip3 install Flask selenium
COPY src/ /app/
CMD ["python3", "/app/app.py"]
