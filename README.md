# Get ready to print some PDFs!

## Version with two separately running Docker containers

Required: You have a working installation of Docker

### To get the PDF service running:
From the repo root run
```console
cd backend
```
Build the container image and it interactively to log errors
```console
docker build -t flaskbackend . && docker run -p 5000:5000 flaskbackend # could use -d to detach container ps from terminal
```

Access it by visiting localhost:5000 in your favorite browser

### To get the 'fake frontend' server running:
From the repo root run
```console
cd frontend
```
Build the container image and it interactively to log errors
```console
docker build -t vuefrontend . && docker run -p 8080:8080 vuefrontend # could use -d to detach container ps from terminal
```

Access it by visiting localhost:8080 in your favorite browser. Click the button do preview/download a simple PDF from the python microservice.

## Version with Docker-Compose
tbd
