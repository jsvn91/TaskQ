import logging
import time
log = logging.getLogger()


def sample_target_func(args):
    time.sleep(2)
    log.info(f"{args}")
    return 1


def add():
    pass
