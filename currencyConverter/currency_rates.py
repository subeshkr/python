# currency_rates.py
import numpy as np

RATES = {
    "AUDUSD": 0.8371,
    "CADUSD": 0.8711,
    "USDCNY": 6.1715,
    "EURUSD": 1.2315,
    "GBPUSD": 1.5683,
    "NZDUSD": 0.7750,
    "USDJPY": 119.95,
    "EURCZK": 27.6028,
    "EURDKK": 7.4405,
    "EURNOK": 8.6651,
}

DECIMALS = {
    "JPY": 0,
    "DEFAULT": 2,
}


#defining index array to zearch cross currency
indxArray = np.array(['AUD','CAD','CNY','CZK','DKK','EUR','GBP','JPY','NOK','NZD','USD'])
#defining cross currency matrix
crossCurrencyMat = np.array([['01:01','USD','USD','USD','USD','USD','USD','USD','USD','USD','D'],
                            ['USD','01:01','USD','USD','USD','USD','USD','USD','USD','USD','D'],
                            ['USD','USD','01:01','USD','USD','USD','USD','USD','USD','USD','D'],
                            ['USD','USD','USD','01:01','EUR','Inv','USD','USD','EUR','USD','EUR'],
                            ['USD','USD','USD','EUR','01:01','Inv','USD','USD','EUR','USD','EUR'],
                            ['USD','USD','USD','D','D','01:01','USD','USD','USD','USD','USD'],
                            ['USD','USD','USD','USD','USD','USD','01:01','USD','USD','USD','D'],
                            ['USD','USD','USD','USD','USD','USD','USD','01:01','USD','USD','Inv'],
                            ['USD','USD','USD','EUR','EUR','Inv','USD','USD','01:01','USD','EUR'],
                            ['USD','USD','USD','USD','USD','USD','USD','USD','USD','01:01','D'],
                            ['Inv','Inv','Inv','EUR','EUR','Inv','Inv','D','EUR','Inv','01:01']])