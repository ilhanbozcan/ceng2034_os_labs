import os

#create JAIL directory
#copy or create necessary
#test it


home_directory =(os.path.expanduser('~'))
os.chdir(home_directory)
os.mkdir('JAIL')
os.chdir('JAIL')
os.mkdir('bin')
os.mkdir('etc')
os.system('sudo cp -r /lib /home/JAIL')
os.system('sudo cp -r /lib64 /home/JAIL')


os.system('sudo cp /bin/bash /home/JAIL/bin')
os.system('sudo chroot /home/JAIL')


#I wýll change the code to correct one
