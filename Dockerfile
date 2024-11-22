FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# ENV PYTHONPATH=/usr/local/lib/python3.8/site-packages:$PYTHONPATH

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# RUN apt update && apt install -y tree

COPY . .

RUN useradd -ms /bin/bash soto
USER soto
WORKDIR /home/soto
