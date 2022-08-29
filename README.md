# Kafka Handlers

Kafka handlers simple example

Requirements:
- kubernetes cluster with `kubectl`/`helm` connected
- kafka cluster with user / topic / consumer group configured (see [source](app/consumer.py) for defaults)

How to build and run in docker:

```
docker build -t evnp/kafka-handlers
docker run -it --rm -e SERVERS=<kafka-cluster-address+port> evnp/kafka-handlers
```

How to run in kubernetes with [KEDA](https://keda.sh/docs/2.8/scalers/apache-kafka/):

```
helm repo add kedacore https://kedacore.github.io/charts
helm install keda kedacore/keda --namespace keda --create-namespace
kubectl logs -l app.kubernetes.io/instance=keda -n keda -f

docker push evnp/kafka-handlers

helm install handlers charts/kafka-handlers --set connection.servers=<kafka-cluster-address+port>
kubectl get pods -l app=kafka-handlers -w
kubectl logs -l app=kafka-handlers -f
```

How to produce test message in both cases:

```
docker run -it --rm -e SERVERS=<kafka-cluster-address+port> evnp/kafka-handlers python /app/producer.py
```
