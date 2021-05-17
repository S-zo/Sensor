import json
from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka import KafkaClient
from kafka import TopicPartition
import msgpack

zookeeper_servers = ["172.20.40.21:2181"]
bootstrap_servers = ["172.20.40.21:9092"]
client = KafkaClient(bootstrap_servers=bootstrap_servers)
producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

with open("/media/sf_.VirtualBox/mfl/20210507/mfl.json") as mfl:
    mfl = json.load(mfl)
for i in range(1, len(mfl)):
    producer.send("mfl", mfl["{}".format(i)])
