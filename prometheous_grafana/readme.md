# Prometheous and grafana example

## Deploy prometheous (minikube)

[used material](https://semaphoreci.com/blog/prometheus-grafana-kubernetes-helm)

```
helm search hub prometheus

helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo list
helm search repo prometheus
helm repo update

kubectl create namespace promethous-grafana

helm install prometheus prometheus-community/prometheus --namespace promethous-grafana

## test
kubectl get all -n promethous-grafana
(
kubectl expose service prometheus-server --type=NodePort --target-port=9090 --name=prometheus-server-ext -n promethous-grafana

kubectl get pods -l app.kubernetes.io/instance=prometheus -n promethous-grafana

minikube service prometheus-server-ext -n promethous-grafana
)

or
kubectl port-forward service/prometheus-server -n promethous-grafana 9090:80
localhost:9090
```


## Deploy Grafana
```
helm search hub grafana
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
helm install grafana grafana/grafana --namespace promethous-grafana

kubectl expose service grafana --type=NodePort --target-port=3000 --name=grafana-ext -n promethous-grafana

minikube service grafana-ext -n promethous-grafana

#user admin pw admin
kubectl get secret --namespace promethous-grafana grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo

minikube service grafana-np

or
kubectl port-forward service/grafana -n promethous-grafana 3000:80

```

## deploy test app

... helm repo

## Configure prometheus

Solutin 1: (configure to scrap the pod endpoint)

kubectl get configmap prometheus-server -n promethous-grafana -o yaml > prometheus_config_tmp.yaml

or

kubectl edit configmap ...

- job_name: example-app       #scrap my pods data
    static_configs:
    - targets: ['example-app-prometheous.exampleapp-ns.svc.cluster.local:8080']

kubectl apply -f prometheus_config.yaml -n promethous-grafana


kubectl port-forward service/prometheus-server -n promethous-grafana 9090:80


## Grafana 

Data source:
    http://prometheus-server:80/

