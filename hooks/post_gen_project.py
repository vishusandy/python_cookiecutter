import os
import subprocess

git = {{ cookiecutter.git_init }}
license = '{{ cookiecutter.license }}'

if git:
    subprocess.run(['git', 'init', '-q', '-b', 'main'])

if license == '' or license.lower() == 'none':
    os.remove('LICENSE')
