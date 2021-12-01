import pandas as pd
import xlsxwriter

df_tasks = pd.read_excel('data.xlsx', sheet_name='Задачи')
df_HRP1002 = pd.read_excel('data.xlsx', sheet_name='HRP1002')
df_HRT1002 = pd.read_excel('data.xlsx', sheet_name='HRT1002')
df_Pa0000 = pd.read_excel('data.xlsx', sheet_name='Pa0000')
df_TH1 = pd.read_excel('data.xlsx', sheet_name='ТН1')
df_TH2 = pd.read_excel('data.xlsx', sheet_name='ТН2')

df_list = [df_tasks, df_HRP1002, df_HRT1002, df_Pa0000, df_TH1, df_TH2]

print('Тип данных TH1: \n', type(df_TH1['TH']))  # Index(['TH'], dtype='object')
print('Столбец ТН: \n', df_TH1['TH'])
print('Тип данных TH2: \n', type(df_TH2['TH']))
print('Столбец TH: \n', df_TH2['TH'])

print('Количество элементов в ТН1: ', len(df_TH1['TH']))
print('Количество элементов в TH2: ', len(df_TH2['TH']))

unique_TH1 = df_TH1['TH'].unique()
unique_TH2 = df_TH2['TH'].unique()
print('Сравнение длин TH1: ', len(unique_TH1) == len(df_TH1['TH']))
print('Сравнение длин TH2: ', len(unique_TH2) == len(df_TH2['TH']))

set_TH1 = set(df_TH1['TH'])
set_TH2 = set(df_TH2['TH'])
intersection = pd.Series(list(set_TH1.intersection(set_TH2)), name='Intersection(TH1, TH2)')
difference_TH1 = pd.Series(list(set_TH1.difference(set_TH2)), name='TH1-TH2')
difference_TH2 = pd.Series(list(set_TH2.difference(set_TH1)), name='TH2-TH1')
print(intersection)
print(difference_TH1)
print(difference_TH2)

df_result = pd.concat([intersection, difference_TH1, difference_TH2], axis=1)

writer = pd.ExcelWriter("data.xlsx", mode="a", engine="openpyxl")
df_result.to_excel(writer, sheet_name="Task-6", index=False, startrow=1)
