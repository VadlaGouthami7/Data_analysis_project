import pandas as pd
import numpy as np
from datetime import datetime
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

data=pd.read_csv("C:/Gouthami_FinancialKPI_Assignment/Python/Copy of finance_raw_unclean_large.csv")

# -------------INSPECTING DUPLICATES---------------
# print(data)
# print(data.duplicated().sum())
# #--------------REMOVING DUPLICATES------------------
data=data.drop_duplicates(subset=["Transaction_ID","Trans_Date","Department"])
print(data)

#-------------AGAIN INSPECTING DUPLICATES------------
print(data.duplicated().sum())




# -----------------Convert revenue and expense columns to numeric.-------
print(data.dtypes)
data["Budget_Revenue"]=pd.to_numeric(data["Budget_Revenue"])
data["Actual_Revenue"]=pd.to_numeric(data["Actual_Revenue"])
data["Budget_Expense"]=pd.to_numeric(data["Budget_Expense"])
data["Actual_Expense"]=pd.to_numeric(data["Actual_Expense"])

print(data.dtypes)



#------------------Convert Date column to datetime format-----------------
print(data.dtypes)
data["Trans_Date"]=pd.to_datetime(data["Trans_Date"])
print(data.dtypes)


#-----------------Handle missing values logically----------------------------
print(data.info())
print(data["Budget_Expense"].isna())
print(data["Region"].isna())

data["Budget_Expense"]=data["Budget_Expense"].fillna(data["Budget_Expense"].median())
data["Region"]=data["Region"].fillna(data["Region"].mode()[0])

print(data.info())


# ---------- Validate that no negative revenue or unrealistic financial values exist--------------
print(data[data["Actual_Revenue"]<0])
print(data[data["Actual_Expense"]>5000000])


data.loc[data["Actual_Revenue"] < 0, "Actual_Revenue"] = np.nan
print(data[data["Actual_Revenue"]<0])
data["Actual_Revenue"]=data["Actual_Revenue"].fillna(data["Actual_Revenue"].median())
print(data.info())

data.loc[data["Actual_Expense"]>5000000, "Actual_Expense"] = np.nan
print(data[data["Actual_Expense"]>5000000])
data["Actual_Expense"]=data["Actual_Expense"].fillna(data["Actual_Expense"].median())
print(data.info())
data["Revenue_Variance"]=data["Actual_Revenue"]-data["Budget_Revenue"]


data["Expense_Variance"]=data["Actual_Expense"]-data["Budget_Expense"]

# profit = Actual_Revenue - Actual_Expense
data["Profit"]=data["Actual_Revenue"]-data["Actual_Expense"]


# profit_margin = profit / Actual_Revenue
data["profit_margin"]=data["Profit"]/data["Actual_Revenue"]


data["m_onth"]=data["Trans_Date"].dt.month
print(data.dtypes)

print(data)

data.to_csv("./finance_clean.csv")

