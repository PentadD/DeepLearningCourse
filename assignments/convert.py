# /usr/bin/python

import IPython.nbformat.current as nbf
nb = nbf.read(open('hw01.py', 'r'), 'py')
nbf.write(nb, open('hw01_numpy_solved.ipynb', 'w'), 'ipynb')
