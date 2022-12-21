#!/usr/bin/python3
import subprocess
result=subprocess.run(["echo", "Hello, World!"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result.stdout
