import pika
import json
from main import db, Product

RABBIT_MQ_URL = 'amqps://gifcipsg:mRdHfRUPHoO8Z3EkSbwv34Tk0u0M1tpm@baboon.rmq.cloudamqp.com/gifcipsg/%2F'
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
        print('Creating product')
        product = Product(id=data['id'], title=data['title'], image=data['image'])
        db.session.add(product)
        db.session.commit()
        print('Product created')
    elif properties.content_type == 'producted_updated':
        product = Product.query.get(data['id'])
        product.title = data['title']
        product.image = data['image']
        db.session.commit()
        print('Product updated')
    elif properties.content_type == 'product_deleted':
        product = Product.query.get(data)
        if isinstance(product, Product):
            db.session.delete(product)
            db.session.commit()
            print('Product deleted')
        else:
            print('Product not found:', data)

channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)
print("started consuming")
channel.start_consuming()
channel.close()