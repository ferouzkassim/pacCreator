import os
workdir = os.getcwd()
cpu_name = input('enter cpu: loader  ')

files = os.listdir(workdir)


def createCfg():
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
        if file.endswith('.bin'):
         with open("newflash.cfg",'a') as cfg:
           cfg.write(f'\n 1@{file}')
           cfg.close()

createCfg()

