import pika
import json

RABBIT_MQ_URL = 'amqps://gifcipsg:mRdHfRUPHoO8Z3EkSbwv34Tk0u0M1tpm@baboon.rmq.cloudamqp.com/gifcipsg'
params = pika.URLParameters(RABBIT_MQ_URL)
connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)