import json
from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka import KafkaClient
from kafka import TopicPartition

import msgpack
zookeeper_servers = ["172.20.40.21:2181"]
bootstrap_servers = ["172.20.40.21:9092"]
client = KafkaClient(bootstrap_servers=bootstrap_servers)
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))
path_dir = '/media/sf_.VirtualBox/em/'
file_list = os.listdir(path_dir)
for j in file_list:
    with open("/media/sf_.VirtualBox/em/{}/em.json".format(j)) as em:
        em = json.load(em)
    for i in range(0, len(em)):
        producer.send("em", em["{}".format(i)])
