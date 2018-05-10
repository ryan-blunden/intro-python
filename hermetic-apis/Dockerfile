FROM nginx:1.13-alpine

LABEL maintainer="Ryan Blunden <ryan.blunden@rabbitbird.com>"

WORKDIR /var/www/

HEALTHCHECK CMD curl --fail http://localhost/api/v1/health-check/ || exit 1

RUN apk update && \
    apk upgrade && \
    apk add curl

RUN rm /etc/nginx/conf.d/default.conf
