from sys import argv
from os import path
from string import Template
from settings import get_config, template_path

filename = argv[1]
author = argv[2]
name = argv[3]

filein = open(path.join(template_path, filename))
src = Template(filein.read())
result = src.substitute(get_config(author, name))

fh = open(filename, 'w')
fh.write(result)
fh.flush()
fh.close()
