import pandas as pd
import glob

path = r'raw_data/test'  # use your path
all_files = sorted(glob.glob(path + "/*.csv"))

li = []
for filename in all_files:
    df = pd.read_csv(filename, header=0)
    li.append(df)
frame = pd.concat(li, axis=0)

d1 = pd.read_csv('raw_data/OptionCode.csv')
d1 = d1.drop(d1.columns[0], axis=1)
d1.columns = ['de_listed_date', 'maturity_date', 'option_type', 'strike_price', 'listed_date', 'sid']
result = pd.merge(frame, d1, how='left', on=['sid'])
result.set_index('trading_date', inplace=True)
result.to_csv('data_test.csv')
