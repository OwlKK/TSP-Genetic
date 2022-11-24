import numpy as np
import operator
import pandas as pd
import random

from create_initial_population import createFirstPopulation
from fitness import Fitness


def rankRoutes(population):
    # dictionary
    fitnessResults = {}
    for i in range(0, len(population)):
        fitnessResults[i] = Fitness(population[i]).routeFitness()

        # .items() returns dictionary's (element/info) of object - here a whole object from dictionary
        # SORTS THE LIST-LIKE OBJECT ACCORDING TO ROUTE LENGTH
    return sorted(fitnessResults.items(), key=operator.itemgetter(1), reverse=True)


# fitness weighted probability of selecting
# pd.dataframe() - matrix with row/column header

# df => data frame
# Selecting parents from matingpool to be used in creating new generation
# returns a list of ID used in matingPool function
def selection(populationRanked, eliteSize):
    selectionResults = []
    df = pd.DataFrame(np.array(populationRanked), columns=["Index", "Fitness"])

    # .cumsum - returns consecutive sum of elements
    # for np.cumsum(np.array([1, 2, 3, 4, 5, 6])) returns array([1, 3, 6, 10, 15, 21])

    # declaring lists as new columns
    df['cumulative_sum'] = df.Fitness.cumsum()
    df['cumulative_percentage'] = 100 * df.cumulative_sum / df.Fitness.sum()

    # add elite to selectionResults
    for i in range(0, eliteSize):
        selectionResults.append(populationRanked[i][0])

    # add
    # DataFrame.iat -> Access a single value for a row/column pair by integer position.
    for i in range(0, len(populationRanked) - eliteSize):
        # 0 < number < 100
        pick = 100 * random.random()
        for i in range(0, len(populationRanked)):
            if pick < df.iat[i, 3]:
                selectionResults.append(populationRanked[i][0])
                break
    return selectionResults


def matingPool(population, selectionResults):
    mating_pool = []
    for i in range(0, len(selectionResults)):
        index = selectionResults[i]
        mating_pool.append(population[index])
    return mating_pool


def breed(parent1, parent2):
    # -Gene in this context is position of city (the smallest possible change to "object")

    # "Ordered crossover" -  consecutive alleles from parent 1 drops down, and remaining values are placed in the child
    # in the order which they appear in parent 2

    childPart1 = []  # I only need half of the child, rest is created dynamically

    # position of city in list
    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))

    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene, endGene):
        childPart1.append(parent1[i])

    childPart2 = [item for item in parent2 if item not in childPart1]

    child = childPart1 + childPart2
    return child


def breedPopulation(mating_pool, eliteSize):
    children = []
    leftLength = len(mating_pool) - eliteSize
    pool = random.sample(mating_pool, len(mating_pool))

    # adding elite to bred population
    for i in range(0, eliteSize):
        children.append(mating_pool[i])

    # breed - make one child from 2 parents
    # mating_pool - bred population + elite (in that order)
    # pool - reorganized matingpool

    for i in range(0, leftLength):
        child = breed(pool[i], pool[len(mating_pool) - i - 1])
        children.append(child)
    return children


# mutates individual
def mutate(individual, mutationRate):
    for swapped in range(len(individual)):
        if random.random() < mutationRate:
            swapWith = int(random.random() * len(individual))

            city1 = individual[swapped]
            city2 = individual[swapWith]

            individual[swapped] = city2
            individual[swapWith] = city1

    return individual


# mutates every individual in population and adds to list
def mutatePopulation(population, mutationRate):
    mutatedPopulation = []

    for ind in range(0, len(population)):
        mutatedInd = mutate(population[ind], mutationRate)
        mutatedPopulation.append(mutatedInd)

    return mutatedPopulation


def nextGeneration(currentGen, eliteSize, mutationRate):
    populationRanked = rankRoutes(currentGen)
    selectionResults = selection(populationRanked, eliteSize)
    mating_pool = matingPool(currentGen, selectionResults)
    children = breedPopulation(mating_pool, eliteSize)
    nextGeneration = mutatePopulation(children, mutationRate)
    return nextGeneration


def geneticAlgorithm(population, populationSize, eliteSize, mutationRate, generations):
    pop = createFirstPopulation(populationSize, population)
    print("Initial distance: " + str(1 / rankRoutes(pop)[0][1]))

    for i in range(0, generations):
        pop = nextGeneration(population, eliteSize, mutationRate)

    print("Final distance: " + str(1 / rankRoutes(pop)[0][1]))
    bestRouteIndex = rankRoutes(pop)[0][0]
    bestRoute = pop[bestRouteIndex]
    print("Route: " + str(bestRoute))
    return bestRoute
