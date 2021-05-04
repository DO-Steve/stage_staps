import subprocess

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