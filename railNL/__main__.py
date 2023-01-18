from classes.railNetwork import RailNetwork
from visualize.visualize import visualize
from os import path

BATCH = False

if path.exists("railNL/algorithms/random_hajo.py"):
    from algorithms import random_hajo

    BATCH = True

def main():
    network = RailNetwork("data/StationsHolland.csv", "data/ConnectiesHolland.csv")
    
    if BATCH:
        random_hajo.main(network, 7, 120)
        return
    
    network.createRoute(network.getStation("Den Helder"))
    route = network.getRoute(0)
    route.appendStation(network.getStation("Alkmaar"))
    route.appendStation(network.getStation("Castricum"))

    visualize(network.connectionPoints(), network.stationPoints(), network.routePointLists())

    network.exportSolution("results", "Nederland")

if __name__ == "__main__":
    main()