#converter.py
import sys
import numpy as np
sys.path.append('C:/Users/subesh/Documents/Python Scripts')

from currency_rates import RATES, DECIMALS, indxArray, crossCurrencyMat

def find_rate(from_currency, to_currency):
    if from_currency == to_currency:
        return 1
    direct = f"{from_currency}{to_currency}"
    
    inverted = f"{to_currency}{from_currency}"
    if direct in RATES:
        return RATES[direct]
    elif inverted in RATES:
        return 1 / RATES[inverted]
    else:
        try:
            x = np.where(indxArray == from_currency)[0][0]
            y = np.where(indxArray == to_currency)[0][0]
        except:
            return None
        mapped_cur = crossCurrencyMat[x][y]
        rate_fcmc = find_rate(from_currency,mapped_cur)
        ratem_mctc = find_rate(mapped_cur,to_currency)
        return rate_fcmc*ratem_mctc

def convert(amount, from_currency, to_currency):
    rate = find_rate(from_currency, to_currency)
    if rate is None:
        return "Unable to find rate"
    decimals = DECIMALS.get(to_currency, DECIMALS["DEFAULT"])
    #print(decimals)
    return round(amount * rate, decimals)