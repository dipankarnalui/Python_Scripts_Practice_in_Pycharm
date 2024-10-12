import subprocess

out=subprocess.run(["wsl", "ls", "-l"],capture_output=True,text=True)
print(out.stdout)

