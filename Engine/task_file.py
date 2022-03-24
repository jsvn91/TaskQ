import sys
import gc
from worq import get_queue
from worq import get_broker
import sys
from worq.pool.thread import WorkerPool
from Lib.queueProcess import QueueProcess
import ctypes

def main(queue_name):

    queue_id = queue_name

    url = "memory://"

    queue_obj = get_queue(url=url)

    ls = [queue_obj.Lib.queueProcess.add_object(queue_id,x) for x in range(0,10)]

    for i in ls:

        result = queue_obj.Lib.queueProcess.get_object(queue_id,0.1)
        result.wait(0.1)
        print('value is = ',result.value)

if __name__ == '__main__':

    main(sys.argv[-1])

    # main(queue_name=q.queue_id)


