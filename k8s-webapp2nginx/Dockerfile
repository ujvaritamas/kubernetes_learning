FROM ubuntu:latest as dev

RUN apt-get update && \
    apt-get install -y nodejs npm

WORKDIR /app

EXPOSE 3000

COPY package.json package-lock.json ./

#RUN npm install node-fetch
RUN npm install

COPY . ./

#CMD ["node", "app.js"]

CMD ["npm", "start"]

#CMD ["bash", "-c", "while true; do sleep 3600; done"]