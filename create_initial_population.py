import random


# random.sample(sequence, k)
# Returns a k length list of unique elements chosen from the population sequence.
# Used for random sampling without replacement.
def createRoute(cities):
    # route has len of 11 when given "Berlin 11" file - as expected
    # print(str(len(route)) + "test route length")
    route = random.sample(cities, len(cities))
    return route


def createFirstPopulation(populationSize, cities):
    population = []

    for i in range(0, populationSize):
        population.append(createRoute(cities))
    return population
