# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 20:55:23 2017

@author: TempAdmin1
"""
import datetime as dt # Datetime functions
import quandl         # Type "conda install -c anaconda quandl" to download
import random         # Ranom library for generation population
import math           # Math library
import numpy as np
from operator import add


###################################################################
# Function is get_data(symbol, from_date, to_date, field)
#
#  Inputs:
#    symbol = stock symbol to retrieve (default is WIKI/TLSA)
#    start = start date (default is 5 years ago or 8 Oct 2013)
#    end = end date (default should be today or 8 Oct 2017)
#    field = information to retrieve (default is adjusted closing price)
#
#  Output:
#    Requested data - Closing price the dates for the specific stock
#
# NOTE: Quandl must be loaded into Anaconda to retrive data 
#       Also, you will need your FREE user account authentication token
#       after 50 downloads.   Hence, create a FREE account.
##################################################################
def get_data(symbol="WIKI/TSLA", start="2013-10-23", end="2017-10-23", field="Adj. Close"):
        
#    alldata = quandl.get(symbol)    # 50 free anonymous calls allowed per day
    alldata = quandl.get(symbol, authtoken='MgUeDFrhs9JjaA4gKzEx' )    # Must use your own authentication token thereafer
    mydata = alldata.loc[start:end,field]
    
# API call is Quandl.get(symbol, authtoken)

    return(mydata)

##################################################################
# Step 1 - Initialize the population with a random set of C
#
# Function is generate_individual(min_price, max_price, n_tuples)
#
#  Inputs:
#     min_price = lowest price condition
#     max_price = higher price condition
#     n_tuples = number of tuples (10 or fewer)
#
#   Output:
#     C = random set of indiviudals 
#
##################################################################
def generate_individual(min_price = 141, max_price = 390, n_tuples = 5):
        
    # Return if invalid parameters passed in
    if (max_price <= min_price) or (n_tuples < 2) or (n_tuples > 10):
        print("Invalid parameters (min_price = %d, max_price=%d, n_tuples = %d" % (min_price, max_price, n_tuples))
        return
    
    # Compute the increment (or range) of prices
    inc = int(round((max_price - min_price) / (n_tuples + 1)))
    
    # Assign the initial price range between start and next
    start_price = min_price
    next_price = min_price + inc
    
    # Randomaly assign first conditional prices
    a = random.randint(start_price, next_price)
    b = random.randint(next_price+1, next_price+(2*inc))
        
    # Check how many tuples requested
    if n_tuples == 2: # Only 2 so done
        individuals = (a, b)
    elif n_tuples == 3: # 3, so compute third conditional price
        c = random.randint(next_price+(2*inc)+1, max_price)
        individuals = (a, b, c)
    elif n_tuples == 4: # 4, so compute all four conditional prices
        c = random.randint(next_price+(2*inc)+1, next_price+(3*inc))
        d = random.randint(next_price+(3*inc)+1, max_price)
        individuals = (a, b, c, d)
    elif n_tuples == 5: # 5, so compute all five conditional prices
        c = random.randint(next_price+(2*inc)+1, next_price+(3*inc))
        d = random.randint(next_price+(3*inc)+1, next_price+(4*inc))
        e = random.randint(next_price+(4*inc)+1, max_price)
        individuals = (a, b, c, d, e)
    elif n_tuples == 6: # 6 so compute all six conditional prices
        c = random.randint(next_price+(2*inc)+1, next_price+(3*inc))
        d = random.randint(next_price+(3*inc)+1, next_price+(4*inc))
        e = random.randint(next_price+(4*inc)+1, next_price+(5*inc))
        f = random.randint(next_price+(5*inc)+1, max_price)
        individuals = (a, b, c, d, e, f)
    elif n_tuples == 7: # 7 so compute all six conditional prices
        c = random.randint(next_price+(2*inc)+1, next_price+(3*inc))
        d = random.randint(next_price+(3*inc)+1, next_price+(4*inc))
        e = random.randint(next_price+(4*inc)+1, next_price+(5*inc))
        f = random.randint(next_price+(5*inc)+1, next_price+(6*inc))
        g = random.randint(next_price+(6*inc)+1, max_price)
        individuals = (a, b, c, d, e, f, g)
    elif n_tuples == 8: # 8 so compute all six conditional prices
        c = random.randint(next_price+(2*inc)+1, next_price+(3*inc))
        d = random.randint(next_price+(3*inc)+1, next_price+(4*inc))
        e = random.randint(next_price+(4*inc)+1, next_price+(5*inc))
        f = random.randint(next_price+(5*inc)+1, next_price+(6*inc))
        g = random.randint(next_price+(6*inc)+1, next_price+(7*inc))
        h = random.randint(next_price+(7*inc)+1, max_price)
        individuals = (a, b, c, d, e, f, g, h)
    elif n_tuples == 9: # 9 so compute all six conditional prices
        c = random.randint(next_price+(2*inc)+1, next_price+(3*inc))
        d = random.randint(next_price+(3*inc)+1, next_price+(4*inc))
        e = random.randint(next_price+(4*inc)+1, next_price+(5*inc))
        f = random.randint(next_price+(5*inc)+1, next_price+(6*inc))
        g = random.randint(next_price+(6*inc)+1, next_price+(7*inc))
        h = random.randint(next_price+(7*inc)+1, next_price+(8*inc))
        i = random.randint(next_price+(8*inc)+1, max_price)
        individuals = (a, b, c, d, e, f, g, h, i)
    else: # 10 (or more), so compute 10 conditinal prices
        c = random.randint(next_price+(2*inc)+1, next_price+(3*inc))
        d = random.randint(next_price+(3*inc)+1, next_price+(4*inc))
        e = random.randint(next_price+(4*inc)+1, next_price+(5*inc))
        f = random.randint(next_price+(5*inc)+1, next_price+(6*inc))
        g = random.randint(next_price+(6*inc)+1, next_price+(7*inc))
        h = random.randint(next_price+(7*inc)+1, next_price+(8*inc))
        i = random.randint(next_price+(8*inc)+1, next_price+(9*inc))
        j = random.randint(next_price+(9*inc)+1, max_price)
        individuals = (a, b, c, d, e, f, g, h, i, j)
        
    # Return set of individual conditional prices
    return individuals

##################################################################
# Fuction is condition_satisfied
#
#   Inputs:
#     a = current index of allele
#     allele = individual set of conditions
#     s = current index of stock data
#     stock = time series data of stock prices
#     n_tuples = how many conditions per tuples stock prices are to satisfy
#
#   Output:
#     True - if condition met
#     False - otherwise
#
# These can be ANY conditions or rules you choose to define
##################################################################
def condition_satisfied(a, allele, s, stock, n_tuples): 
    
    # The is ONLY valild for allels of 3, 4, 5, and 6.  
    
    if n_tuples == 3:
        # Three conditions C1, C2, C3 such that C1 <= P1 < C2 <= P2 < C3
        if stock[s-1] >= allele[a][0] and \
           stock[s]   >= allele[a][1] and \
           stock[s+1] <= allele[a][2]:
              return True
         
    if n_tuples == 4:
         # Four conditions C1, C2, C3, C4 such that C1 >= P1 < C2 <= P2 < C3 <= P3 <= C4
        if (stock[s-1] >= allele[a][0]  or stock[s] >= allele[a][1]) and \
           (stock[s]   >= allele[a][1]  or stock[s+1] <= allele[a][3]):
              return True
          
    if n_tuples == 5:
         # Five conditions C1, C2, C3, C4, C5 such that P1 >= C1, P2 >= C2 or <= C3, and P3 >= C4 or <= C5
        if stock[s-1] >= allele[a][0] and \
          (stock[s]   >= allele[a][1] or stock[s]   <= allele[a][2]) and \
          (stock[s+1] >= allele[a][3] or stock[s+1] <= allele[a][4]):
              return True
 
    if n_tuples == 6:
         # Six conditions C1, C2, C3, C4, C5, C6 such that P1 >= C1, P2 >= C2 or <= C3, and P3 >= C4 or <= C5
        if(stock[s-1] >= allele[a][0] and stock[s-1] < allele[a][1]) and \
          (stock[s]   >= allele[a][1] and stock[s]   < allele[a][2]) and \
          (stock[s+1] >= allele[a][2] and stock[s+1] < allele[a][3]) and \
          (stock[s+2] >= allele[a][3] and stock[s+2] < allele[a][4]) and \
          (stock[s+3] >= allele[a][4] and stock[s+3] <= allele[a][5]):
              return True
    # if n_tuples == 7:
    # if n_tuples == 8:
    # if n_tuples == 9:
    # if n_tuples == 10:

    
##################################################################
# Step 1 - Initialize the population with a random set of C
#
# Function is generate_population(size, min_price, max_price, n_tuples)
#
#  Inputs:
#     size = the population size to generate, default is 100
#     min_price = lowest price condition, default is 141 (Telsa price)
#     max_price = higher price condition, default is 390 (Telsa price)
#     n_tuples = number of tuples (5 or fewer)
#
#   Output:
#     C = random set of indiviudals in the population
#
##################################################################
def generate_population(size = 100, min_price = 141, max_price = 390, n_tuples = 5):

    C = []
    
    # Loop to create entire population of C's
    for i in range(0, size):
        
        # Append individual conditions
        C.append(generate_individual(min_price, max_price, n_tuples)) 
    
    # Return the random set of conditions in entire population
    return C


##########################################################################
# collect stock Y-values that pass the series of conditions

def findYs(individuals, timeSeries, n_tuples = 5):
    myList = []
    myDict = {}
    
    # Look at each individual C in the population and see if a fix exists
    for y in range(len(individuals)):
        # Examine the adjusted closing price to see if condition hold for the Y-values
        for x in range(1, len(timeSeries) - 1):

             if condition_satisfied(y, individuals, x, timeSeries, n_tuples):
                 myList.append(timeSeries[x])
                 myDict[individuals[y]] = myList
        
        # Reset list for next individual condition C
        myList = []
        
    # Return all conditions subsequent Y-values which have been satisfied
    return myDict
##########################################################################

##########################################################################
def popfitness(population, Yvals, std, std_o):
    """Determine the fitness of every individual in the population."""
    popfit=[]
    for i in range(0,len(population)):
        popfit.append(fitness(population[i], Yvals, std, std_o))
    return popfit

##########################################################################
#      Fitness Function:
#        f(C) = -log2(std/std_o) - alpha/N_c
#        where:
#        std: standard deviation of the x set that satisfy condition C
#        std_o: the standard deviation of the distribution of x over the entire dataset
#        N_c: the number of data points satisfying condition C
#        alpha: Constant       
##########################################################################
def fitness(individual, Yvals, std, std_o, alpha = 1):

    myFitness = []
      
    if len(Yvals) > 1:
        myFitness.append(-math.log(std/std_o - (alpha/len(Yvals)))) #Fitness function 
    else:
        myFitness.append(0)
    return myFitness

##########################################################################
# Main program -- load data, generate chromosones, and test fitness
#
# This implements the Meyer Packard Genetic Algorithm in 6 steps:
#   1 - Initialize the population with a random set of C
#   2 - Calculate the fitness of each C
#   3 - Rank the population by fitness
#   4 - Discard lower-fitness individuals and replace with new Cs obtained by 
#       applying crossover and mutation to the remaining Cs
#   5 - Repeat from step 2
#   6 - Once highest fit C's obtained - predict next 24 months of stock prices
#   7 - Improve the algorithms to get better predication's
#
# This is SAMPLE or STARTER code only.  There are many ways to approach
# this problem.  Be creative.  Only Steps 1 and 2 above have been coded.
# Also, the code has not been fully tested -- so use with care and modify as needed
##########################################################################


quandl_symbol = "WIKI/TSLA"         # Replace "AAL" with any stock, "TSLA" is the default
mydata = get_data(quandl_symbol)   # Load time series data from Quandl

# Use the minimum and maximum prices as the low and high prices (but these can be set to different values)  
lowest_price = int(min(mydata))         # Lowest price to test price conditions
highest_price = int(max(mydata))       # Highest price to test price conditions

#lowest_price = 120        # Lowest price to test price conditions
#highest_price = 385       # Highest price to test price conditions

# Set the number of C's the series must satisfy and how many to generate in the population
number_of_tuples = 5       # Number of condition tuples to generate for individuals (2 to 10), default is 5
number_of_individuals = 4  # Number of individuals to generate for entire population, default is 100

################################################################
# 1 - Generate the population of random individuals of C
################################################################
individuals = generate_population(number_of_individuals, lowest_price, highest_price, number_of_tuples)
print("**********************************************************")
print("Step 1: The randomly generated population of C's are:")
print("**********************************************************")
print(individuals)

################################################################
# 2 - Compute the fitness of each C
################################################################

# Find those Y-valus which match the conditions C
Yvals = findYs(individuals, mydata, number_of_tuples)

# Display fitness values of satisfied conditions C
print("**********************************************************")
print("Step 2: Fitness Values")
print("**********************************************************")
std_o = np.std(mydata)
popfit = []
i = 0
for k in Yvals.keys():
    popfit = popfitness(individuals, Yvals, np.std(Yvals[k]), std_o)
    print("For the Condition")
    print(k)
    print("fitness value = %s" % popfit[++i][0])

################################################################
# 3 - Rank Fitness by Population
################################################################
def part():
    options = ('+','-','*','/')
    options += tuple( "%d" % x for x in range(0,10))
    return options[random.randint(0, len(options)-1)]

def generation(pop, target, retain=0.3, random_select=0.05, mutate=0.01):
      popfit = [popfitness(individuals, Yvals, np.std(Yvals[k]), std_o) for k in Yvals.keys]
      popfit = [ k[0] for k in sorted( popfit, reverse=True) ]
      retain_length = int(len(popfit)*retain)
      parents = popfit[:retain_length] 
      for individuals in popfit[:retain_length]:
        if random() > random_select:
            parents.append(individuals)
      for individual in parents:
          if random() > mutate:
              pos_to_mutate = random.randint(0, len(individual)-1)
              individual[pos_to_mutate] = part()
              parents_length = len(parents)
              desired_length = len(individuals) - parents_length
              children = []
      while len(children) < desired_length:
           male = random.randint(0, parents_length-1)
           female = random.randint(0, parents_length-1)
      if male != female:
            male = parents[male]
            female = parents[female]
            half = len(male) / 2
            child = male[:half] + female[half:]
            children.append(child)
            parents.extend(children)
      return parents

################################################################
# 4 - Discard and replace C's using select, mutate, and crossover operations
################################################################
#Import Library
from sklearn.ensemble import RandomForestClassifier #use RandomForestRegressor for regression problem
#Assumed you have, X (predictor) and Y (target) for training data set and x_test(predictor) of test_dataset
# Create Random Forest object
model= RandomForestClassifier(n_estimators=1000)
# Train the model using the training sets and check score
model.fit(individuals, Yvals)
#Predict Output
predicted= model.predict(individuals_test)

import csv
import sys
writer = csv.writer(sys.stdout)
writer.writerows(predicted)


import GeneticAlgo as ga

ga.GeneticAlgorithm(individuals, Yvals)

























              