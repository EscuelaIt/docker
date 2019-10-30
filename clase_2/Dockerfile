FROM node:10

RUN npm install -g yarn

RUN npm install nodemon -g

RUN mkdir /code

WORKDIR /code

ADD app.js /code/

ADD package.json /code/

ADD yarn.lock /code/

RUN yarn install --modules-folder /node_modules

EXPOSE 3000

CMD [ "nodemon", "app.js" ]