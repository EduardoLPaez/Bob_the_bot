import pandas as pd
import numpy as np

import pandas_datareader as pdr

pdr.get_data_fred('GS10')


start_ = '2017-04-22'
end_ = '2018-04-22'

df = pdr.data.DataReader(name='AMZN',data_source= 'yahoo', start=start_, end = end_)
print(df)