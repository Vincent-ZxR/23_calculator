import copy
from ReachableNumbers import ReachableNumbers, NumberPath
from Operations import addition, subtraction, multiplication, division

# List of possible operations
operations_list = [addition, subtraction, multiplication, division]


def find_cost(n: int, nb_layers=3) -> NumberPath:
    """
    Find the cheapest way to reach 23
    :param n: Number to find the cost
    :param nb_layers: Number of layers of operations
    :return: Path to 23 with cost
    """
    # Initialize the dictionary
    numbers_from_n = ReachableNumbers(n)
    numbers_from_n.init_layer0()
    for layer in range(nb_layers):
        print(layer)
        # Save the reachable numbers from n at layer l-1
        save_numbers_from_n = copy.deepcopy(numbers_from_n)
        # Test all operations
        for operation in operations_list:
            # Test all reachable numbers from n at layer l-1
            for number, path in save_numbers_from_n.items():
                numbers_from_n.connect(operation(number, max(numbers_from_n[23].cost - path.cost, 0)))
    return numbers_from_n[23]


print(find_cost(1101))
