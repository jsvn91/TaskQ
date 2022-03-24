import pika
import time
import multiprocessing as mp


def single_run(queue_name):
    try:

        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue=queue_name, durable=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')

        def callback(ch, method, properties, body):
            print(" [x] Received %r" % body.decode())
            time.sleep(body.count(b'.'))
            print(" [x] Done")
            ch.basic_ack(delivery_tag=method.delivery_tag)

        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue=queue_name, on_message_callback=callback)

        channel.start_consuming()

    finally:
        pass

class QueueProcessor():

    def __init__(self,task_name,workers):
        self.workers = workers
        self.threadobj = []
        self.task_name = task_name
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.queue_name_ls = []
        ls = list(range(1,workers))
        task_name_ls = []
        for i in ls:
            queue_name = f'{task_name}_queue_{str(i)}'
            self.queue_name_ls.append(queue_name)
            self.channel.queue_declare(queue=queue_name, durable=True)

    def __del__(self):

        for i in self.queue_name_ls:
            self.channel.queue_delete(queue=i)
            try:
                # del self.threadobj[-1]

                # self.processLs[-1].kill()
                del self.processLs[-1]
            except:
                pass
            finally:

                pass

    def run_workers(self):
        from subprocess_worker import main
        main(queue_name_ls=self.queue_name_ls)
        print('Finished processing....')

if __name__ == '__main__':
    from datetime import datetime

    start_time = datetime.now()
    q = QueueProcessor('my_producer', 5)

    q.run_workers()

    q.__del__()
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
