import subprocess
import os
import random
import os.path

folder = "web"
#os.chdir(".")

# if os.path.expanduser('~\\Documents\\coaba'):
#     print("Exists")
#     print("yes")
# else: 
#     print("no")
path = os.path.expanduser('~\\Documents\\notes')
subprocess.Popen(f'explorer {os.path.realpath(path)}')
# lala = os.path.expanduser('~\\Documents\\notes')
# if not os.path.exists(os.path.expanduser('~\\Documents\\notes')):
#     os.makedirs(lala)
# else:
#     print("You already have")

# completeName = "bimillah.txt"
# with open(os.path.join(os.path.expanduser('~'),'Documents',completeName), "w") as f:
#     f.write("semoga bisa")

# subprocess.Popen(["notepad.exe", os.path.expanduser('~\\Documents\\'+ completeName)])
