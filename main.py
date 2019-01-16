from sys import argv 
import subprocess

script = argv
name = str(script[0])
print(name)
for i in range(0,10):
    directoryName = 'copy'+str(i)
    subprocess.call(['mkdir', directoryName])
    subprocess.call(['cp',name,directoryName])