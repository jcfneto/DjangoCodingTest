FROM python:3.8-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /igsesm
WORKDIR /igsesm
COPY requirements.txt /igsesm/
RUN pip install -r requirements.txt
COPY . /igsesm/