import subprocess
command = subprocess.run("gconftool-2 --set /home/bruno/Pictures/1989-3840x2160-desktop-4k-outer-wilds-background-photo.jpg --type string '/home/bruno/Pictures/data/frame4464.jpg'")
print(command.stdout)

