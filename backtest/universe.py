from log3 import log
from settings import PATH_TO_STOCKS_FOLDER
import os


class Universe(object):

    def __init__(self, tickers, name):
        self.tickers = tickers
        self.name = name

        self.remove_tickers_not_in_local_db(tickers)

    def blacklist(self, blacklist):
        """ Removes tickers located in blacklist

        Args:
            blacklist (list): List of blacklisted stocks

        Returns:

        """
        for item in blacklist:
            if item in self.tickers:
                self.tickers.remove(item)

    def add_ticker(self, ticker):
        """
        Add a specific ticker to your Universe
        """
        pass

    def remove_tickers_not_in_local_db(self, tickers):
        """ Check if each ticker is in the local database. If not remove it from universe

        Args:
            tickers (list): Check if tickers exists locally

        """

        for ticker in tickers[:]:
            path = os.path.join(PATH_TO_STOCKS_FOLDER, '%s.txt' % ticker)

            # path = '/Users/system-void/gdrive/code/data/stocks/5min/%s.txt' % ticker
            try:
                # Get the size (lines) of file (must open file)
                size = sum(1 for l in open(path))
            except Exception as ex:
                log.info(
                    '%7s - Ticker not found in local equity database. Removing from universe'
                    % ticker)
                #print ex
                self.tickers.remove(ticker)
