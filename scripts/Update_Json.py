"""Helper script to update the OpenAPI spec with the description from the description.md file
This script updates the 'description' field in an OpenAPI YAML specification file
with the content from a Markdown file.
The script performs the following steps:
1. Reads the content of the Markdown file specified by INPUT_MD_FILE.
2. Appends the content of the Markdown file to a formatted string.
3. Reads the content of the YAML file specified by INPUT_YAML_FILE.
4. Updates the 'description' field in the 'info' section of the YAML data with the formatted string.
5. Writes the updated YAML data back to the original YAML file.
Constants:
    INPUT_MD_FILE (str): The path to the Markdown file containing the description.
    INPUT_YAML_FILE (str): The path to the original OpenAPI YAML specification file.
Dependencies:
    yaml: PyYAML library for parsing and writing YAML files.
"""

import yaml

INPUT_MD_FILE = "Description.md"
INPUT_YAML_FILE = "original.yaml"

with open(INPUT_MD_FILE, 'r', encoding='utf-8-sig') as md_file:
    md_file_data = md_file.read()
md_data_append = f"""|- {md_file_data}"""

with open(INPUT_YAML_FILE, 'r', encoding='utf-8-sig') as yaml_file:
    yaml_data = yaml.safe_load(yaml_file)

for data in yaml_data:
    if data == 'info':
        yaml_data[data].update({'description':md_data_append})
    with open(INPUT_YAML_FILE, 'w',encoding='utf-8-sig') as yaml_file:
        yaml.dump(yaml_data , yaml_file, sort_keys=False)
