import logging
from worq import get_broker, TaskSpace

ts = TaskSpace(__name__)

def init(url):
    logging.basicConfig(level=logging.DEBUG)
    broker = get_broker(url)
    broker.expose(ts)
    return broker

@ts.task
def num(value):
    return int(value)

@ts.task
def add(values):
    return sum(values)