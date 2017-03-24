# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 09:46:49 2017

@author: tih
"""

import pandas as pd

# ---------------------------- One date ----------------------------

OneDate = '2016-05-15'

pandas_date = pd.Timestamp(OneDate)
Year = pandas_date.year
Month = pandas_date.month
Day = pandas_date.day

print('Year:', Year, 'Month:', Month, 'Day:', Day)


# -------------------------- Range of dates -------------------------


Startdate = '2003-01-01'
Enddate = '2014-03-31'

Dates = pd.date_range(Startdate,Enddate,freq='3Min')

One_Date = Dates[3]
Year = One_Date.year
Month = One_Date.month
Day = One_Date.day

print('Year:', Year, 'Month:', Month, 'Day:', Day)



