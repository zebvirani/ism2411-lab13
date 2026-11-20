#1. a boolean gives a true or false value and based on that, dictates how the code is printed
#2.df["revenue"] is a series, which is one dimensional
#df[['revenue]] is a dataaframe, which is 2 dimensional
#matters when you need a dataframe.
#3. I would say pandas can quikly proccess lots of data and automate it better than excel.


#exercise 1
import pandas as pd

df = pd.read_csv('data/retail_sales.csv')

print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

#exercise 2
south = df[df['region'] == 'South']

print(len(south))
print(south.head())

#exercise 3
top5 = df.sort_values('revenue', ascending=False).head(5)
print(top5)

#exercise4
big_south = df[(df['region'] == 'South') & (df['revenue'] > 1000)]

print(len(big_south))
print(big_south.head())

#exercise5
df['per_unit'] = df['revenue'] / df['quantity']

print(df.head())
print(df['per_unit'].mean())

#exercise6
print(df['region'].unique())
print(df['region'].value_counts())

#exercise7
newfram = df [['region', 'product', 'revenue']]
print(newfram.shape)

#exercise8
df.to_csv('data/explored.csv', index=False)