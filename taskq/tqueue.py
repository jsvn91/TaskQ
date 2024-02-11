import uuid
import logging
import os, sys
from taskq.tqitem import Tqitem
from taskq.tqworker import Tqworker

MAX_WORKERS = os.cpu_count()

log = logging.getLogger()


class TQueue:

    def __init__(self, target, max_workers=MAX_WORKERS, max_parallel_worker=1) -> None:
        """_summary_

        Args:
            max_workers (_type_, optional): _description_. Defaults to MAX_WORKERS.
            max_parallel_worker (int, optional): _description_. Defaults to 1.
        """
        # self.max_workers = max_workers
        self.max_parallel_worker = max_parallel_worker
        log.info(f"max_parallel_worker set to {self.max_parallel_worker}")
        self.dequeue_no = max_parallel_worker
        self.prep_queue(target=target)
        self.workers = []
        self.tqueue = []

    def enqueue_item(self, *items):

        for item in items:
            tq_item = Tqitem(
                target_args=item,
                target_module=self.target_module,
                target_name=self.target_name,
            )
            log.info(f"tqitem : {tq_item.tqitem_guid}")
            self.tqueue.append(tq_item)
        self.item_count = len(self.tqueue)

    def dequeue_item(self):
        pop_items = []
        try:
            pop_items = self.tqueue[: self.dequeue_no]
            del self.tqueue[: self.dequeue_no]
        except Exception as e:
            pop_items = self.tqueue[: self.dequeue_no]
            del self.tqueue[: self.dequeue_no]
        return pop_items

    def process_queue(self):
        # for stage in range(max_parallel_worker)
        for stage in range(0, self.item_count, self.dequeue_no):
            tqitems = self.dequeue_item()
            workers = Tqworker(*tqitems)

            self.workers.extend(workers.sub_workers)
            poll_result = []
            while poll_result != [0]:
                poll_result = list(set([x.proc.poll() for x in workers.sub_workers]))
                continue
            for x in workers.sub_workers:
                log.info(f"{x.proc.pid} end")

    def set_module(self, target):
        self.target_module = target.__module__
        self.target_name = target.__name__

    def prep_queue(self, target=None):
        if target is None:
            log.error("Please set the target fucntion..")
            sys.exit()
        self.set_module(target=target)
        self.main_pid = os.getpid()
        log.info(f"self.main_pid is { self.main_pid}")
