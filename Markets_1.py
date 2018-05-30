# from pandas_datareader import data, wb
# import pandas_datareader.data as wb
# import pandas_datareader as pdr
#
# import datetime as dt
# start = dt.datetime(2015, 1, 1)
# end = dt.datetime(2017, 1, 1)
#
# # dt = wb.DataReader('FB', 'google', start, end)
# dt = panel = pdr.get_quote_google('AAPL', start, end)
# dt.head()

import quandl
# from bs4 import BeautifulSoup
import urllib3 # import requests # no need since urllib using requests
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# aapl = quandl.get("CUR/EUR", start_date="2006-10-01", end_date="2012-01-01")
direct_download = quandl.get("CUR/MXN", authtoken="b9JHksQZ5xsefG5QGfzP") #download direct from quandl
url_csv = 'https://www.quandl.com/api/v3/datasets/CUR/MXN.csv?api_key=b9JHksQZ5xsefG5QGfzP' # to download CSV
url = 'https://www.quandl.com/api/v3/datasets/WIKI/FB/data.json?api_key=b9JHksQZ5xsefG5QGfzP' # to get json code and convert into dataframe

# http = urllib3.PoolManager()
# data = http.request(method= 'GET', url = url)

# import json
# x = json.loads(data.data.decode('utf-8'))
# z= pd.read_json(data.data)
# print(z) #TODO upload data using JSON


currencies = ['MXN', 'JPY',  'GBP', 'EUR','CNY', 'INR','HKD', 'CHF', 'CAD'] # TODO FIX dates for USDAUD

ccy = []
for currency in currencies:
    path = os.path.join('/Users/federicogottardo/Documents/Python/data_market', 'CUR-' + currency + '.csv')
    if currency == 'MXN':
        df = pd.read_csv(filepath_or_buffer= path) ### 1st way to upload in dataframe
        df = df.rename(columns={'RATE':'MXN'}) ### rename column RATE as MXN
        ###another way to rename is to create a new column called MXN and then delete RATe --> df['MXN']=df['RATE], df.drop('RATE',1) where 1 is the axis dropping (columns)
    elif currency in ['GBP','EUR','AUD']: ### use 'in' not '==', '==' does not work since currency is not a list
        df[currency] = 1/pd.read_csv(filepath_or_buffer=path)['RATE']  # invert USGBP, USDEUR & USDAUD

    else:
        # df.append(pd.read_csv(filepath_or_buffer= path)) ### becareful, appends add dataframe to end of columns unless specify to create a new column
        df[currency]  = pd.read_csv(filepath_or_buffer= path)['RATE'] ### append column using same index
df= df.set_index('DATE') ### reindex to use column DATE as the new index. using df.reindex created a new empty dataframe except with the correct index


# for currency,i in zip(currencies,range(len(currencies))): # to loop across 2 different indices or more, use for x,y,z in zip(a,b,c) 















    # ccy.append(df) # list of Dataframes
# print(df)

### do df.index.values to get the values of the index


### df.shape (6208,11), df.size 68288 --? 6208*11




###### 2 ways to uplpod the CSV both require to go through os.path.join to get the filepath, but it can be uploaded as a dataframe using pd.read_csv directly, or you can use io to open the file, .read it, and upload it to dataframe
### 1st way is cleaner since data gets uploaded as float instead of str
###3rd way would be to upload dataframe from json
#
#          DATE       RATE   1st way
# 0  2016-12-31  20.735160
# 1  2016-12-30  20.643453
# 2  2016-12-29  20.66588
# 3  2016-12-28  20.722011
# 4  2016-12-27  20.740400
#                        0
# 0             DATE,RATE    2nd way
# 1   2016-12-31,20.73516
# 2  2016-12-30,20.643453
# 3   2016-12-29,20.66588
# 4  2016-12-28,20.722011


#2nd way to upload into dataframe
# f = open(path,'r')  # type is io.TextIOWrapper
# a = f.read() # type is str
# b = a.split() # type is list of str
# c = pd.DataFrame(b) # type(c) is Dataframe
# print(df.head(5), '\n', c.head(5))

###### PD.SCATTER_MATRIX is a plot in pandas

# print(ccy[0].describe())

# print(i.describe())

# for i in range(len(currencies)): ### when looping you can use range(len(list)) or enumerate(list), enumerate is slower
#     fig, ax = plt.subplots(nrows = 5, ncols=5, sharex=False)
#     # ccy[i].plot()
#     ax.plot(ccy[i])
#     # plt.legend([i],loc= 'upper right')
# plt.show()


# fig,ax = plt.subplots()
# plt.plot(df['DATE'],df['MXN'])
# df['MXN'].plot()


# for i in currencies:
# ax.plot(df.index,df['MXN'])
# plt.scatter(df.index,df['MXN'])

# fig, ax = plt.subplots(nrows=9,ncols=1)
# for i,j in zip(ax):
#     ax[i].plot(df['MXN'],df['MXN'])
#     plt.show()
df.plot(use_index= True, subplots = True, layout= (9,1), sharex= True)# kind = 'scatter')
plt.show()
# sns.pairplot(df,kind='scatter',diag_kind='hist',size = 2.0) ### diag_kind is type of plot for diagonal
# plt.show()

# print(ccy[5]['DATE'].iloc[-1]) ### use dataframe.iloc(-1) to find last item

print(df.index)
