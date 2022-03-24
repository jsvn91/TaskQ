#!/usr/bin/env python
import main
import threadPool as pool

url = "memory://"

p = pool.main(url)
try:
    main.main(url)
finally:
    p.stop()


# if __name__ == "__main__":
#     url = "memory://"
#     p = pool.main(url)
#     try:
#         main.main(url)
#     finally:
#         p.stop()