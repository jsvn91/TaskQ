import logging 
from taskq.tqueue import TQueue

log=logging.getLogger()

def test_tqueue():
    tq = TQueue()

    tq.add_item("HI")
    tq.add_item("HI")
    tq.add_item("HI")
    tq.add_item("HI")
    tq.add_item("HI")