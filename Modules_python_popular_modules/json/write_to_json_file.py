import json

import json

data = {
    "name": "Dipankar",
    "age": 35,
    "skills": ["Python", "Selenium", "API Testing"]
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)