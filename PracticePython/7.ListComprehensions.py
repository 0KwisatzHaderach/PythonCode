#%%

#Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [i for i in a if i % 2 == 0]
print(b)

#%%

#Determine age for a list of birthyears:

current_year = 2020
years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]

ages = [current_year - year for year in years_of_birth]
print(ages)