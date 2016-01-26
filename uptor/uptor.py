#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess
import sys
import getopt

def ctor(path, torrent_path, trackers, name, cat, host, base):
  tracker = ""
  for track in trackers:
    tracker = str(tracker + " -t " + track)
  ccom = str("transmission-create \"" + path + "\"" + tracker + " -o \"" + torrent_path +"\"")
  rcom = str("transmission-remote " + host + " --add \"" + torrent_path + "\" --download-dir \"" + base + "\"")
  print(rcom)
  ucom = str("curl -i -F filename=\"" + name + "\" -F category=" + cat + " -F info=... -F anonymous=true -F torrent=@\"" + torrent_path + "\" http://192.168.49.204/upload.php")
  os.system(ccom)
  os.system(rcom)
  os.system(ucom)

def topath(pa, fol):
  bar = str("/")
  baz = int(pa.count(bar))
  foo = bar.join(pa.split(bar)[:baz])
  torpath = str(foo + "/." + fol + ".torrent")
  return torpath


# Setting
host = "192.168.49.203:9091"
trackers = ["http://freishare.fffd.eu/announce.php", "udp://10.185.1.11:6969"]

# Parameters
upload_folder = ''
cat = ''
recu = int(0)

# get cli params
myopts, args = getopt.getopt(sys.argv[1:],"u:c:r")
for o, a in myopts:
    if o == '-u':
        upload_folder = str(a)
    elif o == '-c':
        cat = str(a)
    elif o == '-r':
        recu = int(1)
    else:
        print("Usage: %s -u folder -c categorie [-r]" % sys.argv[0])

print(cat)

data = str(subprocess.check_output(["ls", upload_folder]))[:-1]
folders = data.split('\n')

for folder in folders:
  foopath = str(upload_folder + "/" + folder)
  
  if recu == 1:
    rdata = str(subprocess.check_output(["ls", foopath]))[:-1]
    rfolders = rdata.split('\n')
    for rfolder in rfolders:
      path = str(foopath + "/" + rfolder)
      if os.path.isdir(path):
        torrent_path = str(path + "/.torrent")
      else:
        torrent_path = topath(path, rfolder)
      base = upload_folder + "/" + folder
      name = folder + " - " + rfolder
      if not os.path.isfile( torrent_path ):
        ctor(path, torrent_path, trackers, name, cat, host, base)

  else:
    path = foopath
    if os.path.isdir(path):
      torrent_path = str(path + "/.torrent")
    else:
      torrent_path = topath(path, folder)
    base = upload_folder
    name = folder
    if not os.path.isfile( torrent_path ):
      ctor(path, torrent_path, trackers, name, cat, host, base)
