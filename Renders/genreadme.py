#!/usr/bin/env python3
import re

from pathlib import Path


def debug_msg(msg):
  dmsg.append(msg)

def get_names(files): 
  count = 1
  for f in files:
    new_f = re.sub(".png|\.", "", str(f))
    new_f = re.sub("-|_", " ", new_f)
    msg = "File {}: File name: {} Title: {}".format(count, f, new_f)
    names.append(new_f)

    debug_msg(msg)
    count += 1
  return (names)

def main():
  # Set globals
  global txt_folder
  global files
  global dmsg
  global names
  global debug

  txt_folder = Path('./').rglob('*.png')
  files = [x for x in txt_folder]
  dmsg = []
  names = []
  debug = 0

  # Start main logic
 
  names = get_names(files)
  debug_msg("Names list: {}".format(names))

  if debug == 1:
    for m in dmsg:
      print("DEBUG: {}".format(m))


if __name__ == "__main__":
  main()
