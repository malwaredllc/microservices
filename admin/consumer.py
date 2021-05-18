import pika

RABBIT_MQ_URL = 'amqps://gifcipsg:mRdHfRUPHoO8Z3EkSbwv34Tk0u0M1tpm@baboon.rmq.cloudamqp.com/gifcipsg/%2F'
params = pika.URLParameters(RABBIT_MQ_URL)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print("received in admin:", body)

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print("started consuming")

channel.start_consuming()

channel.close()