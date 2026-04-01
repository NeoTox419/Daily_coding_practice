#porblem name: Equalize the towers
'''
INTUITION:
-----------
We need to make all tower heights equal. For any chosen target height H,
the cost to convert tower i from heights[i] to H is:

    abs(heights[i] - H) * cost[i]

So total cost becomes:

    total_cost(H) = Σ |heights[i] - H| * cost[i]

This is a weighted absolute difference minimization problem.

In unweighted cases (all cost[i] = 1), the minimum occurs at the median.
In weighted cases, the minimum occurs at the WEIGHTED MEDIAN.

Why?
Because absolute value functions form a convex function when summed.
The minimum of a convex function can be found using:
    1. Weighted median (mathematical property)
    OR
    2. Binary search on convex function.

The optimal height will be around the weighted median of heights.


APPROACH:
----------
1. Pair heights with their costs.
2. Sort towers by height.
3. Find the weighted median:
        - Compute total cost weight.
        - Traverse sorted towers accumulating weights.
        - The height where cumulative weight >= total_weight / 2
        is the weighted median.
4. Compute total cost using that height.
5. Return total cost.

Time Complexity:
    O(n log n)  (due to sorting)

Space Complexity:
    O(n)
'''


class Solution:
    def minCost(self, heights, cost):
        # Step 1: Pair heights and cost
        towers = list(zip(heights, cost))

        # Step 2: Sort by height
        towers.sort()

        # Step 3: Find weighted median
        total_weight = sum(cost)
        cumulative_weight = 0
        weighted_median = 0

        for h, c in towers:
            cumulative_weight += c
            if cumulative_weight >= total_weight / 2:
                weighted_median = h
                break

        # Step 4: Compute total minimum cost
        min_cost = 0
        for h, c in towers:
            min_cost += abs(h - weighted_median) * c

        return min_cost
