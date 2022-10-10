import copy
from ReachableNumbers import ReachableNumbers, NumberPath
from Operations import addition, subtraction, multiplication, division

# List of possible operations
operations_list = [addition, subtraction, multiplication, division]


def find_cost(n: int, min_nlayer=3) -> NumberPath:
    """
    Find the cheapest way to reach 23
    :param n: Number to find the cost
    :param min_nlayer: Number of layers of operations
    :return: Path to 23 with cost
    """
    # create the dictionary
    numbers_from_n = ReachableNumbers(n)
    # Initiate with a cost as low as possible
    numbers_from_n.init_layer0()

    # Loop to find the cost
    layer = 0
    cur_cost = numbers_from_n[23]
    prev_cost = cur_cost
    while layer < min_nlayer or cur_cost != prev_cost:
        prev_cost = numbers_from_n[23]
        print(f"With {layer} layer(s): {numbers_from_n[23]}, {len(numbers_from_n)} possibilities tested")
        layer += 1
        # Save the reachable numbers from n at layer l-1
        save_numbers_from_n = copy.deepcopy(numbers_from_n)
        # Test all operations
        for operation in operations_list:
            # Test all reachable numbers from n at layer l-1
            for number, path in save_numbers_from_n.items():
                numbers_from_n.connect(operation(number, max(numbers_from_n[23].cost - path.cost - 1, 0)))
        # Remove the numbers further than the current cost to reach 23
        numbers_from_n.clean()
        cur_cost = numbers_from_n[23]
    print(f"With {layer} layer(s): {numbers_from_n[23]}, {len(numbers_from_n)} possibilities tested")
    return numbers_from_n[23]

print("1996")
# find_cost(1996)
print("1997")
# find_cost(1997)

