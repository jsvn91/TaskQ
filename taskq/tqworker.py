import subprocess
import sys, os
import logging
import uuid
from pathlib import Path
from taskq.tqitem import Tqitem

log = logging.getLogger(__name__)

class Tqworker():

    def __init__(self,*tqitems) -> None:
        self.tqitems = tqitems
        self.sub_workers = []
        self.cache_path = Path(os.getcwd(), ".tqcache").as_posix()
        os.makedirs(
            self.cache_path,exist_ok=True
        )
        self.call_process()
    
    def get_worker_id(self):
        return str(uuid.uuid4())
    
    def get_sub_worker(self,sub_worker_id, target_module, target_name):
        
        sub_worker_dict = dict(
                            sub_worker_id=sub_worker_id,
                            sub_worker_proc=self.get_process(
                                    sub_worker_id=sub_worker_id,
                                    target_module=target_module,
                                    target_name=target_name
                                )
                            ) 

    def get_process(self, sub_worker_id, target_module, target_name, target_args):
        artifact_path = Path(self.cache_path,sub_worker_id).as_posix()
        cmd = [sys.executable, "-c", f"import pickle;from {target_module} import {target_name};dbfile = open('{artifact_path}', 'wb');args='{target_args}';result={target_name}(args);pickle.dump(result, dbfile);dbfile.close()"]
        proc = subprocess.Popen(
                                cmd,
                                stdin=subprocess.PIPE, 
                                stderr=subprocess.PIPE,
                                stdout=subprocess.PIPE
                                )
        
        log.info(f"{proc.pid} started")
        return artifact_path, proc

    def get_module(self, target_module, target_name):
        try:
            func_args = f"{target_module}.{target_name}".split(".")
            function_module = __import__(func_args[0])
            cmd = f"function_module"
            for attr in func_args[1:]:
                cmd = cmd + f".{attr}"
                obj = eval(cmd)
        except Exception as e:
            self.log.error(e)
            sys.exit()
        return obj

    def call_process(self):
        for tqitem in self.tqitems:
            sub_worker_id = self.get_worker_id()
            tqitem.artifact_path, tqitem.proc = self.get_process(
                    sub_worker_id = sub_worker_id,
                    target_args = tqitem.target_args,
                    target_module = tqitem.target_module,
                    target_name = tqitem.target_name,
                )
            self.sub_workers.append(tqitem)




