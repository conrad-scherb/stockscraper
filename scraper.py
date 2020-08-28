import requests, json, datetime, os, time, sqlManager

def pullStockData(ticker, token, apiMode):
    url = "https://" + apiMode + ".iexapis.com/stable/tops?token=" + token + "&symbols=" + ticker
    resp = requests.get(url)
    return resp.json()[0] #.json() chucks the dict into a list so extract list element as dict

def recordJsonToSQL(ticker, data):
    currTime = str(datetime.datetime.now())[0:19]
    price = data['lastSalePrice']
    sqlManager.insertStock(ticker, currTime, price)

with open(os.path.relpath('auth.json')) as json_file:
    auths = json.load(json_file)

#change this on use
mode = "TEST"

if mode == "TEST":
    token = auths["testToken"]
    apiMode = "sandbox"
elif mode == "REAL":
    token = auths["realToken"]
    apiMode = "cloud"

data = 0
tickers = []

while True:
    print("Enter a stock ticker symbol to scrape from (press X to exit): ")
    newTicker = input().lower()
    print(newTicker)
    if newTicker == "x":
        print("got here")
        break
    tickers.append(newTicker)

while True:
    for tick in tickers:
        data = pullStockData(tick, token, apiMode)
        recordJsonToSQL(tick, data)
    time.sleep(0.5)