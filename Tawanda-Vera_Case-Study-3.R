#################################################################
#1.	Consider following values for the purpose of this project:  # 
#  a.	St =10$
#  b.	r= 0.15 (15% expected return per year)
#  c.	sigma =0.20 (20% annual volatility in prices)
#  d.	T = 1 year
#  e.	N=100
#  f.	e=0.15
#St+1 = function(st, r, sigma, t, n, e) {
dt = t / n # dt = size of the nit step size

returnValue(st * exp((r - 0.5 * sigma^2)*dt + sigma * e * sqrt(dt)))
# 10.04309

###################################################
# Step 1
# Set initial values
####################################################

St = 10         # Initial stock price
r = 0.15         # 15 % expected annual stock return per year
sigma = 0.2      # 20% annualized volatility in prices
t = 1            # 1 year
n = 100          # 100 steps
e = 0.15   #a random value from a normal sample)
nextPrice = function(st, r, sigma, t, n, e) {
  +     dt = t / n # dt = size of the Nit step size
  +     return(st * exp(((r - (0.5 * (sigma ^ 2))) * dt) + (sigma * e * sqrt(dt))))}

######################################################### 
# Step 2
# Calculate the expected value of the stock price at
# the end of every successive dt interval of time
#########################################################

prices <- price.delta(st,r,sigma,t,n, epsilon=e, F)

print(prices)

# to cross check the prices

library (emdbook)
# emdbook contains lseq() is just a wrapper for exp(seq(log(from),
#log(to), length.out = length.out))

lseq(st, returnValue(st * exp((r - 0.5 * sigma^2)*dt + 
                                sigma * e * sqrt(dt))^(n-1)), 
     length.out = n)


#########################################################
# Step 3
# Plot the entire movement of prices over tht T 
# period under observation
#########################################################

plot(prices,
     main = 'movement of prices over the T period',
     xlab = 'Step', 
     ylab = 'Stock Price', 
     xlim = c(0, 100), 
     ylim = c(0, 20), 
     type='l')

####################################################################################
# Step 4
# Randomly assign values to ε from a standard normal 
# distribution
###################################################################################
prices <- price.delta(st,r,sigma,t,n, epsilon, T)
plot(prices, 
       +      main = 'Random epsilon in normal distribution in each time step',
       +      xlab = 'Step', 
       +      ylab = 'Stock Price', 
       +      xlim = c(0, 100), 
       +      ylim = NULL, 
       +      type='l')

#########################################################
# Step 5
# Perform 5 trials of 100 steps to plot probable 
# movement of stock prices over a 1 year period.
# Plot each trajectory of prices as a separate line
#########################################################

#Trial 1
prices <- price.delta(st,r,sigma,t,n, epsilon, T)
plot(prices, type = 'l',xlab = 'step', ylab = 'Stock Price', main = '5 trials of random epsilon in 1 year', xlim = c(0, 100),ylim = c(-10, 25))

#Trial 2
prices <- price.delta(st,r,sigma,t,n, epsilon, T)
lines(prices, type = 'l', col = 'red')

#Trial 3
prices <- price.delta(st,r,sigma,t,n, epsilon, T)
lines(prices, type = 'l', col = 'green')

#Trial 4
prices <- price.delta(st,r,sigma,t,n, epsilon, T)
lines(prices, type = 'l', col = 'blue')

#Trial 5
prices <- price.delta(st,r,sigma,t,n, epsilon, T)
lines(prices, type = 'l', col = 'orange')

# Answers to the  Questoins
#########################################################
# 1. How wide a variance is noticeable in the final 
# year-end price of the stock for the 5 separate trials 
# performed through steps 4 and 5? 
 Analyze and draw your conclusions.
#
# 
#  The variance is noticeable for the 5 trials, 
# the results suggest that the number of trials were too low, 
# the variance is increasing with time from close 10 at the
# beginning to values above 15 near the 100th step.
# There is results appear almost like a binomial occurrence (i.e., 0 or 1)
# than a normal distribution.Which may be lead to the conclusion that
# the stockreturns do not follow a normal distribution, 
# 

# 
# 
###################################################################################
# 2. Would the variance been higher if ε was assigned 
# purely on a random basis from an arbitrary distribution? 
# 

# Most certainly, the variance would be higher for the stock prices, if an
# arbitrary distribution were used because the epsilon was coming from a
# normal distribution with a variance of 1 and still registered high variances.

 
#################################################################################




