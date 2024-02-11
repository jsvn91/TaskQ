import uuid
import logging

log = logging.getLogger()

class TQueue():

    def __init__(self) -> None:
        self.__tqueue = {}
        
    def add_item(self, tqitem):
        self.tqitem_guid = str(uuid.uuid4())
        log.info(f"tqitem : {self.tqitem_guid}")
        self.__tqueue[self.tqitem_guid] = tqitem
