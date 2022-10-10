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
        from constants import ADD_COST, MUL_COST
        # Initiate with the number its own and the direct addition path to 23
        self[self.number] = NumberPath(0, f"{self.number}")
        if abs(self.number) > 46:
            quotient = self.number // 23
            remainder = self.number % 23
            self[23] = NumberPath(ADD_COST + remainder + MUL_COST + abs(quotient),
                                  f"({self.number}-{remainder})/{quotient}")
        else:
            self[23] = NumberPath(ADD_COST + abs(23 - self.number), f"{self.number}{23 - self.number:+}")

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

    def clean(self):
        """
        Remove all value further than the current cost to rach 23
        """
        for key in list(self):
            if self[key] > self[23]:
                del self[key]


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
        if self.operation.startswith('(') and self.operation.endswith(')'):
            return f"cost {self.cost} with {self.operation[1:-1]}"
        return f"cost {self.cost} with {self.operation}"

    def __add__(self, other):
        return NumberPath(self.cost + other.cost, f"({other.operation}{self.operation})")

    def __eq__(self, other):
        return self.cost == other.cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __len__(self, other):
        return self.cost <= other.cost
