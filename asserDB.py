'''
asserDB v0.0 developed by Seok Ho Lee
(A.K.A. Mercen Lee)
Github : https://github.com/Mercen-Lee
Tistory : https://mercen.net/
'''
import json, os, inspect, subprocess

def check():
    asLink = os.path.basename(inspect.stack()[2].filename.replace('.py',''))
    asName = '.asserDB$'+os.path.splitext(asLink)[0]
    with open(asName, 'w+') as f: f.write('{}'); f.close
    try: subprocess.run(['attrib','+h',asName],check=True)
    except: pass

def add(variable):
    check()
