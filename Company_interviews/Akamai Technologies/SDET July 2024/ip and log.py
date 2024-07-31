'''
Suppose you have an access log for a web server in the following format:
timestamp IP_address file_path
12345678 10.1.2.3 /var/www/index.html
12345679 10.1.2.2 /var/www/search.html

#Task: Given this log file and an IP address,
#please write code to give a list of unique files that IP has accessed.
'''

d1={}
with open("weblog.txt","r") as f:
    all_lines=f.readlines()
    for line in all_lines:
        time,ip,filepath=line.split()
        if ip in d1.keys():
            if filepath not in d1[ip]:
                d1[ip] = d1[ip] + [filepath] #list merge
        else:
            d1[ip] = [filepath]
for k,v in d1.items():
    print(f"Client IP = {k} , Accessed Log files = {v}")