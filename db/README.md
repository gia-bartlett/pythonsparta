pyobdc  
pyodbc is a library that helps connect to a database (open database connectivity)  
interface with Microsoft database management  
```python
import pyodbc
```

cursor:  
control structure that allows us to control and manage rows of data from a response.  
In the pyodbc instance 




https://pandas.pydata.org/  
pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
built on top of the Python programming language.  
```python
import pandas as pd
# pd alias is standard practice
```
pd.Series() create a Series from scratch  

A data table in Pandas is called a DataFrame.  
When using a Python dictionary of lists, the dictionary keys will be used as column headers and the values in each list as rows of the DataFrame.  
DataFrame is a 2 dimensional data structure that can store data of different types:  
characters  
integers  
floating point values  
categorical data etc  
  
```python
df = pd.DataFrame({
    "Name": ["Braund, Mr. Owen Harris",
             "Allen, Mr. William Henry ",
             "Bonnell, Miss. Elizabeth"],
    "Age":  [22, 33], 58,
    "Sex": ["male", "male", "female"]}
)
df
''' output:
                       Name  Age     Sex
0   Braund, Mr. Owen Harris   22    male
1  Allen, Mr. William Henry   35    male
2  Bonnell, Miss. Elizabeth   58  female
'''
```
Each column in a DataFrame is called a Series  
To select the column, use the column label in between square brackets []  
(this is very similar to selection of dictionary value based on the key)
```python
df["Age"]
'''output:
0    22
1    35
2    58
Name: Age, dtype: int64
'''
```
Creating a Series from scratch  
No column labels as it is just a single column of a DataFrame but it does have row labels.   
```python
ages = pd.Series([22, 35, 58], name = "Age")
ages
'''output:
0    22
1    35
2    58
Name: Age, dtype: int64
'''
```
Using methods to 'do something' with the DataFrames or Series
How about the maximum and minimum age?  
This is done using the method .max() and .min()
```python
# applying this to the DataFrame
df["Age"].max()
df["Age"].min()
'''
output:
58
22
'''
# applying this to the Series
ages.max()
ages.min()
'''
output:
58
22
'''
```
Import data from different data sources using (read_*)  
Store data to different data sources using (to_*)  
Matplotlib is used to plot data within Pandas  


