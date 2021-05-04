#!/usr/bin/env python
# -*- coding: utf-8 -*-

import chrono
import selectionCourt
import USBDetection
import Timestanp
import subprocess
import datetime

## Création du dossier de réception
folderDest = "/media/pi" + USBDetection() + "/Test"
print(folderDest)

proc = subprocess.call("mkdir", folderDest)
print(proc)


## Création du fichier d'enregistrement + début de l'enregistrement
outputFileName = folderDest + "/" + datetime.datetime.now() + ".txt"
proc = subprocess.call(["ffmpeg", "-i", listeCourt(), "-r", "25", outputFileName])

