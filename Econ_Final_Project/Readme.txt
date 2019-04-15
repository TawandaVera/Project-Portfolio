1. The code was developed on Windows 10 Pro, Core i3, Using Python 3.6 & Spyder IDLE in Anaconda 3. The code should work on other OS and Python 3 compatible IDLEs.

NB: The code takes around 3- 10 minutes to load the simulated Auto.Arima function for estimating the best SARIMAX model Still needs a bit of tweaking,
to improve the times. An alternative would be to replace the SARIMAX with tsa.ARMA, which is faster but gave a different optimal pdq.

Data is collected from the Quandl dataset, which is 1 week behind to the World Gold Council (WGC) Gold price data. The Quandl free download after 50 times requires an API key to acce
2. Installing Packages, so i have downloaded and attached current data from WGC, which was used to compare with the forecasted gold prices.

We start by creating a new directory for our project. 
We will call it ECON_FINAL_PROJECT and then move into the directory.

This project will require the sys, warnings, itertools, pandas, numpy, matplotlib and statsmodels libraries.
	The calendar, warnings and itertools libraries come included with the standard Python library set so there is no need to install them.
The other Python packages, we can install these requirements with pip. 
We need to install quandl, numpy, scipy, pandas, statsmodels, and the data plotting package matplotlib.

Their dependencies will also be installed:
•	pip install quandl pandas numpy statsmodels matplotlib
Then we are now set up to start working with the installed packages.

Importing Packages and Loading Data
To begin working with our data, we will start up Spyder through Anaconda 3:

fivethirtyeight is the defined matplotlib style our plots will use.
