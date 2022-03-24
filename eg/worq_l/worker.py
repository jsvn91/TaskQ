import pandas as pd

class Worker():

    def __init__(self):
        pass

    def get(self,x):
        return x

    def put(self,df : pd.DataFrame):
        print(df.to_dict())