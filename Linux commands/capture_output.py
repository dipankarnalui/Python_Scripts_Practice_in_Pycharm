import subprocess

out=subprocess.run(["ipconfig"],capture_output=True)
print(out.stdout)

