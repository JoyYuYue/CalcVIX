import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# use the commented code to generate to_daily.csv and true_vix.csv
# result = pd.read_csv('Calculated_result.csv')
# result['datetime']=pd.to_datetime(result['time'])
# result.set_index(result['datetime'],inplace = True)
# dayvix = result.resample('D').mean()
# dayvix = dayvix.dropna()
# dayvix.to_csv('to_daily.csv')
#
# true_vix = pd.read_csv('ivixx.csv',usecols = [u'日期',u'收盘价(元)'],encoding='GBK')
# true_vix['date'] = pd.to_datetime(true_vix[u'日期'].copy())
# true_vix.set_index(true_vix['date'],inplace=True)
# true_vix = true_vix.reindex(pd.date_range('2015-02-10','2019-10-22')).fillna(method='ffill')
# true_vix = true_vix.drop(columns = [u'日期'])
# true_vix.columns = ['price','date']
# true_vix.to_csv('true_vix.csv')

result = pd.read_csv('to_daily.csv')
true_vix = pd.read_csv('true_vix.csv')

plt.title("Calculated VIX")
plt.plot(result['datetime'], result['Calculated_VIX'], label='Calculated VIX')
plt.plot(true_vix.index,true_vix['price'],label='true vix')
plt.yticks(np.arange(0, 80, step=5))
plt.legend()
fig = plt.gcf()
fig.set_size_inches(28.5, 10.5)
fig.savefig('test2png.png', dpi=100)
plt.show()