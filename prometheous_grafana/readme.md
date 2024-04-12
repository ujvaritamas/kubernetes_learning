# Prometheous and grafana example

## Install prometheous (minikube)

[used material](https://semaphoreci.com/blog/prometheus-grafana-kubernetes-helm)

```
helm search hub prometheus

helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo list
helm search repo prometheus
helm repo update

kubectl create namespace promethous-grafana

helm install prometheus prometheus-community/prometheus --namespace promethous-grafana


kubectl get all -n promethous-grafana

kubectl expose service prometheus-server --type=NodePort --target-port=9090 --name=prometheus-server-ext -n promethous-grafana

kubectl get pods -l app.kubernetes.io/instance=prometheus -n promethous-grafana

minikube service prometheus-server-ext -n promethous-grafana
```


## Install Grafana
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
```