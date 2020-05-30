import os
from questrade_api import Questrade 
from collections import defaultdict

if __name__ == "__main__":

    key = os.environ.get('QUESTRADE_API_KEY')

    if key is None: 
        print('ERROR: Environment variable QUESTRADE_API_KEY not set.')
         
        
    try:
        q = Questrade(refresh_token=key) 
        # After run the first time, can create object without initializing with ref token 
    except Exception as e:
        q = Questrade()
        
    time = q.time['time']

    accounts_raw = q.accounts['accounts']
    accounts = defaultdict(dict)
    for acc in accounts_raw:
        accounts[acc['number']]['type'] = acc['type']
        
    for acc_num in accounts:
        handler = q.account_balances(acc_num)
        accounts[acc_num]['balance_usd'] = handler['perCurrencyBalances'][1]['totalEquity']
        
    if not os.path.isdir('data'):
        os.mkdir('data')
        
    for acc_num in accounts:
        with open(os.path.join('data', acc_num + '.csv'), 'a') as f:
            f.write(time + ',' + str(accounts[acc_num]['balance_usd']) + '\n')
            