import json

config={
        "blr" : {"server" : "mail", "ip" : "10.1.8.2"},
        "mum" : {"server" : "app" , "ip" : "9.1.1.250"}
       }

# Convert python dict into JSON STRING
result = json.dumps(config)
print(result)
opposite= json.loads(result)
print(opposite)
