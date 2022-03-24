#!/usr/bin/env python
import pika
import sys

def main(queue_name,chunksize=100):
    # queue_name = "my_producer_queue_0"
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name, durable=True)
    input_ls = list(range(0,chunksize))

    for no in input_ls:
        message = {'input':no}

        channel.basic_publish(
            exchange='',
            routing_key=queue_name,
            body=str(message),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ))
        print(" [x] Sent %r" % message)

    channel.basic_publish(
        exchange='',
        routing_key=queue_name,
        body=str('finished'),
        properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
        ))
    connection.close()

if __name__ == '__main__':
    import sys
    main(sys.argv[-1])