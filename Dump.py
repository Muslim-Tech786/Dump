import os, platform
try:
    import requests
except:
    os.system('pip install requests')
import requests
bit = platform.architecture()[0]
if bit == '32bit':
   os.system('python BB.cpython-311.so')
else bit == '64bit':
   from AA import dump
   dump()
