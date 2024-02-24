FROM ubuntu:latest as dev

WORKDIR /app

COPY . .

RUN apt-get update && \
    apt-get install -y nodejs npm

RUN npm install

#RUN node app.js

CMD ["bash", "-c", "while true; do sleep 3600; done"]