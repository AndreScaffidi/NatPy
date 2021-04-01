#!/bin/bash

rm -r dist build NatPy.egg-info

python setup.py sdist bdist_wheel

python -m twine upload dist/*