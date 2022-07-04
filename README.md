<div align="center">

<a href="https://github.com/miraclx/freyr-js">
  <img src="https://media.discordapp.net/attachments/955362477137362954/992759487041650718/2022-07-02_14-51.png" alt="pt2bs">
</a>

# `pt2bs`

<h4>
  Python to binary build system.
</h4>

![Maintenance](https://img.shields.io/maintenance/yes/2022)
![PyPi](https://img.shields.io/pypi/v/pt2bs)
[![CodeFactor](https://www.codefactor.io/repository/github/unxsh/pt2bs/badge)](https://www.codefactor.io/repository/github/unxsh/pt2bs)

[![GitHub stars](https://badgen.net/github/stars/unxsh/pt2bs)](https://GitHub.com/unxsh/pt2bs/stargazers/)
[![GitHub issues](https://badgen.net/github/issues/unxsh/pt2bs)](https://GitHub.com/unxsh/pt2bs/issues/)
![Commits](https://img.shields.io/github/commit-activity/m/unxsh/pt2bs)

[![](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/release/python-383/)
![License: MIT](https://img.shields.io/github/license/unxsh/pt2bs)

</div>

# Description

`pt2bs` is a small build system for python based on nuitka for building a program into a single binary file.
`pt2bs` generate a `build.py` file which contains the name of the main program file and the name of the output file as well as the args for the `python` interpreter and `nuitka` and from this generates a shell command to build the program into the `build/` dir.

(for template of build.py file see https://github.com/unxsh/pt2bs/blob/main/templates/build.py)

# Installation

```fish
pip install pt2bs
```

# Usage

```fish
python -m pt2bs 
```

### Example usage
```py
Modes:
 1) default (single binary without libs)
 2) default + pgo (may cause errors)
 3) standalone dir (binary + libs for distribute)
:2

 Main file of program.
:sfome.py

 Output file.
:sfome

 [build.py generated]
```
or
```fish
python -m pt2bs -g 2 sfome.py sfome
```

### flags
```fish
  -g, --generate | generate new build.py file with options by args
  -h, --help     | print this message
  -v, --version  | print program version
```

<br>
<br>

# File architecture
```python
pt2bs
  ├── LICENSE
  ├── pt2bs
  │   ├── argp.py
  │   ├── assets.py
  │   ├── build.py
  │   ├── funcs.py
  │   ├── __init__.py
  │   ├── __main__.py
  │   ├── perform.py
  │   └── pt2bs.py
  ├── README.md
  ├── setup.cfg
  ├── setup.py
  ├── templates
  │   ├── build.py
  │   └── idea.dat
  └── tests
      └── test.py

3 directories, 15 files
```

