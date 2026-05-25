import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataframe = pd.read_csv(r"C:\Users\Sourav Sharma\OneDrive\Documents\Desktop\python\Zomato-data-.csv")
print(dataframe.head())

def handlerate(value):
    value= str(value).split('/')
    value=value[0];
    return float(value)

dataframe['rate']= dataframe['rate'].apply(handlerate)
print(dataframe.head())

dataframe.info()

print(dataframe.isnull().sum())

sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel('Types of Restaurant')
plt.show()


grouped_data= dataframe.groupby('listed_in(type)')['votes'].sum()
result=pd.DataFrame({'votes': grouped_data})
plt.plot(result,c='Green',marker='o')
plt.xlabel('Type of restaurantt')
plt.ylabel('Votes') 
plt.show()