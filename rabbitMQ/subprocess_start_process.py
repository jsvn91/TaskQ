from sys import executable
from subprocess import Popen, CREATE_NEW_CONSOLE , PIPE
import signal

def main(queuename_ls):
    workers_ls = []
    try:
        for queuename in queuename_ls:
            workers_ls.append(Popen([executable, 'worker.py',queuename] , creationflags=CREATE_NEW_CONSOLE))
            # p1 = Popen([executable, 'worker.py','my_producer_queue_1'], creationflags=CREATE_NEW_CONSOLE)
            # p3 = Popen([executable, 'worker.py','my_producer_queue_2'], creationflags=CREATE_NEW_CONSOLE)
    finally:
        pass

    for wc in workers_ls:
        wc.wait()

# input('Enter to exit from this launcher script...')
# workers_ls[0].send_signal(signal.SIGINT)


