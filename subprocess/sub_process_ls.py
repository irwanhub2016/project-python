import subprocess

#p = subprocess.call(['ls', '-l'])

p = subprocess.call(['shutdown', '-h', 'now'])
print p
