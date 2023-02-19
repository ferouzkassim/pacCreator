import tkinter as tk
import xml.etree.ElementTree as Et
root = tk.Tk()
from cfgfilecreator import *
xmlfile = ('sample.tdf')
root.config(height=400,width=600)
root.maxsize(height=600,width=800)
frame1 = tk.Frame(root,height=300,width=500)
cpu_options= ('T606','T606_64','s7731E')
cpu_iterator = tk.StringVar()
cpu_iterator.set('cpu_model')
optionmenu = tk.OptionMenu(frame1,cpu_iterator,*cpu_options)
optionmenu.grid(column=0,row=0)
frame1.pack()
xmlpars = Et.parse(xmlfile)
xmlroot = xmlpars.getroot()
for sector in xmlroot:
    print(sector.tag)

#root.mainloop()