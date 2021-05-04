from timeit import default_timer

def updateTime():
    ## Bouton_chronometre
    now = default_timer - default_timer
    minutes, seconds = divmod(now, 60)
    hours, minutes = divmod(minutes, 60)
    str_time = "%d:%02d:%02d" % (hours, minutes, seconds)
    updateTime()
    return str_time
