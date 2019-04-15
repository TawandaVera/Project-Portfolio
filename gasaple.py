# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 16:21:12 2017

@author: TempAdmin1
"""

from random import randint, random

def part():
    options = ('+','-','*','/')
    options += tuple( "%d" % x for x in range(0,10))
    return options[randint(0, len(options)-1)]

def individual(length=5):
    return [ part() for i in range(length) ]

def population(size=1000, length=5):
    return [ individual(length=length) for x in range(size) ]

def fitness(x, target):
    try:
        val = eval(" ".join(x))
        return target - abs(target-val)
    except:
        return -100000

#rank pop fitness
def grade_population(pop, target):
    pop_fitness = [ fitness(x, target) for x in pop ]
    valid_syntax = [ x for x in pop_fitness if x > -100000 ]
    valid_count = len(valid_syntax)
    return valid_count

# generate ranked pop fitness
def generation(pop, target, retain=0.3, random_select=0.05, mutate=0.01):
    graded = [ (fitness(x, target), x) for x in pop ]
    graded = [ x[1] for x in sorted(graded, reverse=True) ]
    retain_length = int(len(graded)*retain)
    parents = graded[:retain_length]
# randomly add other individuals to
# promote genetic diversity
for individual in graded[retain_length:]:
    if random() > random_select:
        parents.append(individual)
# mutate some individuals
for individual in parents:
    if random() > mutate:
        pos_to_mutate = randint(0, len(individual)-1)
# this mutation is not ideal, because it
# restricts the range of possible values,
# but the function is unaware of the min/max
# values used to create the individuals,
        individual[pos_to_mutate] = part()
# crossover parents to create children
        parents_length = len(parents)
        desired_length = len(pop) - parents_length
        children = []
        while len(children) < desired_length:
            male = randint(0, parents_length-1)
            female = randint(0, parents_length-1)
            if male != female:
    male = parents[male]
    female = parents[female]
    half = len(male) / 2
    child = male[:half] + female[half:]
    children.append(child)
    parents.extend(children)
    return parents

def evolve(pop_size=1000, target=15, individ_size=5, retain=0.3,
generations=1000, random_select=0.05, mutate=0.01):
    p = population(size=pop_size, length=individ_size)
    history = [ p, ]
    fit_history = [ grade_population(p, target=target) ]

for i in range(generations):
    p = generation(p, target, retain, random_select, mutate)
    history.append(p)
    fit_history.append(grade_population(p, target=target))
return history, fit_history