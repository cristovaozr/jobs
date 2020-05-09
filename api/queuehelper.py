# Copyright (c) 2020 Cristóvão Zuppardo Rufino
# Please read LICENSE file

import logging

class JobQueueHelper:
    
    __instance = None


    def __init__(self):
        self._mqueues = {}
        self._log = logging.getLogger("JobQueueHelper")


    def GetInstance():
        if JobQueueHelper.__instance is None:
            JobQueueHelper.__instance = JobQueueHelper()
        
        return JobQueueHelper.__instance


    def QueueAdd(self, mqueue):
        qname = mqueue.GetName()
        if qname in self._mqueues:
            self._log.warning("'JobQueue '{}' already exists! Double adding?".format(qname))
            return False

        self._log.debug("Adding JobQueue '{}'".format(qname))
        self._mqueues[qname] = mqueue
        return True
    

    def QueueGet(self, qname):
        if not qname in self._mqueues:
            self._log.warning("No JobQueue named '{}' found! You sure this is correct?".format(qname))
            return None

        self._log.debug("Getting JobQueue named '{}'".format(qname))
        return self._mqueues[qname]


    def QueueExists(self, qname):
        return qname in self._mqueues


    def QueueRemove(self, qname):
        if qname in self._mqueues:
            self._log.debug("Removing JobQueue '{}'".format(qname))
            del x[qname]
        
        else:
            self._log.warning("Trying to remove JobQueue '{}' but it doesn't exist. Ignoring but troublesome!".format(qname))
    