FROM node:10.16.0-alpine

# set the working directory inside the container
# if we have an existing app folder use it or create a new one.
WORKDIR /app

# add the package .JSON in our app dir | The Caching
ADD package*.json ./

# Run cmd allows us to pass arguments i.e npm install all
# all packages dependencies for our JSON
RUN npm install

# add everything inside this directory to the app dir
ADD . .

# Command to execute to start our node server
CMD node index.js