import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
def drawCode(code):
    database = json.load(open("database.json","r"))
    lis = database[code]
    prices = []
    times = []
    for item in lis:
        prices.append(item)
    print(prices)
    df =  pd.DataFrame(prices)
    df.plot()
    plt.show()

if __name__ == '__main__':
    drawCode("14D")