# Fitness is the LITERAL inverse of distance function
class Fitness:
    def __init__(self, route):
        # same shit
        # route = create_initial_population.createRoute(cities=city_list_generator.readData())
        self.route = route
        self.distance = 0
        self.fitness = 0.0

    def routeDistance(self):
        # print(len(self.route)) - works here - is 11
        # print(self.distance) - works here - is 0
        if self.distance == 0:
            pathDistance = 0
            # print len of route - is 11
            # print(len(self.route))

            for i in range(0, len(self.route)):
                # self.route[i] - works - gets a city from route at position
                fromCity = self.route[i]
                toCity = None

                # if not last city
                if i + 1 < len(self.route):
                    toCity = self.route[i + 1]

                # if last city
                else:
                    toCity = self.route[0]
                pathDistance += fromCity.distance(toCity)
            self.distance = pathDistance
        return self.distance

    def routeFitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.routeDistance())
        return self.fitness
