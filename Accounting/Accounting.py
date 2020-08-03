#%%
#Learning accounting and python at the same time. Turning accounting concepts into python scripts.

import datetime

Equity = 0
Assets = 0
Liabilities = 0
CommonStock = 1000
RetainedEarnings = 0
Revenues = 0
Expenses = 0
Dividends = 0

#Equity = Assets - Liabilities

def FinalAssets(Equity, Liabilities, CommonStock, Revenues, Expenses, Dividends):
    RetainedEarnings = Revenues - Expenses - Dividends
    Equity = CommonStock + RetainedEarnings
    Assets = Equity + Liabilities
    print(f"Assets at are equal to {Assets}")
    return Assets

Assets = FinalAssets(Equity, Liabilities, CommonStock, Revenues, Expenses, Dividends)

print(Assets)


# %%
