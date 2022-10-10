from ReachableNumbers import NumberPath, ReachableNumbers

"""
For all operations:
    Return all numbers reachable from "number" with a max range of "max_cost".
    Return empty if nothing is reachable within "max_cost" range.
"""


def addition(number: int, max_cost: int) -> ReachableNumbers:
    from constants import ADD_COST
    reachable_numbers = ReachableNumbers(number)
    if max_cost - ADD_COST > 1:
        for i in range(1, max_cost - ADD_COST + 1):
            reachable_numbers[number + i] = NumberPath(abs(i) + ADD_COST, f"+{i}")
        return reachable_numbers
    return ReachableNumbers(number)


def subtraction(number: int, max_cost: int) -> ReachableNumbers:
    from constants import ADD_COST
    reachable_numbers = ReachableNumbers(number)
    if max_cost - ADD_COST > 1:
        for i in range(-(max_cost - ADD_COST), 0):
            reachable_numbers[number + i] = NumberPath(abs(i) + ADD_COST, f"{i}")
        return reachable_numbers
    return ReachableNumbers(number)


def multiplication(number: int, max_cost: int) -> ReachableNumbers:
    from constants import MUL_COST
    reachable_numbers = ReachableNumbers(number)
    if max_cost - MUL_COST > 2:
        for i in range(2, max_cost - MUL_COST + 1):
            reachable_numbers[number * i] = NumberPath(abs(i) + MUL_COST, f"*{i}")
            reachable_numbers[number * -i] = NumberPath(abs(i) + MUL_COST, f"*-{i}")
        return reachable_numbers
    return ReachableNumbers(number)


def division(number: int, max_cost: int) -> ReachableNumbers:
    from constants import MUL_COST
    reachable_numbers = ReachableNumbers(number)
    if max_cost - MUL_COST > 2:
        for i in range(2, max_cost - MUL_COST + 1):
            if number % i == 0:
                reachable_numbers[number // i] = NumberPath(abs(i) + MUL_COST, f"/{i}")
                reachable_numbers[number // -i] = NumberPath(abs(i) + MUL_COST, f"/-{i}")
        return reachable_numbers
    return ReachableNumbers(number)
