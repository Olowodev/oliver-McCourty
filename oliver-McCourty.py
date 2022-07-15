import math

def commission_function(amountPaid):
    commission = (10/100) * amountPaid
    commission = math.floor(commission)
    print(commission)

commission_function(103450.34526)