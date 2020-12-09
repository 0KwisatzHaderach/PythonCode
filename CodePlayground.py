#%%
#Round money by the nearest nickel value. 2.33 = 2.35


def rounding(value, base=5):
    return int(base * round(float(value)/base))

for i in range (0,10000):
    rounded =rounding(i)/100
    print(rounded)

# %%
