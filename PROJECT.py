import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO

# Step 1: Data Acquisition
data = """
RowNumber,CustomerId,Surname,CreditScore,Geography,Gender,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary,Exited,Complain,Satisfaction Score,Card Type,Point Earned
1,15634602,Hargrave,619,France,Female,42,2,0,1,1,1,101348.88,1,1,2,DIAMOND,464
2,15647311,Hill,608,Spain,Female,41,1,83807.86,1,0,1,112542.58,0,1,3,DIAMOND,456
3,15619304,Onio,502,France,Female,42,8,159660.8,3,1,0,113931.57,1,1,3,DIAMOND,377
4,15701354,Boni,699,France,Female,39,1,0,2,0,0,93826.63,0,0,5,GOLD,350
5,15737888,Mitchell,850,Spain,Female,43,2,125510.82,1,1,1,79084.1,0,0,5,GOLD,425
6,15574012,Chu,645,Spain,Male,44,8,113755.78,2,1,0,149756.71,1,1,5,DIAMOND,484
7,15592531,Bartlett,822,France,Male,50,7,0,2,1,1,10062.8,0,0,2,SILVER,206
8,15656148,Obinna,376,Germany,Female,29,4,115046.74,4,1,0,119346.88,1,1,2,DIAMOND,282
9,15792365,He,501,France,Male,44,4,142051.07,2,0,1,74940.5,0,0,3,GOLD,251
10,15592389,H?,684,France,Male,27,2,134603.88,1,1,1,71725.73,0,0,3,GOLD,342
"""
# Step 2: Data Import
# Use StringIO to simulate a CSV file for demonstration purposes
df = pd.read_csv(StringIO(data))

# Display the first few rows of the dataset
print("Data Preview:")
print(df.head())

# Display basic information about the dataset

print("\nData Information:")
print(df.info())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Step 3: Exploratory Data Analysis (EDA)
# Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Visualizations
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], bins=10, kde=True)
plt.title('Age Distribution of Customers')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Exited', hue='Gender')
plt.title('Customer Exit Count by Gender')
plt.xlabel('Exited')
plt.ylabel('Count')
plt.legend(title='Gender')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='CreditScore', y='Exited')
plt.title('Credit Score vs Customer Exit')
plt.xlabel('Credit Score')
plt.ylabel('Exited')
plt.show()
