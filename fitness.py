# Fitness is the LITERAL inverse of distance function
class Fitness:
    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.fitness = 0.0

    def routeDistance(self):
        # for testing

        # prints [cityZ_(x,y), (x,y) ...] 11 times for 11 cities
        # print(self.route)
        if self.distance == 0:
            pathDistance = 0
            for i in range(0, len(self.route)):
                # same as higher
                # print(self.route)

                # self.route is a list
                # print(type(self.route))
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
