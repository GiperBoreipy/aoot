FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /server/

RUN pip install poetry

COPY pyproject.toml poetry.lock* ./

RUN poetry install 

COPY . ./

