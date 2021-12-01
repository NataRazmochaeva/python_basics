import pandas as pd
import math
df = pd.read_excel('data.xlsx', sheet_name='Лист1')
# ['PERNR' 'BEGDA' 'ENDDA' 'DOCUMENT' 'ZZSPECIAL' 'ZZQUAL']

# print(math.nan == df['PERNR'].values[116])

nan_columns = set()

for col_name in df.columns.values:
     for value in df[col_name].values:
         if pd.isnull(value):
             nan_columns.add(col_name)
             value = 'Пустая ячейка'
print(nan_columns)
