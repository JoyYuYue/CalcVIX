import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

result = pd.read_csv('to_daily.csv')
true_vix = pd.read_csv('true_vix.csv',encoding='GBK')
# true_vix['date'] = pd.to_datetime(true_vix[u'日期'])
# true_vix.set_index(true_vix['date'],inplace=True)
# true_vix = true_vix.reindex(pd.date_range('2015-02-10','2019-10-22')).fillna(method='ffill')


plt.title("Calculated VIX")
plt.plot(result['datetime'], result['Calculated_VIX'], label='Calculated VIX')
plt.plot(true_vix.index,true_vix['price'],label='true vix')
plt.yticks(np.arange(0, 80, step=5))
plt.legend()
plt.show()
