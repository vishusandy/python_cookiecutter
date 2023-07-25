import subprocess

git = {{ cookiecutter.git_init }}

if git:
    subprocess.run(['git', 'init', '-q', '-b', 'main'])
