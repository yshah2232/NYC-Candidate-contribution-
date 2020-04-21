# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
nyc= pd.read_csv('C:/Users/ip4186/Desktop/New folder/ny.csv',index_col=False,low_memory=False)

###df.fucntion ......df=data frame
nyc.shape #same as dim() in R--rows and columns

nyc.columns #Column description 

nyc.dtypes# giuves you the data types.

nyc.head(10) #First 5 rows---dataframe.fucntion(arguemnt)

nyc.tail #Last 5 rwos

nyc['cand_nm']

nyc['cand_nm'].value_counts()##distribution of counts by name

nyc['cand_nm'].value_counts(normalize=True)

##The goal of normalization is to change the values of numeric columns in the dataset to a common scale, without distorting differences in the ranges of values. 
#For machine learning, every dataset does not require normalization. It is required only when features have different ranges.#

pd.isnull(nyc.contbr_employer).value_counts()
## to check null values , false = no null values, True = Null values 
#Whether its possible to identify the 'Party' for each candidate (datawrangling)
print(nyc)


nyc['contb_receipt_amt'].value.counts() 


##BASIC PYTHON --INTRO TO SEIRES 
s=pd.Series([0.25,0.5,0.75,1])
print(s.values)
print(s.index)
s[0:2]
s[1:3]


s1=pd.Series([.25,.5,.75,1],index=['a','b','c','d'] )
s1.loc[1]#error
s1.iloc[1]#0.5
s1.loc['a']#0.25
s1.loc[a]#error
s1.loc[1]

s2=pd.Series([.5,.75,1,1.25],index=['a','b','c','d'] )
df=pd.DataFrame({'s1':s1,'s2':s2})
print(df)

s1=pd.Series([.25,.5,.75,1],index=['a','b','c','d'])
s3=pd.Series([.5,.75,1,1.25],index=['b','c','d','e'])
df=pd.DataFrame({'s1':s1,'s2':s2})
print(df)

s1=pd.Series([0.25,0.5,0.75,1],index=['a','b','c','d'])
s3=pd.Series([0.5,0.75,1,1.25],index=['a','b','d','e'])
df=pd.DataFrame({'s1':s1,'s3':s3})
print(df)


price=pd.Series({'cherry':1,'apple':2,'pear':4,'kiwi':5})
qty=pd.Series({'apple':1.99,'cherry':5,'kiwi':3,'pear':6})
fruits=pd.DataFrame({'price':price,'qty':qty})
print(fruits)

fruits[1:3]['price']
fruits.loc['kiwi','price']
fruits.iloc[apple]
fruits.loc['apple']
fruits.iloc[1:3,1]
fruits.loc['apple':'pear']
fruits.loc['apple':'pear','qty']


##############################################################################


#1) To identify the ’Party’ for each candidate
dfc = nyc.cand_nm.value_counts()
type(dfc)
print(dfc)
ucm=dfc.index.values
print(ucm)
dfc.index.values#creation of array for dataset with indexing range of 0 to ----
dfc.index
ucm[0]# to access records by index use []
#()-function and tuples
#[] list, serires, slicing 

#loc it can be used date label-let it be number or character 
#iloc -indexing only through number
dfc2.loc[5]
dfc2.iloc[5]

dfc2 = pd.DataFrame({'cand_nm':ucm})# creation of data frame to map unique value to the main data set
print(dfc2)

dfc2.loc[[0,1,14,21,18],'Party']='Democrat'
dfc2.loc[10,'Party']='Green'
dfc2.loc[11,'Party']='Libertarian'
dfc2.loc[19,'Party']='Independent'
dfc2.loc[dfc2['Party'].isnull(),'Party']='Republican'

print(dfc2)
cand_dict = dict(zip(dfc2.cand_nm, dfc2.Party)) # cobining indexs inot columns
nyc['Party']=nyc['cand_nm'].map(cand_dict)

print(nyc.head(10))
print(nyc[['cand_nm','Party']].head(10))

