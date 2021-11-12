# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     notebook_metadata_filter: markdown
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# ## Topics in Pandas
# **Stats 507, Fall 2021** 
#   

# ## Contents
# Add a bullet for each topic and link to the level 2 title header using 
# the exact title with spaces replaced by a dash. 
#
# + [Topic Title](#Topic-Title) 
# + [Topic 2 Title](#Topic-2-Title)
# + [DataFrame Method: `select_dtypes()`](#DataFrame-Method:-`select_dtypes()`) 

# ## Topic Title
# Include a title slide with a short title for your content.
# Write your name in *bold* on your title slide. 

# ## DataFrame Method: `select_dtypes()`
# *Brody Erlandson*
# berlands@umich.edu
#
# We can select the columns with a specific type(s), and/or exclude columns
# with a specific type(s).
#   
# - Parameters:
#   - include: scalar or list-like. Default None.
#   - exclude: scalar or list-like. Default None.
# - Returns: DataFrame

# ## `select_dtypes()` Example

df = pd.DataFrame({"strings1" : ["a", "b", "c"], "ints" : [1, 2, 3],
                   "floats" : [.1, .2, .3], 
                   "category" : ["cat1", "cat1", "cat2"],
                   "string2" : ["x", "y", "z"]})
df = df.convert_dtypes()
df["category"] = df["category"].astype("category")
df.select_dtypes(include=["string", "category"])

# Similarly:

df.select_dtypes(exclude=[float, int])

# ## When to use `select_dtypes()`
#
# Say you have a lot of columns of different types. You'd like to apply some
# function to only one type. Instead of finding all the indices or names
# of the columns, we can use `select_dtypes()` to get these columns.  
# 
# For example:   

df.select_dtypes(include="string").apply(lambda x : x + "_added")