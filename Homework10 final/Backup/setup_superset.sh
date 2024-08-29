#!/bin/bash

# Set environment variables
export SECRET_KEY='nw+gZEP1CcvQo1tgkcG92fB6rVu24gBwu0bbzuISq5ccZIkBIa4Nx/K9'
export POSTGRES_USER='superset'
export POSTGRES_PASSWORD='superset'
export POSTGRES_DB='superset'

# Pull the necessary images
docker pull postgres:13
docker pull apache/superset

# Create network and volume
docker network create superset_network
docker volume create superset_db_data

# Start PostgreSQL container
docker run -d --name superset_db --network superset_network \
  -e POSTGRES_USER=$POSTGRES_USER \
  -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD \
  -e POSTGRES_DB=$POSTGRES_DB \
  -v superset_db_data:/var/lib/postgresql/data \
  postgres:13

# Start Superset container
docker run -d --name superset --network superset_network \
  -e SUPERSET_ENV=production \
  -e SECRET_KEY=$SECRET_KEY \
  -p 8088:8088 \
  -v $(pwd)/superset_config/superset_config.py:/app/pythonpath/superset_config.py \
  apache/superset

# Wait for Superset to start
echo "Waiting for Superset to start..."
sleep 30

# Initialize the Superset database
docker exec superset superset db upgrade

# Create an admin user
docker exec -it superset superset fab create-admin --username admin --password admin --firstname Admin --lastname User --email admin@admin.com

# Initialize Superset
docker exec superset superset init

# Output the URL for accessing Superset
echo "Superset is now running at http://localhost:8088"