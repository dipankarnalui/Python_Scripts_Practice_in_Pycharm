import subprocess


out=subprocess.run(["wsl","ifconfig"],capture_output=True,text=True)
print(out.stdout)

