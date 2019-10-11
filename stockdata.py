import pandas as pd
import pandas_datareader.data as dr
import datetime
from datetime import date
from pandas import DataFrame
import tkinter as tk
from tkinter import *
import os
from tkcalendar import Calendar, DateEntry

f ="global"
df ="global"


def scripname():
    scrip = variable.get()
    start =  cal_start.get()
    end = cal_end.get()
    i=0
    myfile = ("D:\csv_files\%s.csv" % scrip)
    if os.path.isfile(myfile):
        os.remove(myfile)
    f = dr.DataReader(scrip,"yahoo",start,end)
    df = pd.DataFrame(round(f,2), columns = ["Open","High","Low","Close"])
    df.to_csv(myfile, mode = "a", header = True, index = True)
    for index, row in df.iterrows():
        listbox1.insert(END,index, row, " ")

def savetocsv():
    print(f)
   # df = pd.DataFrame(round(f,2), columns = ["Open","High","Low","Close"])
    #df.to_csv(myfile, mode = "a", header = True, index = True)
    #print(df)
    #df.to_csv(myfile, mode = "a", header = False, index = True)

root = tk.Tk()
root.title("Data Fetcher")

Label(text="Scrip_Name").grid(row = 0,column = 0)
symbols = ["3IINFOTECH.NS",
"ACC.NS",
"ADVANIHOT.NS",
"AICHAMP.NS",
"ALLSEC.NS",
"ALPHAGEO.NS",
"ALPINEHOU.NS",
"AMARJOTHI.NS",
"AMLSTEEL.NS",
"ANKURDRUG.NS",
"ANTGRAPHI.NS",
"ARIHANT.NS",
"ARROWTEX.NS",
"ASHAPURMI.NS",
"ASHCONIUL.NS",
"ASHIMASYN.NS",
"ASIANELEC.NS",
"ASIL.NS",
"AUSOMENT.NS",
"AUSTRAL.NS",
"BAGFILMS.NS",
"BANARBEAD.NS",
"BANG.NS",
"ZEEL.NS"]
variable = StringVar(root)
variable.set(symbols[0]) # default value

w = OptionMenu(root, variable, *symbols)
w.grid(row=0,column=1)

Label(root, text='Startdate',width = 12).grid(row=1,column=0)
cal_start = DateEntry(root, width=12, background='darkblue',
                    foreground='white', borderwidth=2, year=2019)
cal_start.grid(row=1,column=1)

Label(root, text='Enddate',width = 12).grid(row=2,column=0)

cal_end = DateEntry(root, width=12, background='darkblue',
                    foreground='white', borderwidth=2, year=2019)
cal_end.grid(row=2,column=1)

Button(root, text="Fetch", width=12 ,command=scripname).grid(row = 2,column=2)
Button(root, text="Save to Excel",width=12,command = savetocsv).grid(row =1,column=2)
# create the listbox (note that size is in characters)
listbox1 = tk.Listbox(root, width=70, height=6)
listbox1.grid(row=5, column = 0,columnspan = 7)

# create a vertical scrollbar to the right of the listbox
yscroll = tk.Scrollbar(command=listbox1.yview, orient=tk.VERTICAL)
yscroll.grid(row=5, column=8, sticky=tk.N+tk.S)
listbox1.configure(yscrollcommand=yscroll.set)

# create a vertical scrollbar to the right of the listbox
xscroll = tk.Scrollbar(command=listbox1.xview, orient=tk.HORIZONTAL)
xscroll.grid(row=6, column=0,columnspan=8, sticky=tk.W+tk.E)
listbox1.configure(xscrollcommand=xscroll.set)


root.mainloop()
