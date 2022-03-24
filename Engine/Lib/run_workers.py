from sys import executable
from subprocess import Popen, CREATE_NEW_CONSOLE , PIPE
import signal

def main(queuename_ls,consumer_file_name):
    workers_ls = []
    try:
        for queuename in queuename_ls:
            workers_ls.append(Popen([executable, f'{consumer_file_name}.py',queuename] , creationflags=CREATE_NEW_CONSOLE))
    finally:
        pass

    for wc in workers_ls:
        wc.wait()

# input('Enter to exit from this launcher script...')
# workers_ls[0].send_signal(signal.SIGINT)


