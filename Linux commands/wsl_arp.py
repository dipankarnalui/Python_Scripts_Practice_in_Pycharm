import subprocess

out=subprocess.run(["wsl","arp","-a"],capture_output=True, text=True)
print(out.stdout)

