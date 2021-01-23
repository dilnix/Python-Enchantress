# Use following commands to build and start:

`docker build -t age_form .` to build image according to Dockerfile

`docker run -it --rm -p 8080:8080 --name running_age_form age_form` to run container from built image with several options about interaction, ports, name and autoremove after stop

### Follow to http://localhost:8080/ to get running page and try to use it.

# Instead of running "docker run" with a lot of arguments you can try to use a prepared docker-compose.yml with simple commands:

`docker-compose build` to build image according to rules specified in docker-compose.yml
`docker-compose up -d` to start container from built image in daemon mode
`docker-compose ps` to see running container short info
`docker-compose stop` to stop container
`docker-compose rm` to remove container
