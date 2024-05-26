FROM python:3.10-slim-buster

WORKDIR .
COPY . .
RUN apt-get update && apt-get install -y ffmpeg git
RUN pip3 install -r requirements.txt

ENV PORT = 8000
EXPOSE 8000

CMD python3 -m bot
