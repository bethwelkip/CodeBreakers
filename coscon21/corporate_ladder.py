'''
The COO of your company has a list of  workers who are all paid the same, but have different productivities. She says she's recently secured a supply of machines, each of productivity . She wants to know the maximum increase in productivity possible if she chooses to fire some subset of her employees and replaces them with machines.

Input Format

The first line contains two space-separated positive integers  and  (in that order), which represent the number of workers she has, as well as the productivity of a machine. The next line contains  space-separated integers that represent the productivities of each of her workers.

Constraints

You can assume that , and both  and all the productivities will be in the range .

Output Format

The output should consist of one integer: the maximum possible increase in productivity that can be attained by firing some subset of her workers and replacing them with machines. (Note a worker can only be replaced by a single machine.)

Sample Input 0

5 10
7 8 20 13 3
Sample Output 0

12




'''
#!/bin/python3


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    # technically unnecessary, but it's ok to keep
    productivities = list(map(int, input().rstrip().split()))
    max_prod = 0
    # Input has been handled for you; write your code here
    for prod in productivities:
        if prod < m:
            max_prod += m-prod
    print(max_prod)
