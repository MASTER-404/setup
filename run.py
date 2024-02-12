import os, sys
os.system("git pull")
try:
    __import__("setup")
except Exception as e:
    exit(str(e))
