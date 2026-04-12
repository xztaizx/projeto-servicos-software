FROM node:18
 
WORKDIR /app
 
RUN npm install -g serve
 
COPY ./src .
 
CMD ["serve", "-s", ".", "-l", "3000"]