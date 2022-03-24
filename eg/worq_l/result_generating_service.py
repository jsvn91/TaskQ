import time

start_time = time.time()

l = list(range(0,1000000))

# for i in l:
#     print(i)
#
# print("--- %s seconds ---" % (time.time() - start_time))

import pika as pk

pk.connection.