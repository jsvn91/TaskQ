#!/usr/bin/env python
import pika
import time

def main(queue_name):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue=queue_name, durable=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body.decode())
        time.sleep(body.count(b'.'))

        ch.basic_ack(delivery_tag=method.delivery_tag)
        if body.decode() == 'finished':
            exit(0)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=queue_name, on_message_callback=callback)

    channel.start_consuming()

if __name__ == '__main__':
    import sys
    main(sys.argv[-1])