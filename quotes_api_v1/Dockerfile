FROM python:3.8-slim

LABEL version="1.0" maintainer="Marcelo Gonçalves"

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN useradd -ms /bin/bash back-user

USER back-user 

WORKDIR /home/back-user

COPY back.py .

ENTRYPOINT python back.py