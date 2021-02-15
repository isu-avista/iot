FROM node:lts-alpine as build-stage

# make the 'app' folder the current working directory
WORKDIR /app

# copy both 'package.json' and 'package-lock.json' (if available)
COPY ./package*.json ./

# install project dependencies
RUN npm install -g npm@7.5.4
RUN npm install

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY ./ ./

# build app for production with minification
RUN npm run build


FROM nginx as production-stage
RUN mkdir /app
COPY --from=build-stage /app/dist /app
COPY nginx.conf /etc/nginx/nginx.conf

#CMD [ "http-server", "dist"]
CMD ["nginx", "-g", "daemon off;"]
