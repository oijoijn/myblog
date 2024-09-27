FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN useradd -ms /bin/bash soto
USER soto

WORKDIR /home/soto

COPY requirements.txt .
RUN pip install --upgrade pip setuptools
RUN pip install -r requirements.txt

COPY . .
