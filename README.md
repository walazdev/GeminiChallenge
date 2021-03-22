# Gemini Cryptocurrency Alerts
This Python program tracks all cryptocurrency pairs supported by the Gemini public API, printing alerts and information 
based on user input.

## Usage
NOTE: This program was written with Python 3.9.2. Older versions might not be compatible.
To run the program, make sure that you are in the correct directory.
Once you're there, you can simply type:

```python gemini.py [% threshold]```

Where [% threshold] is percent change in price that will trigger an ERROR-specific alert.
The program will run indefinitely until the user issues a stop command. 
In order to stop the program, you will have to press: CTRL + C or CMD + C, depending on your Operating System. 

An example run looks like:

```python gemini.py 3.5```

Where the program will output ERROR messages whenever any ticker's percent price change exceeds 3.5% in either direction (+/-)

## Dependencies
This program will need require pip, which will be used to install other packages. 
For information on how to install pip, visit the pip [documentation](https://pip.pypa.io/en/stable/installing/)

After installing pip, make sure to install PyPi. You can find how to do it [here](https://pypi.org/project/pypi-install/)

Finally, install [requests](https://pypi.org/project/requests/)

## Improvements and further features
Currently, the program only tracks percent price changes. Adding alerts for (1) price deviation and (2) volume deviation would be ideal

For trading purposes, adding alerts for specific prices (determined by user input) might be beneficial. This could be used to track major milestones, like BTC hitting $60k USD 
or if a currency drops below a certain price.

The program tracks and prints information for ALL the tickers available on the Gemini public API. The next step would be to allow users to choose which tickers they would like to track
via command line inputs.

Similarly, if more features such as (1) and (2) are to be added, the program should also allow the user to choose a combination of alerts that they would like to receive (e.g. percent price change + volume deviation)

As an attempt to generate further profits, calculating the risk and possible gains from the bid-ask spread could be particularly helpful.

Computing Simple Moving Averages (SMA) and Exponential Moving Averages (EMA) can prove useful when it comes to deciding whether to buy a certain cryptocurrency or not.

SMA and EMA can be used to identify "hype" periods of popular cryptocurrencies like BTC and ETH. Identifying these points in the market provides better information as to whether it might be a good time to buy and/or sell.

## Issues with implementation
I had multiple versions of Python due to some courses in the past requiring different versions. This became a problem when I tried to compile my work, as WSL wasn't sure what version to use and figuring this out was rather tricky.

I had to install Python 3.9.2 and configure the venv appropriately. This whole process took a couple of hours to get it working.

On a more assignment-specific note, I don't have much experience with Python and I have no experience handling APIs, so I had to do a fair amount of research
before starting the assignment. I factored this research time into the overall assignment time.

When I started off, I was using the `Price feed` URL, which I then completely ditched because I saw that some of the information strayed too much from other online sources.

If I understand correctly, the `percentChange24h` field of the `Price feed` only tracks information executed on Gemini's order book, some of which was very different from online sources.

## Time breakdown
1hr30m: Researching REST APIs in general, reading over Gemini's public API, brushing up on Python dictionaries.

30m: Playing around with Gemini's APIs and printing output. Comparing Gemini's information with other info online to double check

1hr30m: Actual coding and testing. Around 30m of this alloted time was "wasted" because I believed that I wasn't using the correct API (Price feed)

20m: Wrinting this README, thinking about possible future improvements, adding comments to the finalized code.

Total time: Around 3hr50m

