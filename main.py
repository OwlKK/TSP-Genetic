from city_list_generator import readData
from create_genetic_algorithm import geneticAlgorithm
from plotting import plotting

if __name__ == '__main__':
    cities = readData()

    # this works - returns a list of objects
    # print(create_initial_population.createRoute(cities))
    # print(len(create_initial_population.createRoute(cities)))

    geneticAlgorithm(population=cities, populationSize=100, eliteSize=20, mutationRate=0.01, generations=100)

    # plotting(population=cities, populationSize=100,
    #         eliteSize=20, mutationRate=0.01, generations=100)
