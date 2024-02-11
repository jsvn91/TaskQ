import uuid
import pickle
import logging
import sys

log = logging.getLogger(__name__)

class Tqitem():

    def __init__(self,target_args, target_module, target_name) -> None:
        self.tqitem_guid = str(uuid.uuid4())
        self.artifact_path = None
        self.target_args = target_args
        self.target_name = target_name
        self.target_module = target_module
        self.proc = None

    def get_result(self):
        try:
            dbfile = open(self.artifact_path, 'rb')    
            db = pickle.load(dbfile)
            dbfile.close()
            return db
        except Exception as e:
            log.error(e)
            return None
            


        