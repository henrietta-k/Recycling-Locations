"""
Creating the graph of recycling stations in Hong Kong and implementing
a BFS algorithm to create a list of stations from closest to farthest from the
starting point
"""

from station import*
from info import*
import PySimpleGUI as py

def create_graph():
    """
    Making a graph determined by MTR lines. Keys are location names and values
    are the respective Station objects

    Returns (dictionary): graph of locations
    """

    result = {}

    for line in all_lines:
        for _, stop in enumerate(line):
            result[stop] = Station(stop)
            result[stop].add_neighbors(line)

    for neigh_pairs in neighboring_lines:
        result[neigh_pairs[0]].add_neighbor(neigh_pairs[1])
        result[neigh_pairs[1]].add_neighbor(neigh_pairs[0])

    for station in all_stations:
        result[station].add_operator(operators[station])
        result[station].add_address(addresses[station])

    return result


def bfs_start(start):
    """
    Starts a BFS algorithm to a list of the closest to farthest

    Input:
        start(str): name of location to start at

    Returns(list): list of locations from closest to the start to farthest
    """

    explored = []
    queue = []

    explored.append(start)
    queue.append(start)

    return bfs(create_graph(), explored, queue)


def bfs(graph, explored, queue):
    """
    Inputs:
        graph(dict): the graph of Station locations
        visited(lst): the names of the visited locations
        queue(lst): queue of locations to visit
        start(Str): the name of the location to start at

    Returns(list): list of locations visited
    """

    while len(queue) > 0:
        current = queue.pop(0)
        for neighbor in graph[current].neighbors:
            if neighbor not in explored:
                explored.append(neighbor)
                queue.append(neighbor)

    explored.pop(0)
    return explored


def to_string():
    """
    Turns the list into a string format that tells you which stops are closest
    and which ones are farthest

    Returns (str): str representation of the cloest locations
    """

    loc_lst = bfs_start(start)
    current_line = None
    for line in all_lines:
        if start in line:
            current_line = line

    for loc in loc_lst:
        if loc in current_line:
            print("Same MTR line: {}".format(loc))
        else:
            print(loc)


#Driver code
print("Welcome to the recycling location mapper! ")
print("Here is a list of all possible recycling locations: ")
counter = 0
for line in all_lines:
    for stop in line:
        counter += 1
        print(counter, ". ", stop)
start = input("\nWhat is the name of the recycling location do you want to start at? ")

if start not in all_stations:
    raise NameError("Not a valid name")
print("\nAll locations from closest to farthest to {}: \n".format(start))
to_string()
view = input("\nEnter name of location to view address or enter (E) to exit: ")

while view != "E":
    graph = create_graph()
    print(graph[view])
    view = input("\nEnter name of location to view address or enter (E) to exit: ")

