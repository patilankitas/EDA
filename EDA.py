import pandas as pd
import seaborn as se
import matplotlib.pyplot as plt

# Reading data from csv file and modifiying dtype of date(object) to datetime 
df=pd.read_csv(r'C:\users\Admin\Downloads\archive\amazon.csv',encoding='iso-8859-1',parse_dates=['date'])
print(df.dtypes)

#Diplay top 5 rows of dataset
print(df.head()) 
print(df.iloc[:5,])

#Display last 5 rows of dataset
print(df.tail())

#Find shape of datset
print(df.shape)
print(f'Number of Rows: {df.shape[0]}') 
print(f'Number of columns: {df.shape[1]}')

#Getting info about datset like total number of rows,total number of coluns,datatypes of each column and memory requirement
print(df.info())

#Check for duplicate data and drop them
result=df.drop_duplicates().any()
print(f'Are there is any duplicates in dataset: {result}')

df=df.drop_duplicates()
print(df.shape)

#Check null values in dataset
print(df.isna().sum())

#Get overall statistics about datframe .Bydefault it will only show stats for numeric values only
print(df.describe(include='all'))

#Rename month names to english language
df['month_english']=df['month'].map({'Janeiro' :'jan'
                                     ,'Fevereiro':'feb'
                                     ,'Marco':'march'
                                     ,'Abril':'april'
                                     ,'Maio':'may'
                                     ,'Junho':'jun'
                                     ,'Julho':'july'
                                     ,'Agosto':'august'
                                     ,'Setembro':'sep'
                                     ,'Outubro':'oct'
                                     ,'Novermbro':'nov'
                                     ,'Dezembro':'dec'})
print(df.head())

#In which month maximum number of forest fires were reported
result=df.groupby('month_english')['number'].sum().reset_index()
print(result)
#bar chart using seaborn lab
print(se.barplot(data=result,x='month_english',y='number'))

#In which year maximum number of forest fires were reported

result1=df.groupby('year').agg({'number':'sum'}).reset_index()
print(result1)
plt.figure(figsize=(16,5))
print(se.barplot(data=result1,x='year',y='number'))

#In which state maximum number of forest fires were reported
result3=df.groupby('state').agg({'number':'sum'}).reset_index()
print(result3)
plt.figure(figsize=(16,5))
plt.xticks(rotation=20)
print(se.barplot(data=result3,x='state',y='number'))

#Total number of fires were reported in amazonas
print(df[df['state']=='Amazonas']['number'].sum())

#Display number of fires were reported in amzonas year wise
result4=df[df['state']=='Amazonas'].groupby('year')['number'].sum().reset_index()
plt.figure(figsize=(16,5))
print(se.barplot(data=result4,x='year',y='number'))

#Display number of fires were reported in amzonas day wise
df['date']=pd.to_datetime(df['date'])
result5=df[df['state']=='Amazonas'].groupby(df['date'].dt.dayofweek)['number'].sum()
print(result5)
#convert numeric days 
import calendar 
result5.index=[calendar.day_name[x] for x in range(0,7)]   #changiing numeric index to words
print(result5.reset_index())

#Find total numbers of fires were reported in 2015 and visualize data based on each month
fire=df[df['year']==2015].groupby('month_english').agg({'number':'sum'}).reset_index()
print(fire)
plt.figure(figsize=(16,5))
print(se.barplot(data=fire,x='month_english',y='number'))

#Find average number of fires were reported from highest to lowest (state_wise)

fire1=df.groupby('state')['number'].mean().sort_values(ascending=False).reset_index()
print(fire1)
plt.figure(figsize=(16,5))
plt.xticks(rotation=20)
print(se.barplot(data=fire1,x='state',y='number'))


#Find state names where fires were reported in dec month
fire3=df[df['month']=='dec']['state'].unique()
print(fire3)