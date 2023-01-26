FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN apt-get update


WORKDIR /etc/app

COPY . .


RUN pip install -r requirements.txt

