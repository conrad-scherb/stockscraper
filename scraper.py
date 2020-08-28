import requests, json, datetime, os, time

def pullStockData(ticker, token, apiMode):
    url = "https://" + apiMode + ".iexapis.com/stable/tops?token=" + token + "&symbols=" + ticker
    resp = requests.get(url)
    #if resp.json() == []: 
    #    print("That is not a valid ticker!")
    #    return 0
    return resp.json()

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
ticker = ""
while data == 0:
    print("Enter a stock ticker symbol to scrape from: ")
    ticker = input().lower()
    data = pullStockData(ticker, token, apiMode)


filepath = os.path.relpath("data/" + ticker + ".json")

while True:
    data = pullStockData(ticker, token, apiMode)
    currTime = str(datetime.datetime.now())[0:19]

    with open(filepath) as json_file:
        newData = json.load(json_file)

    newData[currTime] = data
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(newData, f, ensure_ascii=False, indent=4)
    
    time.sleep(1)