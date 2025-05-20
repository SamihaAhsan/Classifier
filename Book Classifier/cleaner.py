import pandas as pd

reading= pd.read_csv('goodreads_data.csv')

reading.dropna(inplace = True) #dropping empty entries
reading.drop_duplicates(inplace = True) #dropping duplicate entries

reading=reading.drop("Avg_Rating",axis=1)
reading=reading.drop("URL",axis=1)
reading=reading.drop("Num_Ratings", axis=1)


reading.to_csv('cleaned_data.csv', index=False)




