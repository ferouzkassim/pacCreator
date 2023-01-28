import tkinter as tk
root = tk.Tk()
from cfgfilecreator import *

root.config(height=400,width=600)
root.maxsize(height=600,width=800)
frame1 = tk.Frame(root,height=300,width=500)
cpu_options= []
cpu_iterator = tk.StringVar()
cpu_iterator.set('cpu_model')
optionmenu = tk.OptionMenu(frame1,cpu_iterator,*cpu_options)
optionmenu.grid(column=0,row=0)
frame1.pack()
root.mainloop()