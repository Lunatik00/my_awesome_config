import subprocess
def autostart():
    subprocess.Popen(["dex", "--autostart", 
                      "--search-paths", "$HOME/.config/autostart"])
    subprocess.Popen(["picom"])
    subprocess.Popen(["nitrogen", "--restore"])
    subprocess.Popen(["kdeconnect-indicator"])
    subprocess.Popen(["volctl"])
autostart()