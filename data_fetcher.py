import os
import pandas as pd
import pandas_datareader.data as dr
import datetime
from datetime import datetime
from datetime import date
from pandas import DataFrame

start = datetime(2019, 1, 1)
end =  datetime(2019, 5, 24)
myfile = "D:\csv_files\data.txt"
if os.path.isfile(myfile):
    os.remove(myfile)

f = dr.DataReader("ACC","yahoo",start,end)
print(f)
#df = pd.DataFrame(round(f,2), columns = ["Open","High","Low","Close"])
#df.to_csv(myfile, mode = "a", header = False, index = True)
