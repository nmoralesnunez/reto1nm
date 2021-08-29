from flask import Flask, Response
import requests
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'
    return query_string
    
@app.route("/catfact")
def catfact():

    url = "https://catfact.ninja/fact"
    r = requests.get(url)
    fact = r.json()
    printable_fact = fact['fact']
    #print to console
    print("Did you know?: " + printable_fact)
    return Response(json.dumps(fact))

@app.route("/get-price/<ticker>")
def get_price(ticker):
    url = f"https://query2.finance.yahoo.com/v10/finance/quoteSummary/{ticker}?modules=price%2CsummaryDetail%2CpageViews%2CfinancialsTemplate"
    headers={'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url,headers=headers)
    company_info = response.json()

    print(company_info)

    price = company_info['quoteSummary']['result'][0]['price']['regularMarketPrice']['raw']
    company_name = company_info['quoteSummary']['result'][0]['price']['longName']
    exchange = company_info['quoteSummary']['result'][0]['price']['exchangeName']
    currency = company_info['quoteSummary']['result'][0]['price']['currency']

    result = {
        "precio": price,
        "nombre": company_name,
        "exchange": exchange,
        "currency": currency
    }
    print(result)

    return Response(json.dumps(result))

if __name__ == '__main__':
    app.run()

