import json

json_data_str='{"age":20,"name":"Dipankar"}'
python_dict_1=json.loads(json_data_str) #load's, s=string
age=python_dict_1["age"]
print(age)
