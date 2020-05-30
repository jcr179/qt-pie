# qt-pie
Simple portfolio reading/analysis tool for Questrade accounts.

How to use:
1. Replace "MY_KEY" in set_env.bat with your Questrade refresh token.
2. In a cmd terminal, run set_env.bat to set the environment variable.
3. (Optional) To automate recording updates of your balance, schedule read.py to run at desired frequency.
4. Run read.py to create a data folder and a csv file (openable with Excel, Google Sheets, etc.) for each of your accounts whenever you want to update balance records.

Currently only records total equity in USD.
