import logging

log = logging.getLogger()


def sample_target_func(args):
    log.info(f"{args}")
    return 1


def add():
    pass
