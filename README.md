# Get ready to print some PDFs!

## Version with two separately running Docker containers

Required: You have a working installation of Docker

### To get the PDF service running:
From the repo root run
```console
cd backend
```
Build the container image and make it interactively to log errors
```console
docker build -t flaskbackend . && docker run -p 5000:5000 flaskbackend
```

Access it by visiting http://localhost:5000 in your favorite browser. Now you could send a post request to http://localhost:5000/pdf, e.g. with [Postman](https://www.getpostman.com/), do download a PDF.

### To get the 'fake frontend' server running:
From the repo root run
```console
cd frontend
```
Build the container image and make it interactively to log errors
```console
docker build -t vuefrontend . && docker run -p 8080:8080 vuefrontend
```

Access it by visiting http://localhost:8080 in your favorite browser. Click the button do preview/download a simple PDF from the python microservice.

You could use -d on the `docker run` command in both cases to separate (d for detach) terminal ps from container ps.

## Version with Docker-Compose

Required: You have a working installation of both Docker and Docker Compose

Build and run the containers with
```console
docker-compose up
```
Access the backend server by visiting http://localhost:5000 in your favorite browser. Now you could send a post request to http://localhost:5000/pdf, e.g. with Postman, do download a PDF.

Access the frontend server by visiting http://localhost:8080 in your favorite browser. Click the button do preview/download a simple PDF from the python microservice.
