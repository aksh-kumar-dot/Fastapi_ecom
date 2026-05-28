FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /usr/src/app


COPY requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt

COPY . .

