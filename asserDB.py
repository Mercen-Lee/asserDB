'''
asserDB v0.2 developed by Seok Ho Lee
(A.K.A. Mercen Lee)
Github : https://github.com/Mercen-Lee
Tistory : https://mercen.net/
'''
from os import path;from inspect import stack
from subprocess import run;import base64

def typer(variable):
    try:
        try: int(variable); return 'int'
        except: float(variable); return 'float'
    except: return 'str'

def read(filename):
    result={};temp=[];file=open(filename,'r');inside=file.read()
    if inside.startswith('asserDB;'):inside=inside[8:]
    else: Exception('Database is Damaged.')
    dc=base64.b64decode(inside).decode('utf-8')
    for line in dc.splitlines():
        for crop in line.split(':'):temp.append(crop[1:-1])
        for i in range(0,2):
            if typer(temp[i])=='int':temp[i]=int(temp[i])
            elif typer(temp[i])=='float':temp[i]=float(temp[i])
            else:temp[i]=temp[i][1:-1]
        result[temp[0]]=temp[1];temp=[]
    file.close();return result

def write(dictionary, filename):
    dckeys=list(dictionary.keys());dcvals=list(dictionary.values());dc=[]
    for i in range(0,len(dckeys)):
        if typer(dckeys[i])!='str':dckeys[i]='['+str(dckeys[i])+']:'
        else:dckeys[i]='[\''+dckeys[i]+'\']:'
        if typer(dcvals[i])!='str':dcvals[i]='['+str(dcvals[i])+']'
        else:dcvals[i]='[\''+dcvals[i]+'\']'
        dc.append(dckeys[i]+dcvals[i])
    ec=base64.b64encode('\n'.join(dc).encode('utf-8')).decode('utf-8')
    file=open(filename,'w');file.write('asserDB;'+ec);file.close() 

def check():
    asLink=path.basename(stack()[2].filename.replace('.py',''))
    asName='.asserDB$'+path.splitext(asLink)[0]
    if not path.isfile(asName):open(asName,'w+').close()
    try:run(['attrib','+h',asName],check=True)
    except: pass
    return asName

def readDict():return read(check())

def writeDict(dictionary):write(dictionary,check())
