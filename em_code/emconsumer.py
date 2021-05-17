from kafka import KafkaConsumer
from json import loads
import pymysql

mydb = pymysql.connect(
    host="13.124.240.211",
    user="user",
    passwd="12345",
    database="SmartInside",
    port=51642,
)
sensor_list = []
consumer1 = KafkaConsumer(
    'em',
    bootstrap_servers=['smartinside1:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    #      group_id='my-group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))
for message in consumer1:
    a = message.offset
    b = message.value
    mycursor = mydb.cursor()
    sql = "INSERT INTO SmartInside.ke (id,sensor1,sensor2,sensor3,sensor4,sensor5) VALUES (%s,%s,%s,%s,%s,%s)"
    val = (a, b["sensor1"], b["sensor2"],
           b["sensor3"], b["sensor4"], b["sensor5"])
    mycursor.execute(sql, val)
    mydb.commit()
