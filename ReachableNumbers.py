class ReachableNumbers(dict):
    """
    A dictionary that contains all numbers reachable from a given number
    and the associated NumberPath for each number
    """
    def __init__(self, number: int):
        # The starting number
        self.number = number
        # Dictionary that contains the reachable numbers and the associated path
        super().__init__()

    def init_layer0(self):
        from constants import ADD_COST
        # Initiate with the number its own and the direct addition path to 23
        self[self.number] = NumberPath(0, self.number)
        self[23] = NumberPath(ADD_COST + abs(23 - self.number), f"+{23 - self.number}")

    def __str__(self):
        to_print = f"From {self.number}\n"
        for key, value in self.items():
            to_print += f"{key}: {value}\n"
        return to_print

    def connect(self, other):
        """
        Connect other to self:
            If a shorter path is found with other, add it to self
            If a new number is reachable with other, add it to self
            Else keep self
        """
        # Can not connect other to self
        if not bool(other) or other.number not in self.keys():
            return self
        for target, other_to_target_path in other.items():
            # If other provides a faster way to get to target than self
            combined_path = other_to_target_path + self[other.number]
            if target in self.keys():
                if combined_path < self[target]:
                    self[target] = combined_path
            # If other provides another reachable number, add the path to self
            else:
                self[target] = combined_path


class NumberPath(object):
    """
    A NumberPath is a series of operation and the associated cost
    """
    def __init__(self, cost: int, operation: str):
        # Total cost af all operations
        self.cost = cost
        # Operation in str
        self.operation = operation

    def __str__(self):
        return f"cost {self.cost} with {self.operation[1:-1]}"

    def __add__(self, other):
        return NumberPath(self.cost + other.cost, f"({other.operation}{self.operation})")

    def __eq__(self, other):
        return self.cost == other.cost

    def __lt__(self, other):
        return self.cost < other.cost
