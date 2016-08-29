# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 18:53:08 2016

@author: felipelenz
"""

import csv
import sys

filename='Grad.csv'


f = open(filename)
csv_f = csv.reader(f)
    
FirstName=[]
MidName=[]
LastName=[]
Name=[]
Address=[]
Street=[]
City=[]
State=[]
Zip=[]
Label=[]
for column in csv_f:
    FirstName.append(column[3])
    MidName.append(column[4])
    LastName.append(column[5])
    Street.append(column[13])
    City.append(column[14])
    State.append(column[15])
    Zip.append(column[16])
    
text_file = open("Grad.txt", "w")
for i in range(1,len(FirstName)):
    temp=FirstName[i] + ' ' + MidName[i]+ ' ' + LastName[i]
    Name.append(temp)
    temp2=Street[i]
    temp3=City[i]+', '+State[i]+' '+Zip[i][0:5]
    Address.append(temp2+' '+temp3)
    
    temp4=(temp+'\n'+temp2+'\n'+temp3+'\n')
    Label.append(temp4)
    text_file.write("%s\n" %temp4)
#    print(temp4)


text_file.close()
