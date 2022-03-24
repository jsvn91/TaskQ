import sys
import logging
from worq import get_queue

def main(url):
    logging.basicConfig(level=logging.DEBUG)
    q = get_queue(url)

    # enqueue tasks to be executed in parallel
    nums = [q.threadTask.add(value=x) for x in range(10)]

    # process the results when they are ready
    result = q.threadTask.sum(nums)
    #
    # wait for the final result
    result.wait(timeout=30)

    print('0 + 1 + ... + 9 = {}'.format(result.value))

if __name__ == '__main__':
    url = "memory://"
    main(url)