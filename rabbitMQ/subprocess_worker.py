from sys import executable
from subprocess import Popen, CREATE_NEW_CONSOLE
import signal

def main(queue_name_ls):
    tasks_ls = []
    try:
        for queue_name in queue_name_ls:
            tasks_ls.append(Popen([executable, 'new_task.py',queue_name] , creationflags=CREATE_NEW_CONSOLE))

        from subprocess_start_process import main
        main(queue_name_ls)

        for tc in tasks_ls:
            tc.wait()
    except:
        pass



# input('Enter to exit from this launcher script...')

