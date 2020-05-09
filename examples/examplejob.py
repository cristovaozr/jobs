# Copyright (c) 2020 Cristóvão Zuppardo Rufino
# Please read LICENSE file

import random
from api.job import Job

class ExampleJob(Job):

    def __init__(self):
        super().__init__(jname="ExampleJob")
    

    def JobExecute(self):
        print("Hello World!")
        self.JobSleep(random.randint(1,30))
