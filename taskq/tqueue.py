import uuid
import logging
import os, sys

MAX_WORKERS = os.cpu_count()

log = logging.getLogger()

class TQueue():

    def __init__(self, max_workers=MAX_WORKERS, ) -> None:
        log.info(f"max_worker set to {max_workers}")
        self.__tqueue = {}
        
    def add_item(self, tqitem):
        self.tqitem_guid = str(uuid.uuid4())
        log.info(f"tqitem : {self.tqitem_guid}")

        self.__tqueue[self.tqitem_guid] = tqitem

    def initialise_worker(self):
        


    def set_module(self, target):
        self.target_module = target.__module__
        self.target_name = target.__name__
        
    def process(self, target=None):
        if target is None:
            log.error("Please set the target fucntion..")
            sys.exit()
        self.set_module(target=target)
        self.main_pid = os.getpid()
        log.info(f"self.main_pid is { self.main_pid}")

        for tq_item in self.__tqueue:
            log.info(tq_item)