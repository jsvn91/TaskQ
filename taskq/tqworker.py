import subprocess

class Tqworker():

    def __init__(self,target_module, target_name) -> None:
        self.target = self.get_module(target_module, target_name)
        self.proc = subprocess.Popen(cmd)
        pass

    def get_module(self, target_module, target_name):
        try:
            func_args = f"{target_module}.{target_name}".split(".")
            function_module = __import__(func_args[0])
            cmd = f"function_module"
            for attr in func_args[1:]:
                cmd = cmd + f".{attr}"
                obj = eval(cmd)
        except Exception as e:
            log.error(e)
            sys.exit()
        return obj

    def call_process():


Tqworker(
    target_module="task.sample",
    target_name="sample_target_func"
)    

