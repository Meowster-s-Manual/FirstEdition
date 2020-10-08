FROM node:14-buster

WORKDIR /client

COPY package.json ./

RUN npm install -g @vue/cli

RUN npm install

CMD vue ui -H 0.0.0.0 -p 8081