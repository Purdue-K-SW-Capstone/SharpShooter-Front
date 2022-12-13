FROM node:16

#install dependencies
COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 8081
EXPOSE 3333

CMD ["npm", "start"]

