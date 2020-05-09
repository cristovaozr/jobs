# Copyright (c) 2020 Cristóvão Zuppardo Rufino
# Please read LICENSE file

import logging
from threading import Thread, Event

class Job(Thread):

    """
    All jobs *must* inherit from this class
    """

    def __init__(self, jname="Job", jargs=(), jkwargs={}):
        super().__init__(name=jname, args=jargs, kwargs=jkwargs)
        self._jname = jname
        self._jevent = Event()
        self._log = logging.getLogger(jname)
    
        self._log.debug("Starting Job: {}".format(jname))


    def JobStart(self):
        self.start()


    # This function *must* be overriden with the real running function
    # This function *should* return **always**!
    def JobExecute(self):
        self._log.warning("IMPLEMENT ME! - Running default JobExecute() function!")
        self.JobWaitForever()


    def JobQuit(self):
        self._jevent.set()

    
    def JobJoin(self, jtimeout=None):
        try:
            self.join(timeout=jtimeout)
        
        except RuntimeError as e:
            self._log.warning(e)
    

    def JobSleep(self, delay):
        self._jevent.wait(delay)


    def JobWaitForever(self):
        self._jevent.wait()


    def JobTerminate(self):
        self._log.warning("IMPLEMENT ME! - Running default JobTerminate() function!")


    def run(self):
        while self._jevent.is_set() is False:
            self.JobExecute()
        
        self.JobTerminate()


    def JobGetJobName(self):
        return self._jname
