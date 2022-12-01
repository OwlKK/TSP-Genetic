import matplotlib.pyplot as plt


# this wont work form now XD
def print_path(bestRoute, cityList):
    points = cityList[bestRoute]
    x, y = zip(*points)
    plt.plot(x, y, color="skyblue", marker="o")
