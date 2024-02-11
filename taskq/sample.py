import logging
import time
log = logging.getLogger()


def sample_target_func(args):
    time.sleep(0.2)
    log.info(f"{args}")
    return args + " Hello"