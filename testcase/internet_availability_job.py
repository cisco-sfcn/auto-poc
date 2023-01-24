"""
To run:
    pyats run job internet_availability_job.py
"""
import argparse
import os
import sys

from pyats import aetest
from pyats.easypy import run

root_folder = "/auto/auto"

# parser = argparse.ArgumentParser()
# parser.add_argument('--testbed_file', help='path to testbed_file')

SCRIPT_LOCATION = root_folder + '/testcase/{}'


def run_script(runner=run):
    # args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])
    test_script = SCRIPT_LOCATION.format('internet_availability.py')
    # test_script = "helloworld.py"
    # Execute the test script
    runner(test_script, **vars())


def main():
    """
    main() function is the default easypy job file entry point.
    """
    run_script(run)


if __name__ == '__main__':
    run_script(aetest.main)