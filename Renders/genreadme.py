#!/usr/bin/env python3
import re
from pathlib import Path

txt_folder = Path('./').rglob('*.png')
files = [x for x in txt_folder]

count = 1
for f in files:
  new_f = re.sub(".png|[0-9]|\.", "", str(f))
  new_f = re.sub("-|_", " ", new_f)
  # new_f = re.sub("")
  print("File {}:\t old name: {} \t\t new name: {}".format(count, f, new_f))
  count += 1
