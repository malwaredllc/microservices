import pika
import json
from main import db, Product

RABBIT_MQ_URL = 'amqps://gifcipsg:mRdHfRUPHoO8Z3EkSbwv34Tk0u0M1tpm@baboon.rmq.cloudamqp.com/gifcipsg'
params = pika.URLParameters(RABBIT_MQ_URL)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print("received in main:", body)
    try:
        data = json.loads(body)
    except json.decoder.JSONDecodeError as e:
        print(str(e))
        return
    if properties.content_type == 'product_created':
        product = Product(id=data['id'], title=data['title'], image=data['image'])
        db.session.add(product)
        db.session.commit()
    elif properties.content_type == 'producted_updated':
        product = Product.query.get(data['id'])
        product.title = data['title']
        product.image = data['image']
        db.session.commit()
    elif properties.content_type == 'product_deleted':
        product = Product.query.get(data)
        db.session.delete(product)
        db.session.commit()

channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print("started consuming")

channel.start_consuming()

channel.close()