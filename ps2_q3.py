# # Imports

import numpy as np
from numpy.random.mtrand import randint
import pandas as pd
import time
from IPython.core.display import display, HTML

# # Question 3
# ## Part a
# Reading the data in

root = "data/"

cols = ["SEQN", "RIDAGEYR", "RIDRETH3", "RIAGENDR",
        "DMDEDUC2", "DMDMARTL", "RIDSTATR", 
        "SDMVPSU", "SDMVSTRA", "WTMEC2YR", 
        "WTINT2YR"]
demo_11_to_18 = pd.concat([pd.read_sas(
                        root + "DEMO_G.XPT")[cols].assign(cohort="11-12"),
                        pd.read_sas(
                        root + "DEMO_H.XPT")[cols].assign(cohort="13-14"), 
                        pd.read_sas(
                        root + "DEMO_I.XPT")[cols].assign(cohort="15-16"), 
                        pd.read_sas(
                        root + "DEMO_J.XPT")[cols].assign(cohort="17-18")])

# changing the column names

newColNames = {"SEQN" : "id", "RIDAGEYR" : "age", "RIAGENDR" : "gender",
               "RIDRETH3" : "race_ethn", "DMDEDUC2" : "education", 
               "DMDMARTL" : "marital_status", 
               "RIDSTATR" : "exam_status", 
               "SDMVPSU" : "pseudo-psu_var_est.", 
               "SDMVSTRA" : "pseudo-stratum_var_est.", 
               "WTMEC2YR" : "mec_exam_weight", 
               "WTINT2YR" : "interview_weight"}
demo_11_to_18 = demo_11_to_18.rename(newColNames, axis=1)

# changing data types

demo_11_to_18 = demo_11_to_18.convert_dtypes()
demo_11_to_18["age"] = demo_11_to_18["age"].astype("int8")
catCols = ["cohort", "race_ethn", 
           "education", "marital_status",
           "exam_status"]
demo_11_to_18[catCols] = demo_11_to_18[catCols].astype("category")
demo_11_to_18.dtypes

# changing gender as I did in pset4

new_gender_cat = {1 : "Male",
                  2 : "Female"}
demo_11_to_18["gender"] = (demo_11_to_18["gender"].replace(new_gender_cat)
                                                  .astype("category"))
                                                  
# saving data

demo_11_to_18.to_pickle("demo11to18.pickle")

# ## part b

cols = ["SEQN", "OHDDESTS"]
for n in range(2, 32):
    if n < 10:
        cols.append("OHX0" + str(n) + "CTC")
    elif (n == 16) or (n == 17):
        continue
    else:
        cols.append("OHX" + str(n) + "CTC")
for n in range(1, 33):
    if n < 10:
        cols.append("OHX0" + str(n) + "TC")
    else:
        cols.append("OHX" + str(n) + "TC")

oralHlthDen11to18 = pd.concat([pd.read_sas(
                       root + "OHXDEN_G.XPT")[cols].assign(cohort="11-12"),
                       pd.read_sas(
                       root + "OHXDEN_H.XPT")[cols].assign(cohort="13-14"), 
                       pd.read_sas(
                       root + "OHXDEN_I.XPT")[cols].assign(cohort="15-16"), 
                       pd.read_sas(
                       root + "OHXDEN_J.XPT")[cols].assign(cohort="17-18")])

# changing the column names

newColNames = {"SEQN" : "id",
               "OHDDESTS" : "dentition_code"}
for col in cols[2:]:
    if col[-3:] == "CTC":
        newColNames[col] = "ctc" + col[-5:-3]
    else:
        newColNames[col] = "tc" + col[-4:-2]


oralHlthDen11to18 = oralHlthDen11to18.rename(newColNames, axis=1)

# changing the types

bStrCols = oralHlthDen11to18.columns[oralHlthDen11to18.dtypes 
                                     == "object"][:-1]
for col in bStrCols:
    oralHlthDen11to18[col] = oralHlthDen11to18[col].str.decode('utf-8')

oralHlthDen11to18 = oralHlthDen11to18.convert_dtypes()
oralHlthDen11to18["cohort"] = oralHlthDen11to18["cohort"].astype("category")
oralHlthDen11to18.dtypes

# saving data

oralHlthDen11to18.to_pickle("oralHlthDen11to18.pickle")

# ## Part c

numCases = oralHlthDen11to18.shape[0] + demo_11_to_18.shape[0]
