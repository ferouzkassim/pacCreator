import os
import tkinter as tk
root = tk.Tk()
workdir = os.getcwd()


files = os.listdir(workdir)

root.config(height=400,width=600)
root.maxsize(height=600,width=800)

def createCfg():
    cpu_name = input('enter cpu: loader  ')
    while os.path.exists(f'{workdir}/newflasher.cfg') :
     print('file exists')
     os.remove(workdir.find('/newflash,cfg'))
    else:
     try:
        with open("newflash.cfg",'a') as cfg:
            cfg.write(f" new pandora backup flasher\
                      '\n[Setting]\
                        \nPacVer=Bingo\
                        \nPAC_PRODUCT= {cpu_name}\
                        \nProductAlias={cpu_name}\
                        \nProductVer={cpu_name}\
                        \nMode=0\
                        \nFlashType=0\
                        \nNandStrategy=0\
                        \nNandPageType=0\
                        \nNvBackup=1\
                        \nOmaDmProductFlag=0\
                        \nOmaDM=1\
                        \nIsPreload=1\
                        \nPAC_CONFILE={cpu_name}.xml\
                        \n[FlashParam]\"")
     except:
        print('file exists')

    for file in files:
        binfiles=[]

        with open("newflash.cfg",'a') as cfg:
            if file.endswith('.bin'):
                binfiles.append(file)
                for singe_bin_file in binfiles:

                  cfg.write(f'\n{singe_bin_file} = 1@{file}')
            else:
                pass
            cfg.close()

#createCfg()

root.mainloop()