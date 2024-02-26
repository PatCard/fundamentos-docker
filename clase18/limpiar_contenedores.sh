#!/bin/bash

# Detener y eliminar los contenedores
docker-compose down

# Eliminar volúmenes no utilizados
docker volume prune -f

# Eliminar las imágenes
docker rmi -f backend
docker rmi -f frontend
