import os
import time
import subprocess

send_pipe_name = "communication_pipe" # Because

if os.path.exists(send_pipe_name):
    os.remove(send_pipe_name)
    os.mkfifo(send_pipe_name)
else:
    os.mkfifo(send_pipe_name)

subprocess.Popen([
    "python3.5",
    "test2_read.py"
])

send_pipe = os.open(send_pipe_name, os.O_WRONLY)

while True:
    os.write(send_pipe, b"TEST!!!\n")
    print("Sent")
    time.sleep(10)


