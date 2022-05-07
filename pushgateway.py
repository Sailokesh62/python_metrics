from prometheus_client import CollectorRegistry,Gauge,push_to_gateway
import random


registry=CollectorRegistry()

guage= Gauge('errors_now','errors in the system at this point ',registry=registry)

while True:
    random_number= random.random()*1000
    if(random_number%2==0):
        guage.inc()
    else:
        guage.dec()
    if(int(random_number)==540):
        break
    push_to_gateway('http://34.204.75.47:9091/',job="short job",registry=registry)    



