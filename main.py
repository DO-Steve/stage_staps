import subprocess
import now

#Détection de l'USB
p1 = subprocess.Popen(["ls", "/media/pi"], stdout=subprocess.PIPE)
p2 = subprocess.Popen(["grep", "-v", "SETTINGS*"], stdin=p1.stdout, stdout=subprocess.PIPE)
result = p2.stdout.read()
print(result)

#Création du dossier de réception
folderDest = "/media/pi" + result + "/Test"
print(folderDest)

proc = subprocess.call("mkdir", folderDest)
print(proc)

#Création du fichier d'enregistrement
outputFileName= folderDest + "/" + now.strftime("%d-%m-%y") + ".txt"

