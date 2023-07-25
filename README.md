# Python Cookiecutter Template

Creates a basic python project with a src layout.  Includes license, tests, pyproject.toml, git, and a README stub.

## Prerequisites

[Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/README.html) must be installed:

```bash
pip install --user cookiecutter
```

## Usage

Use with:

```bash
cookiecutter https://github.com/vishusandy/python_cookiecutter
```

You will be prompted for project information.

### Alias

Personally I find a bash alias makes this easier:

```bash
alias pyp="cookiecutter https://github.com/vishusandy/python_cookiecutter"
```

which would be called by running `pyp` in the terminal.

## .cookiecutterrc

I recommend the following for your [`~/.cookiecutterrc`](hhttps://cookiecutter.readthedocs.io/en/latest/advanced/user_config.html) file:

```
default_context:
    full_name: "<your name>"
    email: "<your email>"
    license: "Apache-2.0"
```