#2) Convert Date as needed 
#Convert the contb receipt dt to Date type
import datetime as dt
nyc['contb_receipt_dt']
nyc['Date']=pd.to_datetime(nyc['contb_receipt_dt'])
nyc['Date']=pd.to_datetime(nyc['contb_receipt_dt']).dt.strftime('%m/%d/%Y')#conversion of object to date to date time format  e.g 1-spe-16 to 2016-09-01
print(nyc[['contb_receipt_dt','Date']].head(10))
nyc.dtypes
df['sale_date'] = pd.to_datetime(df['sale_date'], format='%d/%m/%y %H:%M:%S')

#import datetime

#datetime.datetime.strptime("21/12/2008", "%d/%m/%Y").strftime("%Y-%m-%d")
#The call to strptime() parses the first argument according to the format specified in the second, so those two need to match. Then #you can call strftime() to format the result into the desired final format.

A=pd.Series(['red','blue','yellow','orange','red','blue','yellow','orange'])
B=pd.Series([1,1,1,1,2,2,2,2])
Price = pd.Series(np.arange(1,9))
dfexmp=pd.DataFrame({'A':A,'B':B,'Price':Price})

dfexmp.groupby('A')['Price'].sum() # groupby (columns Nmae) [values you want to display]. aggregation 

#3) Using group by, show the number of donations given to each party
nyc.groupby('Party')['contb_receipt_amt'].count() # group by 


#4) Using group by, show the number of donations given to each party, over time

nyc.groupby(['Party','Date'])['contb_receipt_amt'].count()

#5) Using group by, show the total dollar amount of donations given toeach party
nyc.groupby('Party')['contb_receipt_amt'].sum() # group by 

pd.options.display.float_format = '{:,.2f}'.format# t0 change the format of the value -
nyc.groupby('Party')['contb_receipt_amt'].sum()

#6) Using group by, show the total amount of donations given to each party, by date
nyc.groupby(['Party', 'Date'])['contb_receipt_amt'].sum()

#7) Which occupations donated the top 5 most money?
(nyc.groupby('contbr_occupation')['contb_receipt_amt'].sum()).sort_values(ascending=False).head(10)
df7 = nyc.groupby('contbr_occupation')['contb_receipt_amt'].sum().reset_index()#reset_index assigns new indexes to the data frame 
df7.sort_values('contb_receipt_amt', ascending=False, inplace=True)
df7.head(5)


df7.nlargest(5,'contb_receipt_amt')# quickest way to find top 1 to 100 values in a dataset by the dataframe 
nyc.nlargest(5,'contb_receipt_amt')

#8) Which occupations donated the least 5 amount of money?
df7.nsmallest(5,'contb_receipt_amt')
(nyc.groupby('contbr_occupation')['contb_receipt_amt'].sum()).sort_values(ascending=True).head(5)

#9) Which employer's employees gave the most money, give the top 5?
nyc.columns
(nyc.groupby(['contbr_employer','contbr_nm'])['contb_receipt_amt'].sum()).sort_values(ascending=False).head(5)


#To identigy number of unique Id's
nyc['cand_id'].unique()#displays numbe of unique key
nyc['cand_id'].nunique()#25

(nyc.groupby(['cand_nm','contbr_occupation'])['contb_receipt_amt'].sum()).sort_values(ascending=False).head(5)

# 10) For each candidate, what were the top 5 occupations that donated to their election
df10 = nyc.groupby(['cand_nm', 'contbr_occupation'])['contb_receipt_amt'].sum().reset_index()
df10.sort_values(['cand_nm', 'contb_receipt_amt'], ascending=[True, False],inplace=True)
df10.groupby('cand_nm').head()
df10.groupby('cand_nm').count()


#11) For the 5 candidates that raised the most money, graph their donations by time, in a line graph
df11 = nyc.groupby('cand_nm')['contb_receipt_amt'].sum().reset_index()
df11_p = df11.nlargest(5,'contb_receipt_amt')
df11_g = nyc[nyc.cand_nm.isin(df11_p.cand_nm)][['cand_nm','Date','contb_receipt_amt']]

dfpiv=pd.pivot_table(df11_g , values='contb_receipt_amt', index=['Date'],columns=['cand_nm'], aggfunc=np.sum)
dfpiv.loc['2016-01-01':'2016-01-30'].plot.line()

