import json

# Specify the path to your JSON file
json_file_path = "C:/Users/samee/output.json"

# Read the JSON file
with open(json_file_path, 'r') as file:
    json_data_list = json.load(file)

# Remove spaces from keys in each dictionary
json_data_no_spaces_list = [
    {key.replace(" ", ""): value for key, value in data.items()}
    for data in json_data_list
]

# Write the updated data back to the JSON file
with open(json_file_path, 'w') as file:
    json.dump(json_data_no_spaces_list, file, indent=2)
