#!/usr/bin/env python3

# Copyright (c) 2020 Cristóvão Zuppardo Rufino
# Please read LICENSE file

import sys, logging, time
from api.job import Job
from api.queuehelper import JobQueueHelper
from runners.jobrunner import JobRunner
from examples.examplejob import ExampleJob

# Tries to import coloredlogs so logging gets nicer
try:
    import coloredlogs
    coloredlogs.install(level='DEBUG')

except Exception as e:
    print("*** For colored logging please install \"coloredlogs\" package!")


def main(argv):
    log = logging.getLogger("main")

    try:
        runner = JobRunner.GetInstance()

        # Appends extra jobs if any
        runner.AppendJob(ExampleJob())

        # Starts runner - last step for main() function
        runner.Run()
    
    except KeyboardInterrupt as e:
        log.info("Ctrl+C detected!")
        runner.KillJobs()
    
    except Exception as e:
        log.error(e)
        # TODO: die if error occurs?

    return 0

if __name__ == "__main__":
    # Enabling full logging
    logging.basicConfig(level=logging.DEBUG)

    sys.exit(main(sys.argv))
