# Titanic Dataset Analysis using Pandas - Day 3
import pandas as pd
titanic_data = pd.read_csv("Titanic-Dataset.csv")
print(titanic_data)
print(titanic_data.to_string())
print(titanic_data.info())
print(titanic_data.head(6))
print(titanic_data.tail(4))
print(titanic_data.describe())

# data cleaning
print(titanic_data["Age"])
print(titanic_data.isnull())
print(titanic_data.isnull().sum())

# data cleaning for null value
titanic_data["Age"] = titanic_data["Age"].fillna(titanic_data["Age"].median())
# or
titanic_data.fillna({"Age": titanic_data["Age"].median()}, inplace = True)
print(titanic_data)
print(titanic_data.isnull().sum())

# drop column
titanic_data.drop(columns = ["Cabin"], inplace = True)
print(titanic_data)

# mapping categories
titanic_data["Sex"] = titanic_data["Sex"].map({"male" : 0, "female": 1})
print(titanic_data["Sex"])

# changing column name
titanic_data = titanic_data.rename(columns = {"Sex": "Gender"})
print(titanic_data.info())

# Exploratory Data Analytics(EDA)
print("ths is rows of people with gender 1 and pclass 1", titanic_data[(titanic_data["Gender"] == 1) & (titanic_data["Pclass"] == 1)])  
print("this is mean of group of people Pclass who survived ", titanic_data.groupby("Pclass")["Survived"].mean())

# 60 bhanda badi age bako ko name age fare dekhaucha of 10 people
print(titanic_data.loc[titanic_data["Age"] >60 , ["Name", "Age", "Fare"]].head(10))

print(titanic_data.sort_values('Age', ascending=False)) 

print(titanic_data.loc[titanic_data['Age'] > 60, ['Name', 'Age', 'Fare']].head(10))
top_payers = titanic_data.sort_values('Fare', ascending=False) 

# Feature Engineering
titanic_data['Family_Size'] = titanic_data['SibSp'] + titanic_data['Parch']  +1
titanic_data['Title'] =  titanic_data['Name'].str.split(',').str[1].str.split('.').str[0].str.strip()
bins = [0, 12, 18, 60, 100]
labels = ['Child', 'Teenager', 'Adult', 'Senior'] 
titanic_data['Age_Group'] = pd.cut(titanic_data['Age'], bins=bins, labels=labels)