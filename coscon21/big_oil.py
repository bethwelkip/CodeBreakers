'''
You are an analyst who took up a job at a major oil company — Eggson Mobile — with the intention of convincing them to switch to more renewable sources of energy. You hear about a new potential oil drilling operation that your colleagues are investigating, and decide to write a report to convince your boss to abandon this project by showing them that the associated costs are too high.

Luckily, before actually drilling your company needs to test which of the candidate drilling locations have oil. The potential locations of the new testing operations are a series of sites situated in a row, one after the other. You know that testing any one of the sites prevents you from testing any of its neighboring sites for oil, as the testing shockwaves that are propagated through the bedrock might interfere if sites are too close to one another. This could lead to inaccurate determinations of whether oil exists at the site, and the last thing you want (since you care about the environment) is to have your company drill at a place where there's no oil.

You decide to sabotage the testing operation. You obtain from your colleague the costs associated with testing for oil at each of these sites and decide to only include in your report (rather maliciously) the highest possible total cost of a testing operation that doesn't violate your company's constraint (that test sites can't be adjacent). Write a function to compute this maximal cost.

Input Format

The first line contains a positive integer  The next line contains  space-separated (maybe negative) integers that make up the testing costs associated with each of the sites.

Constraints


Each cost lies between  and 

Output Format

The output should consist of one integer: the maximal cost of an allowed testing operation.

Sample Input 0

5
14 12 15 1 20
Sample Output 0

49
Sample Input 1

4
100 0 1 99
Sample Output 1

199





'''
#!/bin/python3


def oil(n, costs):
    if n <= 1:
        return costs[0]
    max_cost = [0 for _ in range(n)]
    max_cost[0] = costs[0]
    max_cost[1] = max(costs[0], costs[1])
    for i in range(2, n):
        max_cost[i] = max(max_cost[i-1], max_cost[i-2]+costs[i])
    return max(max_cost[-1], max_cost[-2])


if __name__ == '__main__':
    n = int(input().strip())

    costs = list(map(int, input().rstrip().split()))
    print(oil(n, costs))
