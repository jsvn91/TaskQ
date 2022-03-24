from Lib.queueProcess import QueueProcess
from worq.pool.thread import WorkerPool

q = QueueProcess()
broker = q.getbroker()
pool = WorkerPool(broker=broker, workers=2)
pool.start()