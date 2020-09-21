#%%
#Learning accounting and python at the same time. Turning accounting concepts into python scripts.

import datetime

Equity = 0
Assets = 0
Liabilities = 0
OpeningContributedCapital = 1000
IssuedShares = 0
RepurchasedShares = 0
RetainedEarnings = 0
OpeningRetainedEarnings = 0
NetEarnings = 0
Revenues = 0
Expenses = 0
Dividends = 0

def Statement_of_Earnings(Revenues, Expenses):
    NetEarnings = Revenues - Expenses
    return NetEarnings

def Statement_of_Changes_in_Equity(OpeningContributedCapital, IssuedShares, RepurchasedShares):
    ContributedCapital = OpeningContributedCapital + IssuedShares - RepurchasedShares
    RetainedEarnings = OpeningRetainedEarnings + NetEarnings - Dividends
    Equity = ContributedCapital + RetainedEarnings
    return Equity

def Satement_of_Financial_Position(Assets, Liabilities, Equity):
    assert Assets == Equity + Liabilities


# %%
