import logging 
from taskq.tqueue import TQueue
from taskq.sample import sample_target_func

log=logging.getLogger()

def test_tqueue():
    tq = TQueue(max_workers=10)

    tq.add_item("HI")
    tq.add_item("HI")
    tq.add_item("HI")
    tq.add_item("HI")
    tq.add_item("HI")
    tq.process(target=sample_target_func)



