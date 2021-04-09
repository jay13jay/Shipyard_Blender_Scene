#!/usr/bin/env python3
import re

from pathlib import Path
from jinja2 import Environment, FileSystemLoader


def debug_msg(msg):
  dmsg.append(msg)

def render():
  names = get_names(files)
  file_loader = FileSystemLoader("./")
  env = Environment(loader=file_loader)
  env.trim_blocks = True
  env.lstrip_blocks = True
  env.rstrip_blocks = True
  template = env.get_template('readme.txt')

  output = template.render(title="Gallery", names=names, desc=desc)
  with open("readme.md", "w") as f:
    f.write(output)
  print(output)

def get_names(files): 
  count = 1
  for f in files:
    new_f = re.sub(".png|\.", "", str(f))
    new_f = re.sub("-|_", " ", new_f)
    msg = "File {}: File name: {} Title: {}".format(count, f, new_f)
    ary = []
    ary.append(f)
    ary.append(new_f)
    
    names.append(ary)

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
  global desc

  txt_folder = Path('./').rglob('*.png')
  files = [x for x in txt_folder]
  desc = "Renders of assets and the scene"
  dmsg = []
  names = []
  debug = 0

  # Start main logic
  
  debug_msg("Names list: {}".format(names))

  render()

  if debug == 1:
    for m in dmsg:
      print("DEBUG: {}".format(m))


if __name__ == "__main__":
  main()
