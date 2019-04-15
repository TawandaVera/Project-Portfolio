# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 19:00:13 2018

@author: Tawanda Vera
"""
from __future__ import (nested_scopes, generators, division, absolute_import,
                        with_statement, print_function, unicode_literals)

#==============================================================================
"""Problem 1: 
Write the LP relaxation (P1) of (IP) and explain why the objective value of 
an optimal solution to (P1) is an upper bound on the value of an optimal 
solution to (IP).

The LP relaxation is obtained by dropping the integrality constraint:
maximize 3x1 − x2 + 2x3 
subject to x1 − x2 + x3 ≤ 5 
2x2 + x3 ≤ 4 
x1 ≤ 3 
x1,x2,x3 ≥ 0
"""
#==============================================================================
# Import PuLP modeler functions
from pulp import *

"""
A variable called prob_1 is created using the LpProblem function. 
It has two parameters, the first being the arbitrary name of this problem 
(as a string), and the second parameter being either LpMinimize or LpMaximize 
depending on the type of LP we are trying to solve:
"""
# Create the 'prob' variable to contain the problem data

prob_1 = LpProblem("LP Relaxation", LpMaximize)

# # The 3 variables stock 1 and stock 2 are created with a lower limit of zero 
"""x1,x2,x3 ≥ 0
The problem variables x1,x2 and x3 are created using the LpVariable class
The LP obtained by omitting all integer or 0-1 constraints on variables is
 called the LP relaxation of the IP.
"""
x1 = LpVariable("x1",0)  
x2 = LpVariable("x2",0)
x3 = LpVariable("x3", 0)

# The formulation of the objective function
"""The variable 'prob' now begins collecting problem data with the += operator.
 The objective function is logically entered first, with an important comma, 
 at the end of the statement and a short string explaining what this 
 objective function is:
"""

prob_1 += 3*x1 - x2 + 2*x3, "The objective function, LP relaxation (P1)" 

# Specify the constraints
"""The constraints are now entered
(Note: any “non-negative” constraints were already included when defining 
the variables). This was done with the ‘+=’ operator, since we are adding
more data to the prob variable. The constraints are logically entered after 
this, with a comma at the end of the constraint equation and a brief 
description of the cause of that constraint:
"""

prob_1 += x1 - x2 + x3 <= 5, "The first constraint" 
prob_1 += 2*x2 + x3 <= 4, "The second constraint"
prob_1 += x1 <= 3, "The decision variable constraint" 

# The problem data is written to an .lp file
"""Now that all the problem data is entered, the writeLP() function can be 
used to copy this information into a .lp file into the directory that our
 code-block is running from. Once the your code runs successfully, 
 we can open this .lp file with a text editor to see what the above steps
 were doing. 
"""

prob_1.writeLP("lpRelaxation.lp")  

# The problem is solved using PuLP's choice of Solver
"""The LP is solved using the solver that PuLP chooses. 
The input brackets after solve() are left empty in this case, however 
they can be used to specify which solver to use (e.g prob.solve(CPLEX()) )
"""

prob_1.solve()

# The status of the solution is printed to the screen
"""Now the results of the solver call can be displayed as output to us.
Firstly, we request the status of the solution, which can be one of 
“Not Solved”, “Infeasible”, “Unbounded”, “Undefined” or “Optimal”. 
The value of prob (pulp.pulp.LpProblem.status) is returned as an integer, 
which must be converted to its significant text meaning using the 
LpStatus dictionary. Since LpStatus is a dictionary(dict), its input must
be in square brackets:
"""

print ("Status:", LpStatus[prob_1.status])

# Each of the variables is printed with it's resolved optimum value
"""The for loop makes variable cycle through all the problem variable names.
 Then it prints each variable name, followed by an equals sign, followed by
 its optimum value. name and varValue are properties of the object variable.
"""

for v in prob_1.variables():
    print (v.name, "=", v.varValue)

# The optimised objective function value is printed to the screen
"""The optimised objective function value is printed to the screen, using 
the value function. This ensures that the number is in the right format to
be displayed. objective is an attribute of the object prob
"""   

print ("The value of an optimal solution to IP = ", value(prob_1.objective))

#==============================================================================
# Comments
"""
The LP relaxation is obtained by dropping the integrality constraint on x1, x2,
and x3:

Maximize
The_objective_function,_LP_relaxation_(P1): 3 x1 - x2 + 2 x3
Subject To
The_decision_variable_constraint: x1 <= 3
The_first_constraint: x1 - x2 + x3 <= 5
The_second_constraint: 2 x2 + x3 <= 4

As this increases the region of feasible solutions and since we are dealing 
with a maximization problem, the value of an optimal solution to (P1) is an 
upper bound on the value of an optimal solution to (IP).

Status: Optimal
x1 = 3.0
x2 = 0.67
x3 = 2.67
The value of an optimal solution to (IP) =  13.67
"""
#==============================================================================
#Application in Quant Finance
"""Any Integrated Programming (IP) may be viewed as the Linear Programming (LP)
 relaxation plus additional constraints. This means that the feasible region
 for any IP must be contained in the feasible region for the corresponding LP 
 relaxation. For any IP that is a max problem, this implies that Optimal 
 z-value for LP relaxation is an optimal z-value for IP. As such, IP algorithms
 can be used get the same results we get from LP relaxation with additional 
 constraints. This is a particularly important concept being used in alpha 
 modelling platforms like websim, were the None or unconstrained option is part 
 and parcel of the modelling strategies. The stepwise removal of constraints on
 these platforms is important for exploring different option, combinations and
 strategies neccessary for alpha generating models.
 """
#==============================================================================