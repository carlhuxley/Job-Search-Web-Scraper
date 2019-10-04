# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 12:23:49 2019

@author: JMN
"""

import pyodbc

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=JNM-PC\SQLEXPRESS;DATABASE=CarSales')
cursor = cnxn.cursor()
cursor.execute('SELECT * FROM CarSales.dbo.work_Car_Sales')

for row in cursor:
    print(row)
