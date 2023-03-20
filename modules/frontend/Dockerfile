FROM node:14.8-alpine3.11

WORKDIR .

COPY package.json ./
COPY package-lock.json ./

RUN npm install
RUN npm install react-scripts@3.4.3 -g

CMD ["pwd"]
COPY . ./

EXPOSE 3000

CMD ["npm", "start"]

