#!/usr/bin/env python3
import sys
import os
from subprocess import call
from argparse import ArgumentParser

parser = ArgumentParser(description="Changes directories, pulls the latest and creates a branch if specified")
parser.add_argument("-b", dest="branch_name", action="store", help="The name of a branch.  If none is specified no working branch is created")

args = parser.parse_args()
branch_name = args.branch_name

os.chdir("dev/SFConnector/code/managed-package")
commands = "git checkout master && git pull"

if branch_name is not None:
    commands = commands + " && git checkout -b {}".format(branch_name)

call(commands, shell=True)
