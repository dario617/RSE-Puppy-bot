import os

temp = os.popen("sensors").read()
rest = os.popen("./foo.sh").read()