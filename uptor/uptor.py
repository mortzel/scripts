#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess
import sys

def ctor(path, trackers, name, cat, host, base):
  tracker = ""
  for track in trackers:
    tracker = str(tracker + " -t " + track)
  ccom = str("transmission-create \"" + path + "\"" + tracker + " -o \"" + path + "/.torrent\"")
  rcom = str("transmission-remote " + host + " --add \"" + path + "/.torrent\" --download-dir \"" + base + "\"")
  ucom = str("curl -i -F filename=\"" + name + "\" -F category=" + cat + " -F info=... -F anonymous=true -F torrent=@\"" + path + "/.torrent\" http://192.168.49.204/upload.php")
  os.system(ccom)
  os.system(rcom)
  os.system(ucom)

# Setting
upload_folder = sys.argv[1]
cat = sys.argv[2]
host = "127.0.0.1:9091"
trackers = ["http://192.168.49.204/announce.php"]
recu = int(sys.argv[3])

data = str(subprocess.check_output(["ls", upload_folder]))[:-1]
folders = data.split('\n')

for folder in folders:
  if recu == 1:
    rdata = str(subprocess.check_output(["ls", upload_folder + "/" + folder]))[:-1]
    rfolders = rdata.split('\n')
    for rfolder in rfolders:
      path = str(upload_folder + "/" + folder + "/" + rfolder)
      if not os.path.isfile(path + "/.torrent"):
        ctor(path, trackers, rfolder, cat, host, upload_folder + "/" + folder)
  else:
    path = str(upload_folder + "/" + folder)
    if not os.path.isfile( path+ "/.torrent"):
      ctor(path, trackers, folder, cat, host, upload_folder)

