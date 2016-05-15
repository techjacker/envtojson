# envtojson
- write shell environment variables to a file in JSON format
- python 3+


## Installation
```Shell
pip install envtojson
```


## Usage
```Shell
$ envtojson -h
usage: envtojson [-h] [-q] filename vars [vars ...]

Write shell environment variables to a file in JSON.

positional arguments:
  filename     file to write to
  vars

optional arguments:
  -h, --help   show this help message and exit
  -q, --quiet
```


## Example
```Shell
$ envtojson envs.json COLORTERM XAUTHORITY
```
Contents of envs.json:
```JSON
{"XAUTHORITY": "/home/me/.Xauthority", "COLORTERM": "gnome-terminal"}
```
