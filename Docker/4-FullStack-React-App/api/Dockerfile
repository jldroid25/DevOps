FROM node

WORKDIR  /home/ec2-user/environment/

COPY .  package*.json ./

RUN npm install

COPY . .

EXPOSE 4000

CMD [ "npm", "start"]