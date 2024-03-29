# Scraping the NASDAQ
# Training deep neural nets is expensive! You might as well invest in NVIDIA stock since you're spending so much on GPUs. To pick the best time to invest, you are going to collect and analyze some data on how their stock is doing. The context manager stock('NVDA') will connect to the NASDAQ and return an object that you can use to get the latest price by calling its .price() method.
# You want to connect to stock('NVDA') and record 10 timesteps of price data by writing it to the file NVDA.txt.


# Use the stock('NVDA') context manager and assign the result to nvda.
# Open a file for writing with open('NVDA.txt', 'w') and assign the file object to f_out so you can record the price over time.
# Use the "stock('NVDA')" context manager
# and assign the result to the variable "nvda"
with stock('NVDA') as nvda:
  # Open "NVDA.txt" for writing as f_out
  with open('NVDA.txt', 'w') as f_out:
    for _ in range(10):
      value = nvda.price()
      print('Logging ${:.2f} for NVDA'.format(value))
      f_out.write('{:.2f}\n'.format(value))

# <script.py> output:
#     Opening stock ticker for NVDA
#     Logging $140.39 for NVDA
#     Logging $140.33 for NVDA
#     Logging $140.27 for NVDA
#     Logging $140.23 for NVDA
#     Logging $140.20 for NVDA
#     Logging $140.28 for NVDA
#     Logging $140.34 for NVDA
#     Logging $140.39 for NVDA
#     Logging $140.29 for NVDA
#     Logging $140.27 for NVDA
#     Closing stock ticker

# Super stock scraping! Now you can monitor the NVIDIA stock price and decide when is the exact right time to buy. Nesting context managers like this allows you to connect to the stock market (the CONNECT/DISCONNECT pattern) and write to a file (the OPEN/CLOSE pattern) at the same time.
