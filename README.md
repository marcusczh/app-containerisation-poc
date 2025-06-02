# app-containerisation-poc

A minimal application to demostrate how containerisation can be used to achieve zero downtime during updates

## Method 1 - nginx
Create the docker image and container and run the script to verify the version number
```
docker-compose up -d --build
python script.py
```
Modify app version to simulate an update
```
const VERSION = {NEW_VERSION};
```
Build only the app1 container and run the script to verify the version number and responsiveness
```
docker-compose up -d --build app1
python script.py
```
Build only the app2 container and run the script to verify the version number and responsiveness
```
docker-compose up -d --build app2
python script.py
```

## Method 2 - Kubernetes
Create the docker image 
```
docker build -t app .
```
Apply the Kubernetes configurations
```
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```
Obtain the deployment port and run the script with the amended URL
```
kubectl get svc app
python script.py
```
Modify app version to simulate an update
```
const VERSION = {NEW_VERSION};
```
Build the new docker image and restart the deployment and run the script to verify the new version number and responsiveness
```
docker build -t app .
kubectl rollout restart deployment/app
python script
```