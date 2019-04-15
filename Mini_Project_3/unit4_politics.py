import pandas as pd
import matplotlib.pyplot as plt


def politicsEffect():
    '''
    to see the effect of political party on stock market index.
    There are lots of factors which affect the price together.
    Thus we cannot make conclusion based ona single factor.
    :return:
    '''
    # Only has data since 1950 and 1985
    # df = getPandasYahooData(['^GSPC','^DJI'],date(1920,1,1),date(2018,2,1))

    ind = pd.read_csv('IndexFile.csv')
    ind['SPCreturns'] = ind['SPC'] / ind['SPC'].shift(1)
    ind['DJIreturns'] = ind['DJI'] / ind['DJI'].shift(1)
    indgroupParty = ind[['President', 'SPCreturns',
                         'DJIreturns']].groupby('President').sum()
    indgroupParty.plot(kind='barh')
    plt.show()

    indgroupParty = ind[['Party', 'SPCreturns',
                         'DJIreturns']].groupby('Party').sum()
    indgroupParty.plot(kind='barh')
    plt.show()

    indgroupParty = ind[['Party', 'SPCreturns',
                         'DJIreturns']].groupby('Party')
    print(indgroupParty.describe())


if __name__ == '__main__':
    politicsEffect()
