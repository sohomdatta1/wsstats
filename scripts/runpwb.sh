#!/bin/bash
id
cat user-config.tmpl > user-config.py
ls -lah user-config.py
python3 $@