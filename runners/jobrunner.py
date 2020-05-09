# Copyright (c) 2020 Cristóvão Zuppardo Rufino
# Please read LICENSE file

import logging
from api.job import Job

class JobRunner:

    __instance = None

    def __init__(self):
        self._log = logging.getLogger("JobRunner")
        self._joblist = []
    

    def __SearchJobByName(self, jname):
        idx = 0
        for (name, job) in self._joblist:
            if name == jname:
                break
            
            idx += 1
        
        return idx


    def GetInstance():
        if JobRunner.__instance is None:
            JobRunner.__instance = JobRunner()
        
        return JobRunner.__instance


    def AppendJob(self, job):
        name = job.JobGetJobName()
        self._log.debug("Appending job {}...".format(name))
        self._joblist.append((name, job))
        job.JobStart()
    

    # Kills all jobs NOW!
    def KillJobs(self):
        self._log.debug("Killing {} jobs!".format(len(self._joblist)))
        for (name, job) in self._joblist:

            self._log.debug("Killing job {}...".format(name))
            job.JobQuit()
            job.JobJoin(0.1)


    def KillJob(self, jname):
        idx = self.__SearchJobByName(jname)
        (name, job) = self._joblist.pop(idx)
        job.JobQuit()


    # Removes Job by jname
    def RemoveJob(self, jname):
        idx = self.__SearchJobByName(jname)
        del self._joblist[idx]


    # This function should *never* return!
    def Run(self):
        while True:
            if len(self._joblist) == 0:
                self._log.critical("NO JOBS RUNNING! Stopping runner")
                break 

            # TODO: consider restarting critical jobs?
            for (name, job) in self._joblist:
                job.JobJoin(.1)
                if job.is_alive() is False:
                    self._log.warning("Job {} died! Maybe premature?".format(name))
                    self.RemoveJob(name)