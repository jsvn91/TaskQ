import logging
from taskq.tqueue import TQueue
from taskq.sample import sample_target_func

log = logging.getLogger()


def test_tqueue():
    tq = TQueue(target=sample_target_func, max_parallel_worker=6)

    tq.enqueue_item("HI", "HI", "HI", "HI","HI", "HI", "HI", "HI", "HI", "HI", "HI", "HI" )

    tq.process_queue()

    for worker in tq.workers:
        log.info(f"result={worker.get_result()}")
