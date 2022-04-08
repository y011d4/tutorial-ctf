FROM python:3.10-alpine
RUN apk add --update --no-cache chromium chromium-chromedriver

RUN pip3 install Flask selenium
COPY src/ /app/
CMD ["python3", "/app/app.py"]
