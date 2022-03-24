import sys
from worq.pool.thread import WorkerPool
from threadTask import ThreadTask

def main(url):
    tt = ThreadTask(url)
    pool = WorkerPool(broker=tt.getBroker(),workers=4)
    pool.start()
    return pool
