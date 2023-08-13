import os
import subprocess

# https://github.com/ericmurphyxyz/dotfiles/blob/master/.local/bin/changevolume

def notify_volume():
    volume = subprocess.run(
       "amixer sget Master | grep 'Right:' | awk -F'[][]' '{ gsub(/%/, \"\"); print $2 }'",
        check=True,
        shell=True,
        stdout=subprocess.PIPE,
    ).stdout.decode("UTF-8").replace('\n', '')

    os.system(f"dunstify -a 'changevolume' -u low -r 9993 -h int:value:'{volume}' 'Volume: {volume}%' -t 2000")
