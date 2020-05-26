# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
df = pd.read_csv('owid-covid-data.csv')
#Label Encoding the Countries
from sklearn.preprocessing import LabelEncoder
country_encoder=LabelEncoder()
df['country_index']=country_encoder.fit_transform(df['location'])

#TO reference all the countries
df_nafill=df.fillna(value=0, axis=0)
df_nafill=df_nafill.groupby(['country_index','location','population'])['total_cases'].max().reset_index()

 
#df_reference=df.groupby(['country_index','location'])
#choose variables as columns
df1=df.groupby(['country_index','location','gdp_per_capita'])['total_cases'].max().reset_index()
df2=df.groupby(['country_index',])['population'].max().reset_index()
#df3=df1.join(df2,lsuffix='suh' ,rsuffix='dude', on='country_index')
df3=pd.merge(df2, df1)
#df3=df3.drop(['country_index_y'],axis=1)
df3=df3.dropna()
#df1.set_index('country_index',inplace=True,drop=False, verify_integrity=True,append=True)

#choosing the conitnen
##list of european countries by index not included Cyprus, greenland, Holy See,Turkey .Included Russia 
country_indeces = [1,3,11,17,18,25,30,47,51,53,62,67,68,73,76,88,89,95,98,113,114,115,116,122,126,129,136,143,152,153,156,157,162,166,171,172,177,182,183,196,198]
df_europe=df3[df3.country_index.isin(country_indeces)]
#making a death per case vairable
df_europe['cases_per_capita'] = df_europe.apply(lambda row: row.total_cases/row.population , axis = 1) 
df3['cases_per_capita'] = df3.apply(lambda row: row.total_cases/row.population , axis = 1)

X_europe = df_europe.iloc[:, 3:4].values
y_europe = df_europe.iloc[:, -1].values
X_world = df3.iloc[:, 3:4].values
y_world = df3.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_europe, y_europe, random_state = 0)
X_train, X_test, y_train, y_test = train_test_split(X_world, y_world, random_state = 0)

# Training the Simple Linear Regression model on the Training set
from sklearn.linear_model import LinearRegression
regressor_europe = LinearRegression()
regressor_europe.fit(X_europe, y_europe)
regressor_world = LinearRegression()
regressor_world.fit(X_world, y_world)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

 #Visualising the Training set results
plt.scatter(X_europe, y_europe, color = 'red')
plt.plot(X_europe, regressor_europe.predict(X_europe), color = 'blue')
plt.title('case per capita vs gdp')
plt.xlabel('gdp_per_capita')
plt.ylabel('case per population')
#plt.scatter(X_world, y_world, color = 'green')
#plt.plot(X_world, regressor_world.predict(X_world), color = 'orange')
plt.show()


