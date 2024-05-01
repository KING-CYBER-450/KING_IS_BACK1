import os, sys
try:
    __import__("qsbuy").jvl()
except Exception as e:
    exit(str(e))
