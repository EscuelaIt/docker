# Clase 4

Comandos empleados en esta clase:

```
# Docker compose common commands
docker-compose up
docker-compose stop
docker-compose down

# Build docker images
docker-compose build
docker-compose build --no-cache

# Start, Stop one service
docker-compose up {service_name}
docker-compose stop {service_name}

# Get in the containers
docker exec -it clase_4_cool_app_1 bash
docker exec -it clase_4_postgres_1 bash
```