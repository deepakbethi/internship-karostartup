# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# importing libraries
import ast
import os
import pandas as pd
import numpy as np

os.chdir("D:\internship")
d = pd.read_excel("skill_data.xlsx")
d1 = d.copy()
web_devloper_skills = [
    'django',
    'html',
    'css',
    'nodejs',
    'reactjs',
    'nodejs',
    'flask',
    'laravel'
]

machine_learning_skills = [
    'nosql',
    'pandas',
    'numpy',
    'matpotlib',
    'seabron',
    'scipy'
]
# changing string to list
for i in range(len(d1.Skills)):
    (d1.Skills[i]) = ast.literal_eval(d1.Skills[i])

# removing duplicates of skills
for i in range(len(d1.Skills)):
    d1.Skills[i] = list(dict.fromkeys(d1.Skills[i]))

# to find disignation
c1 = 0
c2 = 0
li = []
for i in range(len(d1.Skills)):
    for j in range(len(d1.Skills[i])):
        if ((d1.Skills[i])[j] in web_devloper_skills):
            c1 = c1 + 1
        if ((d1.Skills[i])[j] in machine_learning_skills):
            c2 = c2 + 1

    if (c1 >= 3 or c2 >= 3):
        if (c1 > c2):
            li.append("web developer")
        elif (c2 > c1):
            li.append("machine learning developer")
        else:
            li.append("Both")
    else:
        li.append("Not eligible")

    c1 = 0
    c2 = 0
# to find total courses
li2 = []
for i in range(len(d1.Skills)):
    li2.append(len(d1.Skills[i]))

d1["Disignation"]=li
d1["Total skills"]=li2

d1.to_excel(r'D:\csv files\skills_disignation.xlsx', index = False)


