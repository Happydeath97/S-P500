#import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

DIC = {}
DATES = []
PRICES = []

def importing_data():
    with open("S&P500_VALUE.txt") as file:
        for line in file:
            (date_time, value) = line.split()
            DIC[date_time] = value
        file.close()

def extract_data():
    result = DIC.items()
    data = list(result)
    numpyArray = np.array(data)

    count = 0
    for x in numpyArray:
        for y in x:
            if count % 2 == 0:
                DATES.append(y)
            else:
                PRICES.append(y)
            count += 1


if __name__ == "__main__":

    importing_data()
    extract_data()
    print(DATES)
    print(PRICES)
    plt.plot(DATES, PRICES)
    plt.title("S&P500")
    plt.xlabel("Date")
    #plt.ylabel()
    plt.legend(["Price $"])
    plt.xticks(range(len(DATES)), DATES, rotation=25)
    #plt.gca().invert_yaxis()
    plt.show()
