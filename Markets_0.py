# import fx currencies by using github package from the quant that I can't remember the M name

import numpy as np
import pandas as pd
import urllib3
import datetime
import matplotlib.pyplot as plt


website1 = "http://www.google.com/finance/getprices?q=AAPL&i=300&p=10d&f=d,o,h,l,c,v"
website = "https://www.google.com/finance/getprices?q=USDZAR&p=1000d&f=d,c"
website2= 'https://www.google.com/finance/getprices?q=USDZAR&i=111&p=10d&f=d,c'

data = pd.read_csv(website2,skiprows=8,header=None) #skirows up to the 8th since it's metadata not useful
print(data.head(10))

x=np.array(pd.read_csv(website2,skiprows=7,header=None))
date=[]
for i in range(0,len(x)):
    if x[i][0][0]=='a': #[0][0][0] pic first row, first element and first char in the first element( which is a string) x[0][0] 'a1524663000' , x[0][0][0] 'a'
       t= datetime.datetime.fromtimestamp(int(x[i][0].replace('a',''))) #use datetime.fromtimestamp function and as input take a1524663000 and delete the 'a'
       date.append(t)
    else:
        date.append(t+datetime.timedelta(minutes =int(x[i][0])))
data1=pd.DataFrame(x,index=date)
data1.columns=['a','Close']


#
# data1.tail()


# x=np.array(pd.read_csv(website1,skiprows=7,header=None))
# date=[]
# for i in range(0,len(x)):
#     if x[i][0][0]=='a': #[0][0][0] pic first row, first element and first char in the first element( which is a string) x[0][0] 'a1524663000' , x[0][0][0] 'a'
#        t= datetime.datetime.fromtimestamp(int(x[i][0].replace('a',''))) #use datetime.fromtimestamp function and as input take a1524663000 and delete the 'a'
#        date.append(t)
#     else:
#         date.append(t+datetime.timedelta(minutes =int(x[i][0])))
# data1=pd.DataFrame(x,index=date)
# data1.columns=['a','Open','High','Low','Close','Vol']
# data1.head()
# data1.tail

print(data1)


data1.plot()
plt.show()

#TODO add other currencies as columns to the dataframe by loopeing through different ccys, plot a matrix scatter plot and do multiple linear regression