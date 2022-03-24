from sys import executable
from subprocess import Popen, CREATE_NEW_CONSOLE
import signal
from run_workers import main
from worq.pool.thread import WorkerPool

def main(queue_name_ls,task_file_name):
    tasks_ls = []
    try:
        for queue_name in queue_name_ls:
            tasks_ls.append(Popen([executable, f'{task_file_name}.py',queue_name] , creationflags=CREATE_NEW_CONSOLE))
        main(queue_name_ls)

        for tc in tasks_ls:
            tc.wait()
    except:
        pass



# input('Enter to exit from this launcher script...')

