# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 10:55:39 2021

@author: MO_TAREK
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#reading the file
dataset=pd.read_csv("Wuzzuf_Jobs.csv")
dataset.describe()


# dropping ALL duplicate values
dataset.drop_duplicates(subset =("Title","Company"),
					keep = "first", inplace = True)



#Counting the jobs for each company
company = dataset.Company.value_counts().to_frame()
#pie chart
company[company.Company>10].plot(kind='pie',figsize=(15,10),subplots=True)
#bar chart
company[company.Company>10].plot(kind='bar',figsize=(15,10))



#most popular job titles.
jobs=dataset.Title.value_counts().to_frame()
#pie chart
jobs[jobs.Title>10].plot(kind='pie',figsize=(15,10),subplots=True)
#bar chart
jobs[jobs.Title>10].plot(kind='bar',figsize=(15,10))




#most popular job areas.
areas = dataset.Location.value_counts().to_frame()
#pie chart
areas[areas.Location>10].plot(kind='pie',figsize=(15,10),subplots=True)
#bar chart
areas[areas.Location>10].plot(kind='bar',figsize=(15,10))



#most required skills
skills = dataset.Skills.value_counts().to_frame()

####
###