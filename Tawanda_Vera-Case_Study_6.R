
# Performance Analytics is required because of the return.calculate command that 
#calculates the daily returns of x.DJ

require(PerformanceAnalytics)

returns <- na.omit(Return.calculate(x.DJ, method = 'discrete'))


print(returns)

##############################################################################################
#Regression Coefficients
########################################################################################

returns.lm <- lm(returns[-1]~returns[-2])


#####    RESIDUALS SUMMARY   ###################
summary (returns.lm$residuals)

#####    FITTED VALUES SUMMARY    ###################

summary (returns.lm$fitted.values)

#####   ALPHA SUMMARY     ###################
summary (returns.lm$qr$qr)


barplot(returns.lm$qr$qr, main="Distribution of Alpha")


#####   BETA SUMMARY   ###################

summary (returns.lm$coefficients)


hist(returns.lm$coefficients, breaks=20, main="Distribution of Beta")
