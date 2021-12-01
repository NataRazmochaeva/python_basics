import pandas as pd

df = pd.read_excel('data.xlsx', sheet_name='Лист1')
# ['PERNR' 'BEGDA' 'ENDDA' 'DOCUMENT' 'ZZSPECIAL' 'ZZQUAL']
# 'Приказ от 30.03.2021 № 536 "О проведении обучения в ЦПП филиала ПАО "ФСК ЕЭС" - МЭС Урала'

for col_name in df.columns.values:
    df[col_name] = df[col_name].str.replace(' "', ' «')
    df[col_name] = df[col_name].str.replace('" ', '» ')
    df[col_name] = df[col_name].str.replace('\n', '')
    df[col_name] = df[col_name].str.replace(' - ', '-')
    df[col_name] = df[col_name].str.replace(' -', '-')
    df[col_name] = df[col_name].str.replace('- ', '-')

"""
df['ZZQUAL'] = df['ZZQUAL'].str.replace(' "', ' «')
df['ZZQUAL'] = df['ZZQUAL'].str.replace('" ', '» ')
"""

writer = pd.ExcelWriter("data.xlsx", mode="a", engine="openpyxl")
df.to_excel(writer, sheet_name="Task-1-2", index=False)
writer.save()

