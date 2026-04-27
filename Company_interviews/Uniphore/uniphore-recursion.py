def flatten_json(data, parent_key=""):
    result = []

    if isinstance(data, dict):
        for key, value in data.items():
            new_key = f"{parent_key}.{key}" if parent_key else key
            result.extend(flatten_json(value, new_key))

    elif isinstance(data, list):
        for index, value in enumerate(data):
            new_key = f"{parent_key}[{index}]"
            result.extend(flatten_json(value, new_key))

    else:
        result.append(f"{parent_key}: {data}")

    return result


# Example usage
d1 = {
    "user": {
        "id": 101,
        "name": "Alice Johnson",
        "address": {
            "city": "Metropolis",
            "zipcode": "12345"
        }
    },
    "devices": [
        {"type": "laptop", "brand": "Dell"},
        {"type": "phone", "brand": "Apple"}
    ]
}

flattened = flatten_json(d1)
for item in flattened:
    print(item)