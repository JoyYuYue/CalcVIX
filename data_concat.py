import pandas as pd
import glob

path = r'raw_data/50etf_option_1min'  # use your path
all_files = sorted(glob.glob(path + "/*.csv"))
code = pd.read_csv('raw_data/OptionCode.csv')
code = code.drop(code.columns[0], axis=1)
code.columns = ['de_listed_date', 'maturity_date', 'option_type', 'strike_price', 'listed_date', 'sid']

for filename in all_files:
    df = pd.read_csv(filename, header=0)
    result = pd.merge(df, code, how='left', on=['sid'])
    result.to_csv('new_data/'+ filename.split('/')[2])

# frame = pd.concat(li, axis=0)

# d2=pd.read_csv('raw_data/50etf_option_1min/20190320.csv')
# d1 = d1.drop(d1.columns[0], axis=1)
# code.columns = ['de_listed_date', 'maturity_date', 'option_type', 'strike_price', 'listed_date', 'sid']
# result = pd.merge(frame, code, how='left', on=['sid'])
# result.set_index('trading_date', inplace=True)
# result.to_csv('data_test2.csv')
