#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle                           ## System module
from pathlib import Path                ## pip install pathlib

# Save any obj in filepath
def save_obj(obj, filepath):
    with open(filepath, 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

# Load and return any obj from filepath
def load_obj(filepath):
    my_file = Path(filepath)
    if my_file.is_file():
        f = open(filepath, 'rb')
        return pickle.load(f)
    return False

print("Database Module Loaded Correctly.")
