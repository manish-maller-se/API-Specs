"""Helper script to update the OpenAPI spec with the description from the description.md file."""
import yaml

INPUT_MD_FILE = "Description.md"
INPUT_YAML_FILE = "original.yaml"
with open(INPUT_MD_FILE, 'r', encoding='utf-8-sig') as md_file:
    md_file_data = md_file.read()
md_data_append = f"""|- {md_file_data}"""
print(md_data_append)
with open(INPUT_YAML_FILE, 'r', encoding='utf-8-sig') as yaml_file:
    yaml_data = yaml.safe_load(yaml_file)

for data in yaml_data:
    if data == 'info':
        yaml_data[data].update({'description':md_data_append})
    with open(INPUT_YAML_FILE, 'w',encoding='utf-8-sig') as yaml_file:
        yaml.dump(yaml_data , yaml_file, sort_keys=False)
