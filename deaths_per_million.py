
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
df = pd.read_csv('owid-covid-data.csv')
#TO reference all the countries

#Label Encoding the Countries
from sklearn.preprocessing import LabelEncoder
country_encoder=LabelEncoder()
df['country_index']=country_encoder.fit_transform(df['location'])

#df_nafill=df.fillna(value=0, axis=0)
#df_nafill=df_nafill.groupby(['country_index','continent','location','population'])['total_deaths_per_million'].max().reset_index()
#print(len(df_nafill[(df_nafill['continent']=='Oceania')]))
#print(len(df_world[(df_world['continent']=='Oceania')]))
#df_reference=df.groupby(['country_index','location'])
#choose variables as columns
df_o=df[(df['continent']=='Oceania')]
df_world=df.groupby(['country_index','location','continent','gdp_per_capita','cvd_death_rate','aged_70_older'])['total_deaths_per_million'].max().reset_index()
#df2=df.groupby(['country_index','location'])['total_deaths'].max().reset_index()
#df_3=pd.merge(df2, df1)
#df3=df3.drop(['country_index_y'],axis=1)
#df_world=df_world.dropna()
#df1.set_index('country_index',inplace=True,drop=False, verify_integrity=True,append=True)
#df_5=df_4[(df_4['total_cases']!=0)]
df_world=df_world[(df_world['location']!='World')]
df_world=df_world[(df_world['location']!='Luxembourg')]
df_world=df_world[(df_world['location']!='World')]
df_world=df_world[(df_world['location']!='Japan')]
df_world=df_world[(df_world['location']!='World')]
df_world=df_world[(df_world['location']!='Qatar')]
#choosing the conitnen
##list of european countries by index not included Cyprus, greenland, Holy See,Turkey .Included Russia 

df_europe=df_world[(df_world['continent']=='Europe')]
df_asia=df_world[(df_world['continent']=='Asia')]
df_africa=df_world[(df_world['continent']=='Africa')]
df_na=df_world[(df_world['continent']=='North America')]
df_sa=df_world[(df_world['continent']=='South America')]
df_oceania=df_world[(df_world['continent']=='Oceania')]


#not including north korea, including cyprus, singapore, 


#making a death per case vairable
#df_europe['deaths per case'] = df_europe.apply(lambda row: row.total_deaths/row.total_cases , axis = 1) 
#df_world['deaths per case'] = df_world.apply(lambda row: row.total_deaths/row.total_cases , axis = 1)
#['deaths per case'] = df_asia.apply(lambda row: row.total_deaths/row.total_cases , axis = 1)

X_europe = df_europe.iloc[:, 5:6].values
y_europe = df_europe.iloc[:, -1].values
X_world = df_world.iloc[:, 5:6].values
y_world = df_world.iloc[:, -1].values
X_asia = df_asia.iloc[:, 5:6].values
y_asia = df_asia.iloc[:, -1].values
X_na = df_na.iloc[:, 5:6].values
y_na = df_na.iloc[:, -1].values
X_sa = df_sa.iloc[:, 5:6].values
y_sa = df_sa.iloc[:, -1].values
X_oceania = df_oceania.iloc[:, 5:6].values
y_oceania = df_oceania.iloc[:, -1].values
X_africa = df_africa.iloc[:, 5:6].values
y_africa = df_africa.iloc[:, -1].values

#radying the colourmap
c=np.array(df_world['gdp_per_capita'])
c_europe=np.array(df_europe['gdp_per_capita'])
c_asia=np.array(df_asia['gdp_per_capita'])
c_na=np.array(df_na['gdp_per_capita'])
c_sa=np.array(df_sa['gdp_per_capita'])
c_africa=np.array(df_africa['gdp_per_capita'])
c_oceania=np.array(df_oceania['gdp_per_capita'])
#s=np.array(df_world['cvd_death_rate'])+np.array(df_world['cvd_death_rate'])
s=0.05*np.array(df_world['cvd_death_rate'])
s_europe=0.25*np.array(df_europe['cvd_death_rate'])
s_asia=0.10*np.array(df_asia['cvd_death_rate'])
s_na=0.25*np.array(df_na['cvd_death_rate'])
s_sa=0.10*np.array(df_sa['cvd_death_rate'])
s_africa=0.25*np.array(df_africa['cvd_death_rate'])
s_oceania=0.10*np.array(df_oceania['cvd_death_rate'])
#c=np.array([1.5 if  i in europe_indeces else 2.5 if i in asia_indeces else 0.5 for i in range(len(df_world))])
# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_europe, y_europe, random_state = 0)
X_train, X_test, y_train, y_test = train_test_split(X_world, y_world, random_state = 0)
X_train, X_test, y_train, y_test = train_test_split(X_asia, y_asia, random_state = 0)

# Training the Simple Linear Regression model on the Training set
from sklearn.linear_model import LinearRegression
regressor_europe = LinearRegression()
regressor_europe.fit(X_europe, y_europe)
regressor_world = LinearRegression()
regressor_world.fit(X_world, y_world)
regressor_asia = LinearRegression()
regressor_asia.fit(X_asia, y_asia)

# Predicting the Test set results
#y_pred = regressor.predict(X_test)

 #Visualising the Training set results
#plt.scatter(X_europe, y_europe, c=c_europe,s=s_europe,cmap='plasma')

plt.title('Share of population older than 70 years, GDP(colour), Cardio Vascular disease death rate(size) vs deaths per million')
plt.xlabel('Share of population older than 70 years')
plt.ylabel('Deaths per million people')
#ax.legend(handles=s)


#plt.scatter(X_asia, y_asia, c=c_asia,s=s_asia,cmap='plasma')
#plt.scatter(X_europe, y_europe, c=c_europe,s=s_europe,cmap='plasma')
#plt.scatter(X_na, y_na, c=c_na,s=s_na,cmap='plasma')
#plt.scatter(X_sa, y_sa, c=c_sa,s=s_sa,cmap='plasma')
#plt.scatter(X_africa, y_africa, c=c_africa,s=s_africa,cmap='plasma')
#plt.scatter(X_oceania, y_oceania, c=c_oceania,s=s_oceania,cmap='plasma')
plt.scatter(X_world, y_world, c=c,s=s,cmap='plasma')
#plt.plot(X_asia, regressor_asia.predict(X_asia), color = 'blue')
plt.colorbar()
plt.show()
#print(df_asia.loc[df_asia['gdp_per_capita'].idxmax()])
#print(df_europe.sort_values(by=['gdp_per_capita']).head(10))
#print(df_europe.sort_values(by=['cvd_death_rate'],ascending=False).head(10))