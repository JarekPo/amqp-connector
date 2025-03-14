import pika
import os

url = os.environ.get('CLOUDAMQP_URL')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='test_queue')

def callback(ch, method, properties, body):
  print('Received ' + str(body))

channel.basic_consume(
  'test_queue',
  callback,
  auto_ack=True)

print('Waiting for messages...')
channel.start_consuming()
connection.close()