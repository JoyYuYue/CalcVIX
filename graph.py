import matplotlib.pyplot as plt
import pandas as pd
result = pd.read_csv('Calculated_result2.csv')
plt.title("Calculated VIX")
plt.plot(result['time'], result['Calculated_VIX'], label='Calculated VIX')

plt.yticks([22,24,26,28,30,32])
plt.xticks(['2015-02-09 09:31:00','2015-02-09 11:30:00',\
            '2015-02-10 09:31:00', '2015-02-10 11:30:00',\
            '2015-02-11 09:31:00', '2015-02-11 11:30:00'\
            ])
plt.legend()
plt.show()