FROM node:16-buster-slim
WORKDIR /opt/star-burger
COPY package.json .
COPY package-lock.json .
RUN npm ci --include=dev
COPY ./bundles-src/ ./bundles-src/
RUN ./node_modules/.bin/parcel build bundles-src/index.js --dist-dir bundles --public-url="./"