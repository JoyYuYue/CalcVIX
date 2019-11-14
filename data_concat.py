import pandas as pd
import glob

path = r'shibor'  # use your path
all_files = glob.glob(path + "/*.csv")[::-1]
print(all_files)

li = []
for filename in all_files:
    print(filename)
    df = pd.read_csv(filename, header=0)
    li.append(df)
frame = pd.concat(li, axis=0)
frame.columns= ['time','1D','1W','2W','1M','3M','6M','9M','1Y']
frame.set_index('time', inplace=True)
print(frame)
frame.to_csv('shibor.csv')

# d1 = pd.read_csv('raw_data/OptionCode.csv')
# d1 = d1.drop(d1.columns[0], axis=1)
# d1.columns = ['de_listed_date', 'maturity_date', 'option_type', 'strike_price', 'listed_date', 'sid']
# result = pd.merge(frame, d1, how='left', on=['sid'])
# result.set_index('trading_date', inplace=True)
# result.to_csv('data_test.csv')
