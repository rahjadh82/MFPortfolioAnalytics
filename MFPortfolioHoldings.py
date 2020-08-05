#MFPortfolioHoldings.py

from bs4 import BeautifulSoup
import requests
import csv


def getHoldingsData(url):
    response = requests.get(url, timeout=5)
    content = BeautifulSoup(response.content, "html.parser")
    holdingsTable = content.find(id="equityCompleteHoldingTable").find('tbody')
    rows = holdingsTable.find_all('tr')

    holdingsData = []
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        holdingsData.append(cols)
    return holdingsData

def getOutputdataForFundHolding(fund_name,invested_amount,holding):
    security_name = holding[0].replace("\n","").replace("#","")
    sector = holding[1]
    perct_of_fund = float(holding[4].replace("%", ""))
    my_holding_of_sec = invested_amount * perct_of_fund * 0.01
    output = [fund_name, security_name, sector, perct_of_fund, my_holding_of_sec]
    return(output)

def writeToCsv(outputData):
    with open(r'''C:\Users\Shaurya\Desktop\Imp Docs\Savings\MyMFHoldings.csv''', 'w', newline='') as file:
        writer = csv.writer(file)
        header = ["fund_name", "security_name", "sector", "perct_of_fund", "my_holding_of_sec"]
        writer.writerow(header)
        for row in outputData:
            writer.writerow(row)

outputData = []
with open(r'''C:\Users\Shaurya\Desktop\Imp Docs\Savings\MyMFData.csv''') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for row in csv_reader:
       url = row['url']
       fund_name = row['fund_name']
       invested_amount = float(row['amount'])
       holdingsData = getHoldingsData(url)

       for holding in holdingsData:
           outputData.append(getOutputdataForFundHolding(fund_name,invested_amount, holding))

writeToCsv(outputData)
