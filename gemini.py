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
    print(datetime.datetime.now(), "- INFO: Retrieving tickers")
    ticker_url = "https://api.gemini.com/v1/symbols"
    response = requests.get(ticker_url)
    tickers = sorted(response.json())

    while True:
        for i in range (0, len(tickers)):
            # Get general information about specific ticker from list of tickers. 
            # The information that will be of use is: open price (opening price 24hr ago), ask (current best offer)
            timestamp = datetime.datetime.now()
            specificTicker = tickers[i]
            tickerURL = "https://api.gemini.com/v2/ticker/" + specificTicker
            tickerInfo = requests.get(tickerURL).json()
            
            # On 3/22/2021, 7 more tickers were added, some of which had no information (or None) in certain keys
            # The code below is to account for these new tickers without information, as the code would throw errors if no information was present
            if tickerInfo['ask'] == None:
                continue
            print(timestamp, "- INFO: Fetched", specificTicker, "information")

            # uncomment line below to adhere to API rate limits
            # time.sleep(1.0)

            # Retrieve and compute price information
            openPrice = float(tickerInfo['open'])
            currentPrice = float(tickerInfo['ask'])
            percentPriceChange = get24hrPriceChange(currentPrice, openPrice)
            # Price change threshold exceeded
            if abs(percentPriceChange) > userInputFloat:
                print(timestamp, "- ERROR:", specificTicker, "***** PRICE CHANGE *****")
            # Price change threshold NOT exceeded (in either direction, +/-)
            else:
                print(timestamp, "- INFO:", specificTicker, "has not exceeded threshold")
            # Print general information on the ticker of interest, regardless of price change status
            print(timestamp, "|", specificTicker, "| Current price:", currentPrice, "| Open price:", openPrice, "| % change:", round(percentPriceChange, 2))    
            


def get24hrPriceChange(finalPrice, startPrice):
    result = ((finalPrice - startPrice) / startPrice) * 100
    return result


if __name__ == "__main__":
    main()
