# Docker to K8s

This is a todo web app created using Django and Postgres. It is used to demonstrate how to deploy a web app and its database using Docker and Kubernetes.

## Run using Docker

To start the project using Docker:

```
docker-compose up --build
```

## Run using Kubernetes

To start the project using Docker:

```
cd k8s/

kubectl apply -f persistent-volume.yaml
kubectl apply -f secret.yaml
kubectl apply -f config.yaml
kubectl apply -f db-deployment.yaml
kubectl apply -f app-deployment.yaml
```