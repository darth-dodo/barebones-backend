FROM python:alpine3.7
COPY . /app
WORKDIR /app
EXPOSE 8000
CMD python ./barebones_server.py