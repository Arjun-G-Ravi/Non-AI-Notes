# Shebang

A shebang, also known as a hashbang or pound bang, is a character sequence at the beginning of a script or a text file that indicates the path to the interpreter for the script. It typically starts with the hash symbol (#) followed by an exclamation mark (!). The shebang is used in Unix-like operating systems to **specify the interpreter** that should be used to execute the script.

This can be done for .sh, .py, etc. files. 

It has to be written on the first line on a script, to specify the interpreter.
Eg: #!/bin/bash: To set the interpreter to bash
    #!/usr/bin/python3: To set the interpreter to python3, installed in the given location


# How to run
To run the script with the default (or shebangged) interpreter, we do ```./filename```