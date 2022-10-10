import matplotlib.pyplot as plt
from main import find_cost

cost_1layer = {}
cost_2layer = {}
cost_3layer = {}
cost_4layer = {}

for i in range(100):
    cost_1layer[i] = find_cost(i, min_nlayer=3)

fig, ax = plt.subplots()
ax.scatter(cost_1layer.keys(), [cost_1layer[i].cost for i in cost_1layer.keys()])

ax.set_xlabel("Number #")
ax.set_ylabel("Cost")

with open("results.txt", 'w') as f:
    for key, value in cost_4layer.items():
        f.write(f"{key} = {value} \n")
plt.show()
