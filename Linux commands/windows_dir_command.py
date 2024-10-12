import subprocess

out=subprocess.run(["dir"], shell=True)
print(out.stdout)
