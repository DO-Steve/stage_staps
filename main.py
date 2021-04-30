import subprocess
import datetime
from timeit import default_timer
import ps

## Détection de l'USB
def USBDetection() -> str:
    ## global_Bouton_pour_détecter_USB
    p1 = subprocess.Popen(["ls", "/media/pi"], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(["grep", "-v", "SETTINGS*"], stdin=p1.stdout, stdout=subprocess.PIPE)
    if p2 is None:
        ## global pop-up_cle_usb_manquante
    else :
        res = p2.stdout.read()
        res.encode("utf-8")
        print(res)
        return res


## Selection du cours
addressCourt1 = "169.254.74.221"
addressCourt2 = "169.254.74.224"
addressCourt3 = "169.254.74.223"
addressCourt4 = ""


def listeCourt() -> None:
    ## global Bouton_de_la_liste_des_cours
    ## OU
    ## global bouton_court1 etc
    listeCourt = []
    listeCourt.append(addressCourt1)
    listeCourt.append(addressCourt2)
    listeCourt.append(addressCourt3)


## Création du dossier de réception
folderDest = "/media/pi" + USBDetection() + "/Test"
print(folderDest)

proc = subprocess.call("mkdir", folderDest)
print(proc)


## Création du fichier d'enregistrement + début de l'enregistrement
outputFileName = folderDest + "/" + datetime.datetime.now() + ".txt"
proc = subprocess.call(["ffmpeg", "-i", listeCourt(), "-r", "25", outputFileName])


def updateTime():
    ## Bouton_chronometre
    now = default_timer - default_timer
    minutes, seconds = divmod(now, 60)
    hours, minutes = divmod(minutes, 60)
    str_time = "%d:%02d:%02d" % (hours, minutes, seconds)
    updateTime()
    return now


## Fin de l'enregistrement
def stopEnregistrement():
    ## global Bouton_Fin_enregistrement
    updateTime()
    grep = subprocess.Popen(["grep","ffmpeg"], stdin=ps.stdout, stdout=subprocess.PIPE)
    pid = grep.stdout.read()
    print(pid)
    pid = pid.replace("-ffmpeg","")
    pid = pid.replace("\n","")
    pid = pid.replace(" ","")
    print(pid)
    subprocess.call(["kill", pid])
