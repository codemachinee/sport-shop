import pandas as pd
from pandas import *

cols = [0]
rows = [4]

worksheet = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
print(f'{worksheet[589:590].values.item()},000')