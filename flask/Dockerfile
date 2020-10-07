FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /api
ADD ./api /api

RUN ./setup.sh

CMD ["python3", "/api/app.py"]
