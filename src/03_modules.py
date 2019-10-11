"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
print("Number of arguments: ", len(sys.argv)) # 1
print(sys.argv)   # ['03_modules.py']
print(str(sys.argv))   # ['03_modules.py']
print(sys.argv[0])   # 03_modules.py

# Print out the OS platform you're using:
print(sys.platform) # darwin

# Print out the version of Python you're using:
print(sys.version_info) # sys.version_info(major=3, minor=7, micro=4, releaselevel='final', serial=0)


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print(os.getpid()) # 58098

# Print the current working directory (cwd):
print(os.getcwd()) # /Users/katjohnnson/reviewLS/Intro-Python-I/src

# Print out your machine's login name
print(os.getlogin()) # katjohnnson