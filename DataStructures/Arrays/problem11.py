"""
Each position is the product of all elements but the value of the
position.

input: [1,2,3,4,5]
output: [120, 60, 40, 30, 24]

O(n), O(n)
"""


def solve(elements):
    c, cc = 1, 1
    prod_lr, prod_rl = [], []

    for x in elements:
        c *= x
        prod_lr.append(c)

    for y in range(len(elements)-1, -1, -1):
        cc *= elements[y]
        prod_rl = [cc] + prod_rl

    for i in range(len(elements)):
        if i == 0:
            elements[i] = prod_rl[i + 1]
        elif 0 < i < len(elements)-1:
            elements[i] = prod_lr[i-1] * prod_rl[i+1]
        else:
            elements[i] = prod_lr[i-1]

    return elements
