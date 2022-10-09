import matplotlib.pyplot as plt
from main import find_cost

cost_1layer = {}
cost_2layer = {}
cost_3layer = {}
cost_4layer = {}

for i in range(100):
    cost_1layer[i] = find_cost(i, nb_layers=1)
    cost_2layer[i] = find_cost(i, nb_layers=2)
    cost_3layer[i] = find_cost(i, nb_layers=3)
    cost_4layer[i] = find_cost(i, nb_layers=4)

fig, ax = plt.subplots()
ax.scatter(cost_1layer.keys(), [cost_1layer[i].cost for i in cost_1layer.keys()], label="1 layer")
ax.scatter(cost_2layer.keys(), [cost_2layer[i].cost for i in cost_2layer.keys()], label="2 layer")
ax.scatter(cost_3layer.keys(), [cost_3layer[i].cost for i in cost_3layer.keys()], label="3 layer")
ax.scatter(cost_4layer.keys(), [cost_4layer[i].cost for i in cost_4layer.keys()], label="4 layer")

ax.set_xlabel("Number #")
ax.set_ylabel("Cost")
ax.legend()

with open("results.txt", 'w') as f:
    for key, value in cost_4layer.items():
        f.write(f"{key} = {value} \n")
plt.show()
