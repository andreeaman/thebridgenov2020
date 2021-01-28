import sys, os 

dirname = __file__

for i in range(3):
    dirname = os.path.dirname(dirname)
    sys.path.append(dirname)
    print(dirname)

from week7.day2.flask.main_flask import dsd

print(dsd())

