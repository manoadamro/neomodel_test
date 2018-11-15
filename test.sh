#!/usr/bin/env bash

pip3 install neomodel==3.2.9 >> /dev/null
pip freeze | grep neomodel

python3 part1.py

pip3 install --upgrade neomodel >> /dev/null
pip freeze | grep neomodel

python3 part2.py
