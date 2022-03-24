from worq import MemoryQueue
url = "memory://"

mq = MemoryQueue(url)

ls = [1,2,3,4,5]

for no in ls:
    mq.queue.put(no)

print(mq.queue.get())