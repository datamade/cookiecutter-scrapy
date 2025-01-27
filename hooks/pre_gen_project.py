import re
import sys

PROJECT_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
project_name = "{{ cookiecutter.project_name }}"

if not re.match(PROJECT_REGEX, project_name):
    print(f'ERROR: {project_name} is not valid please only use letters and "_"!')
    sys.exit(1)
