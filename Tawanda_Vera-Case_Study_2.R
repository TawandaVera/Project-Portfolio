########################################################################
#The files submited include this R.script, the Rstudio project file,   
# the CaseStudy2.RData file, and the Plot.pdf files with the plots.

 
#######################################################################
# Question 1: Download Data for 1 year for 5 technology stock tickers #
#######################################################################

#the analysis requires quantmod and performanceAnalytics packages
# the Analysis was done in R.IDE (Rstudio Version 1.0.143, Microsoft R Open 3.4.0)
# the packages use include the quantmod, performanceAnalytics, combinat, 
# the install.packages(), and use it library () to start using it

library ('reshape2')
library ('quantmod')
library ('PerformanceAnalytics')
library ('xts')
library ("ggplot2")


#Since,the analysis was for 1 year, the startdate was set to 2016-01-01, inorder to
# download data starting from the start date.

startdate <- '2016-05-31'

#the 5 technology tickers chosen are Microsoft, Yahoo, Oracle,EBay and Cisco

tickers < - c( 'MSFT', 'YHOO', 'ORCL', 'EBAY', 'CSCO')

# the getSymbols.google(tickers, from = startdate) gave errors,  
# so the symbols were fetched seperately.

MSFT.price <- getSymbols.google(tickers[1], auto.assign = F, from = startDate)
YHOO.prices <- getSymbols.google(tickers[2], auto.assign = F, from = startDate)
ORCL.prices <- getSymbols.google(tickers[3], auto.assign = F, from = startDate)
EBAY.prices <- getSymbols.google(tickers[4], auto.assign = F, from = startDate)
CSCO.prices <- getSymbols.google(tickers[5], auto.assign = F, from = startDate)

# To convert month end prices:

MSFT.monthly.prices <- aggregate(MSFT.price, as.yearmon, tail, 1)
YHOO.monthly.prices <- aggregate(YHOO.prices, as.yearmon, tail, 1)
ORCL.monthly.prices <- aggregate(ORCL.prices, as.yearmon, tail, 1)
EBAY.monthly.prices <- aggregate(EBAY.prices, as.yearmon, tail, 1)
CSCO.monthly.prices <- aggregate(CSCO.prices, as.yearmon, tail, 1)

#merge is used to combine the stock close prices into a portfolio of equally weighted prices,
#merge Cl() is used, since I used google finance data, the google data does not have adjusted close column we use Close
# we add the na.omit to remove any NA values, 

Portfolio.prices <- na.omit(merge(Cl(MSFT.monthly.prices), Cl(YHOO.monthly.prices), Cl(ORCL.monthly.prices),
                                  Cl(EBAY.monthly.prices), Cl(CSCO.monthly.prices)))

#The column names are renamed using tickers to MSFT, YHOO and ORCL, EBAY, CSCO
colnames(Portfolio.prices) <- tickers



print(Portfolio.prices)


####################################################################################
#Question 2: Calculate Monthly returns of downloaded stock over the period under
#study 
###################################################################################

library ('quantmod')
library ('xts')


#The portfolio prices is first converted to the data.frame myportf
myportf <- data.frame(Portfolio.prices)

#then the portfolio prices are converted to a time series object, the time series
# object is then used in the portfolio returns formula

myportf.xts <- as.xts(Portfolio.prices)

# convert prices to log returns

r.monthly <- na.omit(diff(log(myportf.xts))) 

# Calculate Simple returns 

portfolio.returns <-diff(Portfolio.prices)/(lag(Portfolio.prices, k=-1)[1:13,])

# use thelog returns to convert the simple returns into an xts object

portfolio.returns.xts <- as.xts(portfolio.returns, order.by = index(r.monthly))


print(portfolio.returns)


####################################################################################
# 
# Question 3: Using the combination function, calculate Monthly returns of an equally
# weighted portfolio of any of the 3 stocks from the 5
#
###################################################################################

library ('quantmod')
library ('PerformanceAnalytics')


#The combination function is used to calculate all the possible combinations of the five
#stock

cmbn.names <- combn(tickers, 3, simplify = TRUE)

#Categories of the combinations, Using the first letters of the ticker, the combinantions
# are categorised. Due to naming conflicts with system, M.O.E was given M.O.EB and the full
#stop added  between the letters

colnames(cmbn.names) <- c('Date', M.Y.O', M.Y.E','M.Y.C','M.O.EB', 'M.O.C.', 'M.E.C', 'Y.O.E', 'Y.O.C', 'Y.E.C', 'O.E.C')

cmbn.names
M.Y.O  M.Y.E  M.Y.C  M.O.EB M.O.C. M.E.C  Y.O.E  Y.O.C  Y.E.C  O.E.C 
[1,] "MSFT" "MSFT" "MSFT" "MSFT" "MSFT" "MSFT" "YHOO" "YHOO" "YHOO" "ORCL"
[2,] "YHOO" "YHOO" "YHOO" "ORCL" "ORCL" "EBAY" "ORCL" "ORCL" "EBAY" "EBAY"
[3,] "ORCL" "EBAY" "CSCO" "EBAY" "CSCO" "CSCO" "EBAY" "CSCO" "CSCO" "CSCO"

