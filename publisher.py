import pika
import os

url = os.environ.get('CLOUDAMQP_URL')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.exchange_declare('test_exchange')
channel.queue_declare(queue='test_queue')
channel.queue_bind('test_queue', 'test_exchange', 'test_routing_key')

channel.basic_publish(
  body='Test Message',
  exchange='test_exchange',
  routing_key='test_routing_key'
  )
print('Message sent...')
channel.close()
connection.close()