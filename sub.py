from sys import argv
from os import path
from string import Template
from settings import config, template_path

filename = argv[1]

filein = open(path.join(template_path, filename))
src = Template(filein.read())
result = src.substitute(config)

fh = open(filename, 'w')
fh.write(result)
fh.flush()
fh.close()
