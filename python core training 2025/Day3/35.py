def connect(host="local",user="guest",pwd="guest",cmd="ls"):
   print("HOST = ",host)
   print("USER = ",user)
   print("PWD  = ",pwd)
   print("CMD  = ",cmd)

# let host,user,pwd be default - we will pass only the command
connect(cmd="uptime")

#connect(cmd="who",user="admin")        # valid/invalid - valid

#connect(user="admin",pwd="admin@123")  # valid/invalid - valid

#connect(user="root", "root123")        # valid/invalid - invalid

#connect("mailserver","admin",cmd="grep")# valid/invalid - valid

#connect("admin","admin@123","grep",host="mailserver") # - valid

