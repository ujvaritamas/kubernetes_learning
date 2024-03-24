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


helm install <name> <chart> 
helm upgrade <release> <chart> 
helm list --all-namespaces


Argocd:
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

kubectl get services -n argocd
minikube service argocd-server -n argocd
username: admin
kubectl get secret argocd-initial-admin-secret -n argocd -o yaml
echo <pw> | base64 --decode
echo TU4wZnZIa3JaY3JYREN2Wg== | base64 --decode
(%not needed)
