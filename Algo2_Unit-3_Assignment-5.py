# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 20:55:12 2018

@author: Tawanda Vera
"""
from __future__ import (nested_scopes, generators, division, absolute_import,
                        with_statement, print_function, unicode_literals)
#==============================================================================
"""
A company is investing in two securities, x1 and x2.  
The risk management division of the company indicated the following 
constraints to the investment strategy:
Short selling is not allowed
The company must not buy more than 400 units of x1
The total volume must not exceed 800 for every unit of x1 and x2 invested
The total volume must not exceed 1,000 for every 2 units of x1 invested and
 1 unit of x2 invested
The total number of units is maximized considering that, for each 3 units of 
x1 security, 2 units of x2 security must be bought

The company requests the following from you:
Indicate the objective function.
Write the optimization problem.
Find x1 and x2 values that maximize the objective function and 
explain the algorithm.
Use the pulp modeler for Python.
"""
#==============================================================================

# Import PuLP modeler functions
from pulp import *

"""
A variable called prob (although its name is not important) is created 
using the LpProblem function. It has two parameters, 
the first being the arbitrary name of this problem (as a string), and
the second parameter being either LpMinimize or LpMaximize 
depending on the type of LP we are trying to solve:
"""
# Create the 'prob' variable to contain the problem data
prob = LpProblem("Investment Strategy",LpMaximize)

"""
The problem variables x1 and x2 are created using the LpVariable class. 
It has four parameters, the first is the arbitrary name of what this variable 
represents, the second is the lower bound on this variable, the third is 
the upper bound, and the fourth is essentially the type of 
data (discrete or continuous). The options for the fourth parameter are 
LpContinuous or LpInteger, with the default as LpContinuous.
The bounds can be entered directly as a number, or None to represent 
no bound (i.e. positive or negative infinity), with None as the default. 
If the first few parameters are entered and the rest are ignored (as shown),
 they take their default values. 
However, if you wish to specify the third parameter, but you want the 
second to be the default value, you will need to specifically set the 
 second parameter as it’s default value. i.e you cannot leave a 
 parameter entry blank. e.g:
"""

# The 2 variables stock 1 and stock 2 are created with a lower limit of zero 

x1=LpVariable("Stock1units",0,None,LpInteger)  
x2=LpVariable("Stock2units",0)

# The objective function is added to 'prob' first
"""The variable 'prob' now begins collecting problem data with the += operator.
 The objective function is logically entered first, with an important comma, 
 at the end of the statement and a short string explaining what this 
 objective function is:
"""
prob += 3*x1 + 2*x2, "The total number of units maximized"

# The five constraints are entered
"""The constraints are now entered
(Note: any “non-negative” constraints were already included when defining 
the variables). This was done with the ‘+=’ operator, since we are adding
more data to the prob variable. The constraints are logically entered after 
this, with a comma at the end of the constraint equation and a brief 
description of the cause of that constraint:
"""

prob += x1 >= 0, "No Short Selling allowed for x1"
prob += x2 >= 0, "No Short Selling allowed for x2"
prob += x2 <= 400, "Must not buy more than 400 units of x1"
prob += x1 + x2 <= 800, "Total volume must not exceed 800 for x1 + x2"
prob += 2*x1 + x2 <= 1000, "Total volume must not exceed 1,000 for 2x1 + x2"


# The problem data is written to an .lp file
"""Now that all the problem data is entered, the writeLP() function can be 
used to copy this information into a .lp file into the directory that our
 code-block is running from. Once the your code runs successfully, 
 we can open this .lp file with a text editor to see what the above steps
 were doing. 
"""
prob.writeLP("InvestStrategy.lp")  

# You will notice that there is no assignment operator (such as an equals sign)  
"""This is because the function/method called writeLP() is being performed to 
the variable/object prob (and the string "InvestStrategy.lp" is an additional
 parameter). The dot . between the variable/object and the function/method is
 important and is seen frequently in Object Oriented software like Python:
"""

# The problem is solved using PuLP's choice of Solver
"""The LP is solved using the solver that PuLP chooses. 
The input brackets after solve() are left empty in this case, however 
they can be used to specify which solver to use (e.g prob.solve(CPLEX()) )
"""
prob.solve()

# The status of the solution is printed to the screen
"""Now the results of the solver call can be displayed as output to us.
Firstly, we request the status of the solution, which can be one of 
“Not Solved”, “Infeasible”, “Unbounded”, “Undefined” or “Optimal”. 
The value of prob (pulp.pulp.LpProblem.status) is returned as an integer, 
which must be converted to its significant text meaning using the 
LpStatus dictionary. Since LpStatus is a dictionary(dict), its input must
be in square brackets:
"""
print ("Status:", LpStatus[prob.status])

# Each of the variables is printed with it's resolved optimum value
"""The for loop makes variable cycle through all the problem variable names
 (in this case just stock1units and stock2units). 
 Then it prints each variable name, followed by an equals sign, followed by
 its optimum value. name and varValue are properties of the object variable.
"""
for v in prob.variables():
    print (v.name, "=", v.varValue)


# The optimised objective function value is printed to the screen
"""The optimised objective function value is printed to the screen, using 
the value function. This ensures that the number is in the right format to
be displayed. objective is an attribute of the object prob
"""   
print ("The total number of units maximized = ", value(prob.objective))
# Running this file should then produce the output to show that: 
# x1 value of 300, x2 value of 400 maximizes the objective function giving the
# number of units maximized of  1700. 
#=============================================================================

# Algorithm
"""\* Investment Strategy *\
Maximize
The_total_number_of_units_maximized: 3 Stock1units + 2 Stock2units
Subject To
Must_not_buy_more_than_400_units_of_x1: Stock2units <= 400
No_Short_Selling_allowed_for_x1: Stock1units >= 0
No_Short_Selling_allowed_for_x2: Stock2units >= 0
Total_volume_must_not_exceed_1,000_for_2x1___x2: 2 Stock1units + Stock2units
 <= 1000
Total_volume_must_not_exceed_800_for_x1___x2: Stock1units + Stock2units <= 800
Bounds
0 <= Stock1units
Generals
Stock1units
End
"""
#==============================================================================

#Application in Quantitative Finance
"""Linear programming algorithm find application in alpha generating models 
through portfolio optimization. Where, alpha generating strategies that are 
aimed at minimizing risk and / or maximizing return.
 A good example of linear programming algorithm is the mean-variance model 
 of Markowitz. Where, the linear programming algorithm is used to determine
 the number of shares in a market index to be selected along with the number 
 of small market orders that need to be purchased from each of these stocks
 so that portfolio has the least risk. From this, a strategy can be developed
 to generate the most return subject to constraints like short-selling 
 constraints.
 """
 #=============================================================================