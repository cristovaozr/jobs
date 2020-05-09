# Copyright (c) 2020 Cristóvão Zuppardo Rufino
# Please read LICENSE file

import logging
from queue import Queue, Empty

class JobQueue(Queue):

    def __init__(self, qname, maxsize=0):
        super().__init__(maxsize)
        self._qname = qname


    def GetName(self):
        return self._qname
    

    def QueuePut(self, item):
        self.put(item)


    def QueueGet(self, mqtimeout=None):
        item = None
        try:
            item = self.get(timeout=mqtimeout)
        
        except Empty as e:
            pass

        return item
