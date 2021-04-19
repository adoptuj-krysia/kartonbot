FROM python:3.8-slim-buster

COPY ./src /opt/kartonbot
WORKDIR /opt/kartonbot

RUN python3 -m pip install -r requirements.txt
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y ffmpeg

CMD [ "python3", "start.py"]
