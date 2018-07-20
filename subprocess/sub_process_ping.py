
import subprocess

#host = raw_input("Enter a host to ping: ")	

#p1 = subprocess.Popen(['ping', '-c 2', host], stdout=subprocess.PIPE)

p1 = subprocess.Popen(['shutdown -h'], stdout=subprocess.PIPE)

#output = p1.communicate()[0]

print p1
