from city_list_generator import readData
from create_genetic_algorithm import geneticAlgorithm
from plotting import plotting
from show_final_path import print_path

if __name__ == '__main__':
    cityList = readData()
    bestRoute = geneticAlgorithm(population=cityList, populationSize=100,
                                 eliteSize=20, mutationRate=0.01, generations=100)

    print(bestRoute)

    plotting(population=cityList, populationSize=100,
             eliteSize=20, mutationRate=0.01, generations=100)
