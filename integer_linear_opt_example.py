'''
Maximize	profit = 124x + 136y
constraint a	18x + 12y <,= 4000
constraint b	6x + 8y <,= 3500
non negativity constraint	x,y >,= 0
'''

import numpy as np
from scipy.optimize import linprog
#Solution without PuLP-2.9.0-py3-none-any.whl.metadata (pulp lib)

profits = np.array([124, 136]) 
component_constraints = np.array([
    [18, 12],  # Component A requirements
    [6, 8]     # Component B requirements
])
supply_limits = np.array([4000, 3500])  

result = linprog(-profits, A_ub=component_constraints, b_ub=supply_limits, bounds=[(0, None), (0, None)], method='highs')
continuous_solution = result.x
continuous_profit = -result.fun

x_max = min(supply_limits[0] // component_constraints[0, 0], supply_limits[1] // component_constraints[1, 0]) + 1
y_max = min(supply_limits[0] // component_constraints[0, 1], supply_limits[1] // component_constraints[1, 1]) + 1

integer_profit = 0
integer_solution = [0, 0]

for x in range(x_max + 1):
    for y in range(y_max + 1):
        if (18 * x + 12 * y <= 4000) and (6 * x + 8 * y <= 3500): 
            profit = 124 * x + 136 * y
            if profit > integer_profit:
                integer_profit = profit
                integer_solution = [x, y]

profit_difference = continuous_profit - integer_profit
rounded_solution_matches = (
    round(continuous_solution[0]) == integer_solution[0] and
    round(continuous_solution[1]) == integer_solution[1]
)

# Results
print("Continuous Solution:", continuous_solution)
print("Continuous Profit:", continuous_profit)
print("Integer Solution:", integer_solution)
print("Integer Profit:", integer_profit)
print("Profit Difference:", profit_difference)
print("Rounded Solution Matches Integer:", rounded_solution_matches)



