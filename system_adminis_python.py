import os
import subprocess
import time

os.system("ls -a")
time.sleep(0.5)
print("********")
subprocess.run(["ls", "-a"], capture_output=True, text=True)