# Clase 3

Comandos empleados en esta clase:

```
docker build . --tag clase_3:lastest
docker run --name clase_3_1 -it -v /Users/carlosmart/Repos/EscuelaIT/Docker/clase_3:/code clase_3:lastest bash
docker rm -f clase_3_1
docker run --name clase_3_1 clase_3:lastest
docker run --name clase_3_1 -it clase_3:lastest bash
docker run --name clase_3_1 -p 8001:8001 -v /Users/carlosmart/Repos/EscuelaIT/Docker/clase_3:/code clase_3:lastest
docker run --name clase_3_1 -p 127.0.0.1:8001:8001 --env-file ./.env clase_3:lastest


# List Docker Components

# Images
docker images

# Containers
docker ps

# Volumes
docker volume ls

# Networks
docker network ls


# Clean
docker rm $(docker ps -qa --no-trunc --filter "status=exited")
docker rmi $(docker images --filter "dangling=true" -q --no-trunc)

docker volume rm $(docker volume ls -qf dangling=true)
docker network rm $(docker network ls | grep "bridge" | awk '/ / { print $1 }')
```