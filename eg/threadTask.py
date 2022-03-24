import logging
from worq import get_broker, TaskSpace
from threading import Thread
ts = TaskSpace(__name__)

class ThreadTask(Thread):

    def __init__(self,url):
        logging.basicConfig(level=logging.DEBUG)
        super(ThreadTask, self).__init__()
        self.url = url
        self.broker = get_broker(url)
        self.broker.expose(ts)
        pass

    # def initTask(self,url):
    #     print('Hi this is thread id',threadId)
        # logging.basicConfig(level=logging.DEBUG)
        # self.broker = get_broker(url)
        # self.broker.expose(ts)

    def getBroker(self):
        return self.broker

    @ts.task
    def add(value):
        return int(value)

    @ts.task
    def sum(values):
        return sum(values)


