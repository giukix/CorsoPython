# CSV

import pandas as pd
pd.options.display.max_columns = 6
df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
#print(df.describe())

small_df = df[['Age', 'Sex', 'Survived']]
print(small_df.head())


### creare una nuova colonna
df['male'] = df['Sex'] == 'male'
print(df.head())


# Salva il DataFrame in un file Excel
df.to_excel('C:/temp/mio_dataframe.xlsx', index=False)