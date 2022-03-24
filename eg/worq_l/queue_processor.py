import multiprocessing as mp
from worker import Worker
import warnings
warnings.filterwarnings("ignore")
import pandas as pd

df = pd.DataFrame({'a':[x for x in range(1000000)]
                 })
q = mp.Queue()

chunk_df_ls = df[chunk=]

for i in range(0,10):
    w = Worker()
    w.put(df)
    q.put(df)
    try:
        p = mp.Process(target = w.get , args=(q,))
        p.start()
    except:
        pass

    print(q.get())