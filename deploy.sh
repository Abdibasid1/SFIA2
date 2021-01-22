scp docker-compose.yaml $USER@swarm-manager:docker-compose.yaml
ssh $USER@swarm-manager << EOF
export DATABASE_URI=${DATABASE_URI}
docker stack deploy --compose-file docker-compose.yaml SFIA2
EOF