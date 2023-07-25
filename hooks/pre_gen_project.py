import re
import sys

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

proj_name = '{{ cookiecutter.project_name }}'
proj_slug = '{{ cookiecutter.project_slug }}'

if proj_name == '':
    print(f'Invalid project name {proj_name}', file=sys.stderr)
    sys.exit(1)
    
if proj_slug == '' or not re.match(MODULE_REGEX, proj_name):
    print(f'ERROR: Invalid project slug {proj_slug} - must be a valid Python module name', file=sys.stderr)
    sys.exit(1)
