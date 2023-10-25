FROM nginx:1.21-alpine

RUN rm /etc/nginx/conf.d/default.conf
WORKDIR /code
COPY . .
COPY ./nginx/nginx.conf /etc/nginx/
