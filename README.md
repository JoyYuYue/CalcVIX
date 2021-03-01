# IVIX Calculation
## Data
Raw Data is in the raw_data folder, containing three categories. 
* Market Data at 1 min frequency of SSE 50ETF
* Option Data
* Tick Data (not complete, collected by third party vendor)
(The Market Data only contains data before my extraction day. According to Ruitao, the API that we use to extract is no longer available. If you need more up-to-date data, you may have to explore new API)

Mapped Data contains the mapping output of market data and option data, which can be used directly in the current code.
Data is kept in seperate daily files for two reasons:
1. The entire dataset is too large to read in RAM and it is very slow to do so
2. Ideally, we can find a data crawler that could prepare files every day and save to the folder

## Code
Code entry is in Calculation.ipynb
I have written some comments on the code. Feel free to reach out if not clear

## Result
A full result is in Calculation_result.csv. However it is not using the latest code so the result is out-of-date.