#The portfolio.returns are first converted to into a data.frame (portfolio.returns.df)

portfolio.returns.df <- data.frame(portfolio.returns)


#The combination function is used to calculate the geometric mean of the portfolio returns
# averaged 3 at a time, the RowMean of the 3 is used as the Function since they are equally weighted, and simplified into
# the portfolio stock combination means are simplified to (portfolio combinations)

portfolio.combinations <- combn(portfolio.returns.df, 3, rowMeans, simplify = TRUE
portfolio.combinations.xts <- as.xts(portfolio.combinations, order.by = index(portfolio.returns.xts))

#The colnames for the portfolio combinations xts object are labelled.

colnames(portfolio.combinations.xts) <- colnames(cmbn.names)

# the xts is converted to dataframe

portfolio.combinations.df <- data.frame(portfolio.combinations.xts)


print(portfolio.combinations.df)




####################################################################################
# Question 4: Graphically represent the cumulative monthly returns for each        #
# possible portfolio through line plots
###################################################################################


# Plot cumulative returns using chart.CumReturns() in the PerformanceAnalytics package.
#Note we need to use simple returns instead of continuously compounded returns for this,
#the simple returns are calculated using diff() and lag() on the price data.

library (PerformanceAnalytics)


# We  use 'portfolio.combinations.xts' for the Graphical representation of the cumulative
#monthly returns for each possible portfolio through line plots. We use the Chart.CumReturns()
#function from 'PerformanceAnalytics' package.

portfolio.combinations.xts, main = 'Portfolio Cumulative Summary')

Chart.CumReturns(portfolio.combinations.xts, legend.loc="topleft", wealth.index=TRUE,
ylab="$", main="Future Value of $1 invested")


print(Rplot)

##################################################################################
# Question 5: Calculate Mean, Median and Standard deviation of the portfolios and#
# plot them on the cumulative returns graph                                         #
##################################################################################
 library ('quantmod')                         
library ('performanceAnalytics')
library("reshape2")
library("ggplot2")

# Calculate the combined monthly, mean, median and standard deviation

portfolio.combn.median <-cbind.data.frame(apply(portfolio.combinations.xts, 1, median))
portfolio.combn.mean <-cbind.data.frame(apply(portfolio.combinations.xts, 1, mean))
portfolio.combn.stddev <-cbind.data.frame(apply(portfolio.combinations.xts, 1, StdDev))
      
#Merge zoo them into combination summmary for ease of analysis
Portfolio.combination.Summary <- merge.zoo(portfolio.combn.mean,portfolio.combn.median, portfolio.combn.stddev)                   

#reshape the data with melt and then rename the colnames to mean, median, standard deviation
melt(Portfolio.combination.Summary)
colnames(Portfolio.combination.Summary) <- c('mean', 'median', 'StdDev')

#convert the data to a xts zoo class object using portfolio.combinations.xts
monthly.summary.xts <- as.xts(Portfolio.combination.Summary, order.by = index(portfolio.combinations.xts))

#convert portfolio.combinations.xts into cumulative returns and june 2016 are base

cum.reet <- (1+portfolio.combinations.xts)*(lag.xts((1+portfolio.combinations.xts), k=1))
cum.reet[1,] <- (1+portfolio.combinations.xts[1,]) 
cum.ret <- cum.reet-1

#For plotting them on the chart in QUestion 4, we merge zoo, the summaries to the data

question5plot.xts <- merge.zoo(monthly.summary.xts, cum.ret)
                    
  

#Plot using Chart.CumReturns and Use lines to plot mean,median and standard deviation
library(PerformanceAnalytics)

chart.CumReturns(portfolio.combinations.xts, legend.loc="topleft", wealth.index=TRUE,
                 ylab="$", main="Future Value of $1 invested")

#Performance Analytics shows two Chart.TimeSeries(), the other one presents the a color
# chart, while the one i used for Q5 is the black and white, which splits the y-axis

charts.TimeSeries(question5plot.xts)




##################################################################################
# Question 6 : Calculate the overall variance of the all the portfolios                      
#                                          
#################################################################################

#Overall Variance

max(var(portfolio.combinations.xts))
#[1] 0.002831253

min(var(portfolio.combinations.xts))
#[1] 0.000594718

mean(var(portfolio.combinations.xts))
#[1] 0.001476837

#overall standard deviation
sd(portfolio.combinations.xts)
#[1] 0.04206286

#overall variance
(sd(portfolio.combinations.xts))^2
#[1] 0.001769285

####################################################################################
#####################################################################################