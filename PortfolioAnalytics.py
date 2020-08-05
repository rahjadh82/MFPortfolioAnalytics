#PortfolioAnalytics.py

import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.max_rows", None, "display.max_columns", None)

mfHoldingsFileName = r'''C:\Users\Shaurya\Desktop\Imp Docs\Savings\MyMFHoldings.csv'''
holdings_df = pd.read_csv(mfHoldingsFileName, encoding= 'unicode_escape')


total_unique_secs = holdings_df['security_name'].nunique()
print(f"Total unique stocks held: {total_unique_secs}")


holdings_by_sec_count_df = holdings_df['security_name'].value_counts(sort=True)
print(f"\n\nSecurity holdings across funds by count:\n{holdings_by_sec_count_df}")
sec_held_in_more_than_1_fund_df = holdings_by_sec_count_df[holdings_by_sec_count_df > 1]
print(f"\n\nSecurities held in more than 1 fund:\n{sec_held_in_more_than_1_fund_df}")

holdings_by_sec_value_df = holdings_df.groupby('security_name').my_holding_of_sec.agg([sum]).sort_values(by='sum', ascending=False)
print(f"\n\nSecurity holdings across funds by value:\n{holdings_by_sec_value_df}")
top_10_holdings_by_value_df = holdings_by_sec_value_df[holdings_by_sec_value_df['sum'] >= 20000 ]
print(f"\n\nTop 10 Securities by value:\n{top_10_holdings_by_value_df}")
