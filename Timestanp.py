import subprocess
import ps
import chrono

class timestanpButton :
    def __init__(self):
        fichier = open("%d:%02d:%02d", "a")
    ## Def par bouton
    def timeStanpAction(self):
        ## global Bouton_timestanp
        action = timestanpButton
        action.write("Action importante : " + updateTime())
    def timeStanpPoint(self):
        point = timestanpButton
        point.write("Point marqué : " + updateTime())
    def timestanpFautes(self):
        faute = timestanpButton
        faute.write("Faute : " + updateTime())


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
