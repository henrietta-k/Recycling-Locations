"""
Station objects to represent each individual recycling station in Hong Kong
"""

class Station:

    def __init__(self, name):
        """
        """
        self.name = name
        self.address = None
        self.neighbors = []
        self.operator = None

    def __repr__(self):
        """
        Representation of the address
        """
        name_str = "\nName of Station: {}\n".format(self.name)
        address_str = "Address: {}\n".format(self.address)
        operator_str = "Operator: {}".format(self.operator)

        return name_str + address_str + operator_str


    def add_neighbors(self, neighbors_lst):
        """
        Adding names of neighbors to the self.neighbors attribute

        Input:
            neighbors_lst(lst of str):
        """

        for neigh in neighbors_lst:
            if neigh != self.name:
                self.neighbors.append(neigh)


    def add_neighbor(self, neigh):
        """
        Adds a singular neighbor to each of the Station objects

        Input:
            neigh(str): the neighbor to add

        Returns: (does not return a value)
        """
        self.neighbors.append(neigh)


    def add_address(self, add):
        """
        Adds a string to the address attribute

        Inputs:
            add(str): address to be added

        Returns: (does not return a value)
        """
        self.address = add


    def add_operator(self, oper):
        """
        Adding an operator to the self.operator attribute

        Inputs:
            oper(str): name of the operator

        Returns: (does not return a value)
        """
        self.operator = oper
