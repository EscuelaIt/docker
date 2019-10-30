FROM ubuntu:19.10

RUN mkdir /code

WORKDIR /code

RUN apt-get update

RUN apt-get install -y nginx

RUN echo "Hello World"

ADD example.sh /code/

RUN chmod +x example.sh

RUN ./example.sh
