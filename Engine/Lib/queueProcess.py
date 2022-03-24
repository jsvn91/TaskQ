from worq import get_queue
from worq import get_broker,TaskSpace
from worq.queue.memory import TaskQueue
import ctypes

ts = TaskSpace(__name__)

class QueueProcess():

    def __init__(self,producer_name=None):

        self.queue_id = id(self)
        self.producer_name = f"{id(self.queue_id)}_producer"
        self.consumer_name = f"{id(self.queue_id)}_consumer"



        print('consumer queue name ', self.consumer_name)
        print('producer queue name ', self.producer_name)

        self.url = "memory://"
        self.broker = get_broker(url=self.url)
        self.broker.expose(ts)

        # self.producer_queue = get_queue(url=self.url, queue = self.producer_name)
        # self.consumer_queue = get_queue(url=self.url, queue = self.consumer_name)

        self.producer_queue = TaskQueue(url=self.url)
        self.consumer_queue = TaskQueue(url=self.url)
        self.producer_name_id = id(self.producer_queue)
        self.consumer_name_id = id(self.consumer_queue)

        pass

    def getbroker(self):
        return self.broker

    @ts.task
    def add_object(a,object):
        self =  ctypes.cast(a, ctypes.py_object).value
        return self.producer_queue.queue.put(object)

    @ts.task
    def get_object(a,timeout = 0.1):
        self = ctypes.cast(a, ctypes.py_object).value
        return self.producer_queue.queue.get(timeout)


# q = queueProcess()
# q.add('1234')
# q.add('1234')
# q.add('VALUE2','1234')
# q.add('VALUE3','1234')
# print('value = ',q.get())
# print('value = ',q.get())
#
# input('Enter ')