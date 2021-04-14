#!/usr/bin/env python
"""build.py: Uses pip to uninstall and re-install the TrajectoryExecutor library."""

__author__ = "Jacob T. Cassady"
__email__ = "jacob.t.cassady@nasa.gov"

from os import system

if __name__ == "__main__":
    system('pip uninstall pylogger -y')
    system('pip install .')
