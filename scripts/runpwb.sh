#!/bin/bash
id
cat user-config.tmpl > user-config.py
python3 $@