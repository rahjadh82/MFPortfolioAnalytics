#PortfolioAnalytics.py

import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.max_rows", None, "display.max_columns", None)

mfHoldingsFileName = r'''C:\Users\Shaurya\Desktop\Imp Docs\Savings\MyMFHoldings.csv'''
holdings_df = pd.read_csv(mfHoldingsFileName, encoding= 'unicode_escape')


total_unique_secs = holdings_df['security_name'].nunique()
print(f"Total unique stocks held: {total_unique_secs}")


top_holdings_df = holdings_df['security_name'].value_counts(sort=True)
print(f"Top security holdings across funds by count:\n {top_holdings_df}")

#print(holdings_df.groupby('security_name').agg({'my_holding_of_sec':'sum'}).sort('my_holding_of_sec'))
top_holdings_by_value = holdings_df.groupby('security_name').my_holding_of_sec.agg([sum]).sort_values(by='sum', ascending=False)
print(f"\n\nTop security holdings across funds by value:\n {top_holdings_by_value}")
