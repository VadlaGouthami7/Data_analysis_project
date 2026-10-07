create database MSQL_Project;
use MSQL_Project;

CREATE TABLE finance_data (
	Trans_Index int,
    Transaction_ID VARCHAR(20) PRIMARY KEY,
    Trans_Date DATE,
    Department VARCHAR(50),
    Cost_Center VARCHAR(20),
    Budget_Revenue bigint,
    Actual_Revenue DECIMAL(15,1),
    Budget_Expense DECIMAL(15,1),
    Actual_Expense DECIMAL(15,1),
    Region VARCHAR(50),

    Revenue_Variance DECIMAL(15,1),
    Expense_Variance DECIMAL(15,2),
    Profit DECIMAL(15,2),
    Profit_Margin DECIMAL(10,4),
    M_onth VARCHAR(20)
);

select * from finance_data;


-- ------------------- SQL ANALYSIS----------------------
-- ------------------------------- Total Actual Revenue and Total Budget Revenue.-- -------------------------
select sum(Actual_Revenue)as total_actual_revenue,sum(Budget_Revenue) as total_budget_revenue from finance_data;

--  -------------------------------Total Actual Expense and Total Budget Expense.-- --------------------------
select sum(Actual_Expense)as Total_Actual_Expense,sum(Budget_Expense) as Total_Budget_Expense from finance_data;

-- ---------------------------------Overall Revenue Variance and Expense Variance.-----------------------------
select sum(Revenue_Variance)as TOT_REV_VAR,sum(Expense_Variance) as TOT_EXP_VAR from finance_data;

-- ---------------------------------Department-wise Revenue and Expense Variance ------------------------------ 
select Department,sum(Revenue_Variance) as Revenue_Variance,sum(Expense_Variance) as Expense_Variance from finance_data group by department;

-- ---------------------------------Monthly Revenue and Expense Trend. -- -------------------------------------
select M_onth,sum(Actual_Revenue) as Actual_Revenue,sum(Actual_Expense) as Actual_Expense from finance_data group by M_onth; 

-- --------------------------------- Profit Margin by Department.-- -------------------------------------------
select department,avg(Profit_Margin) as Profit_Margin from finance_data group by department;

-- ---------------------------------Departments with highest negative variance.-- ------------------------------

select department,sum(Revenue_Variance),sum(Expense_Variance) from finance_data group by department having sum(Revenue_Variance)<0 OR sum(Expense_Variance)<0 order by SUM(Revenue_Variance) ASC;