import requests, json, sys, time, datetime

def main():
    userInput = sys.argv[1]
    try:
        userInputFloat = float(userInput)
    except ValueError:
        print("Usage: python3 gemini.py [% threshold]")
        print("[% threshold] has to be a number")
        sys.exit(1)
    if (len(sys.argv) != 2):
        print("Usage: python3 gemini.py [% threshold]")
        sys.exit(1)
    print("User % change threshold:", sys.argv[1])

    # get tickers and sort by alphabetical order
    ticker_url = "https://api.gemini.com/v1/symbols"
    response = requests.get(ticker_url)
    tickers = sorted(response.json())

    while True:
        i = 0
        while i < len(tickers):
            # Get general information about specific ticker from list of tickers. 
            # The information that will be of use is: open price (opening price 24hr ago), ask (current best offer)
            specificTicker = tickers[i]
            tickerURL = "https://api.gemini.com/v2/ticker/" + specificTicker
            tickerInfo = requests.get(tickerURL).json()
            # uncomment line below to adhere to API rate limits
            # time.sleep(1.0)
            timestamp = datetime.datetime.now()
            openPrice = float(tickerInfo['open'])
            currentPrice = float(tickerInfo['ask'])
            percentPriceChange = get24hrPriceChange(currentPrice, openPrice)
            print(openPrice, currentPrice)
            if abs(percentPriceChange) > userInputFloat:
                percentPriceChange = round(percentPriceChange, 2)
                print("WARNING, PRICE CHANGE OVER THRESHOLD", tickerInfo['symbol'], percentPriceChange, "%")
            else:
                print("all good", tickerInfo['symbol'])
            i += 1
        # generalInfo = "https://api.gemini.com/v1/pubticker/btcusd"
        # openInfo = "https://api.gemini.com/v2/ticker/btcusd"
        # response = requests.get(generalInfo)
        # prices = response.json()
        # # Sort prices by alphabetical order
        # prices = sorted(prices, key = lambda i: i['pair'])
        # item = 0
        # # make all tickers in prices lowercase for comparing purposes later on
        # while item < len(prices):
        #     prices[item]['pair'] = prices[item]['pair'].lower()
        #     item += 1
        # # for rate limiting purposes
        # time.sleep(1.0)
        # response = requests.get(tickers)
        # # sort info by alphabetical order
        # info = sorted(response.json())
        # # length of prices and info == 50
        # i = 0
        # while i < len(prices):
        #     # print(info[i])
        #     # print(prices[i]['pair'])
        #     ticker = info[i]
        #     if abs(float(prices[i]['percentChange24h'])) >= userInputFloat:
        #         print(ticker, "% change: ", prices[i]['percentChange24h'])
        #         print("WARNING, THRESHOLD EXCEEDED")
        #     else:
        #         print(ticker, "% change: :", prices[i]['percentChange24h'], "all good")

        #     # if prices[i]['pair'] == 'BTCUSD':
        #     #     print("Found BTCUSD, % change: ", prices[i]['percentChange24h'])
        #     #     if abs(float(prices[i]['percentChange24h'])) >= userInputInt:
        #     #         print("WARNING, THRESHOLD EXCEEDED")
        #     #     else:
        #     #         print("all good, threshold not exceeded")
        #     i += 1
        # print("next wave")
        # #print(prices[0])
        # # print(prices)
        # time.sleep(1.0)


def get24hrPriceChange(finalPrice, startPrice):
    result = ((finalPrice - startPrice) / startPrice) * 100
    return result





if __name__ == "__main__":
    main()
