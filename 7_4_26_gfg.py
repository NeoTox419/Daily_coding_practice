#problem name: stable marriage problem
'''
INTUITION / APPROACH:

This is the classic Stable Marriage Problem solved using the Gale-Shapley Algorithm.

Key idea:
- We let men propose to women (men-optimal solution).
- Each man proposes to women in the order of his preference list.
- Each woman either:
    1. Accepts the proposal if she is free.
    2. If already engaged, she compares:
        - If she prefers the new man → she switches.
        - Otherwise → she rejects the new proposal.

Steps:
1. Initialize all men and women as free.
2. Keep track of which woman each man will propose to next.
3. While there exists a free man:
    - He proposes to the next woman in his preference list.
    - If she is free → match them.
    - If not:
        - Check her preference:
            - If she prefers this man → replace current partner.
            - Else → reject.
4. Continue until all men are matched.

Data structures:
- result[i] → woman matched with man i
- woman_partner[j] → man matched with woman j
- next_proposal[i] → index of next woman man i will propose to
- ranking[j][i] → preference rank of man i for woman j (for quick comparison)

Time Complexity: O(n^2)
'''
class Solution:
    def stableMarriage(self, men, women):
        n = len(men)

        # result[i] = woman assigned to man i
        result = [-1] * n

        # woman_partner[j] = man assigned to woman j
        woman_partner = [-1] * n

        # next woman index each man will propose to
        next_proposal = [0] * n

        # Create ranking for women: ranking[w][m] = preference order
        ranking = [[0] * n for _ in range(n)]
        for w in range(n):
            for rank, m in enumerate(women[w]):
                ranking[w][m] = rank

        # List of free men
        free_men = list(range(n))

        while free_men:
            m = free_men.pop(0)

            # Get next woman to propose
            w = men[m][next_proposal[m]]
            next_proposal[m] += 1

            if woman_partner[w] == -1:
                # Woman is free → match
                woman_partner[w] = m
                result[m] = w
            else:
                current_m = woman_partner[w]

                # Check if woman prefers new man
                if ranking[w][m] < ranking[w][current_m]:
                    # She prefers new man
                    woman_partner[w] = m
                    result[m] = w

                    # Previous man becomes free again
                    result[current_m] = -1
                    free_men.append(current_m)
                else:
                    # She rejects new man
                    free_men.append(m)

        return result