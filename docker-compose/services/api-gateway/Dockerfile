FROM node
# https://www.npmjs.com/package/express-gateway

WORKDIR /home/node

RUN npm install -g express-gateway
COPY ./src/Gateway/ /home/node/Gateway
WORKDIR /home/node/Gateway
RUN npm install

RUN eg plugins install --enable y --update-gateway-config n express-gateway-plugin-rewrite
COPY ./src/docker-config/ /home/node/Gateway/config/

#RUN eg plugins install express-gateway-plugin-rewrite
EXPOSE 8080
