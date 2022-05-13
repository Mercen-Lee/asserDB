'''
asserDB v1.4 developed by Seok Ho Lee
(A.K.A. Mercen Lee)
Github : https://github.com/Mercen-Lee
Tistory : https://mercen.net/
'''
from os import path;from inspect import stack
from subprocess import run;import base64; from platform import system

systype=system()=='Windows'

def reader(filename):
    result={};temp=[];file=open(filename,'r');inside=file.read()
    if inside.startswith('asserDB;'):inside=inside[8:]
    else: Exception('Database is Damaged.')
    dc=base64.b64decode(inside).decode('utf-8')
    for line in dc.splitlines():
        for crop in line.split(':'):temp.append(crop[1:-1])
        for i in range(0,2):
            try:
                try:temp[i]=int(temp[i])
                except:temp[i]=float(temp[i])
            except:temp[i]=temp[i][1:-1]
        result[temp[0]]=temp[1];temp=[]
    file.close();return result

def writer(dictionary,filename):
    dckeys=list(dictionary.keys());dcvals=list(dictionary.values());dc=[]
    for i in range(0,len(dckeys)):
        if type(dckeys[i])!=str:dckeys[i]='['+str(dckeys[i])+']:'
        else:dckeys[i]='[\''+dckeys[i]+'\']:'
        if type(dcvals[i])!=str:dcvals[i]='['+str(dcvals[i])+']'
        else:dcvals[i]='[\''+dcvals[i]+'\']'
        dc.append(dckeys[i]+dcvals[i])
    ec=base64.b64encode('\n'.join(dc).encode('utf-8')).decode('utf-8')
    if systype:
        run(['attrib','-s','-h',filename],shell=True)
        file=open(filename,'w');file.write('asserDB;'+ec);file.close()
        run(['attrib','+h',filename],shell=True)
    else:file=open(filename,'w');file.write('asserDB;'+ec);file.close()

def check(name,stk):
    if not name:name=path.basename(stack()[stk].filename.replace('.py',''))
    link='.asserDB$'+path.splitext(name)[0]
    if not path.isfile(link):open(link,'w+').close()
    if systype:run(['attrib','+h',link],shell=True)
    return link

def readDict(name=None,stk=2):return reader(check(name,stk))

def readKeys(name=None):return list(readDict(name,3).keys())

def readVals(name=None):return list(readDict(name,3).values.keys())

def read(key,name=None):return readDict(name,3)[key]

def writeDict(dictionary,name=None,stk=2):writer(dictionary,check(name,stk))

def write(key,value,name=None):
    dc=readDict(name,3);dc[key]=value;writeDict(dc,name,3)
