import pandas as pd
df = pd.read_csv('2019.csv', header=1)
df1 = df[(df['Freedom to make life choices'] > 0.55) & (df['Perceptions of corruption'] < 0.3)]
df1 = df1.sort_values('Country or region', ascending=False)
a = len(df1)
list1 = []
for num in range(0, a):
    list1.append(a - num)
df1['Overall rank'] = list1
df1 = df1.transpose()
df1.to_csv('2021.csv', index=True, header=False)

df['Summa'] = df[['Score', 'Healthy life expectancy']].sum(axis=1)
df2 = df[['Country or region', 'Summa']]
df2 = df2.sort_values('Summa', ascending=False)
df2 = df2[0:18]
df2 = df2.sort_values('Country or region', ascending=True)
df2.to_csv('2020.csv', index=False, header=True)
