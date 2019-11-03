import pandas as pd
import glob

path = r'raw_data/test' # use your path
all_files = glob.glob(path + "/*.csv")[::-1]

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)


d1 = pd.read_csv('raw_data/OptionCode.csv')
# d2 = pd.read_csv('raw_data/50etf_option_1min/20150209.csv')
d1 = d1.drop(d1.columns[0], axis=1)
d1.columns = ['de_listed_date', 'maturity_date', 'option_type', 'strike_price', 'listed_date', 'sid']
result = pd.merge(frame, d1, how='left', on=['sid'])
result.to_csv('result_test.csv')
