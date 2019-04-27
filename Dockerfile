FROM python:3.5-slim

MAINTAINER mayankkapoormail@gmail.com, dineshkumar13506@gmail.com

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# Create app directory
WORKDIR /usr/src/app

# Install required software
RUN    apt-get update \
    && apt-get install -y putty-tools
RUN    pip install pathlib \
    && pip install Flask \
    && pip install flask_json

# Bundle app source code
COPY app.py .

EXPOSE 5000
ENTRYPOINT ["python", "/usr/src/app/app.py"]
