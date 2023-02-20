FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apt-get update
WORKDIR /bolid
COPY requirements.txt /bolid/
RUN pip install -r requirements.txt
COPY ./bolid /bolid/