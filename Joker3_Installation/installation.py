import subprocess
import time
print(" "*50 + "XanderPoker Installation")
subprocess.call(['cp', '-r', 'Joker3', '/usr/lib/'])
subprocess.call(['chmod', '+x', '/usr/lib/Joker3/menu.py'])
with open("/etc/apt/apt.conf", 'w') as file1:
	pass
subprocess.call(['apt', 'install', 'python3-tk'])
time.sleep(5)
with open('/usr/share/applications/joker3.desktop', 'w') as file:
	file.write("[Desktop Entry]\n")
	file.write("Name = XanderPoker\n")
	file.write("Version = 0.99\n")
	file.write("Exec = /usr/lib/Joker3/menu.py\n")
	file.write("Icon = /usr/lib/Joker3/icon1.png\n")
	file.write("Type = Application\n")
	file.write("Categories = Application\n")
