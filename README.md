# kubernetes_learning
Basic kubernetes examples

docker build -t k8s-webapp .

docker build . -t tamasujvari/k8s-webapp

docker login

docker push <imagename>

docker run -v /host/path:/app/data --name <container name> <image_name> -d


#after service created with --type=NodePort --port=3000

minikube service k8s-webapp --url
minikube service k8s-webapp
