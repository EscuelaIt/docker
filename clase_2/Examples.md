# Clase 2

Comandos empleados en esta clase:

```
docker build .
docker build . --tag clase_1:lastest
docker build . --tag clase_1:1.0.0
docker run --name clase_1_1 clase_1:lastest
docker run --name clase_1_1 -p 3000:3000 clase_1:lastest
docker exec -it clase_1_1 bash
docker run --name clase_1_1  -p 3031:3000 -v /Users/carlosmart/Repos/EscuelaIT/DockerLive/clase_2:/code clase_2:lastest
docker exec -it clase_1_1 bash

docker images
docker ps
docker ps -a
docker rm {container_id}
docker rm -f {container_id}
```