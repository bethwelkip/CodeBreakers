'''
Paramenters:

array of currency conversion rates. E.g. ['USD', 'GBP', 0.77] which means 1 USD is equal to 0.77 GBP
an array containing a 'from' currency and a 'to' currency
Given the above parameters, find the conversion rate that maps to the 'from' currency to the 'to' currency.
Your return value should be a number.

Example:
You are given the following parameters:

Rates: ['USD', 'JPY', 110] ['US', 'AUD', 1.45] ['JPY', 'GBP', 0.0070]
To/From currency ['GBP', 'AUD']
Find the rate for the 'To/From' curency. In this case, the correct result is 1.89.


'''
from typing import DefaultDict
from collections import defaultdict

def curr_converter(currencies):
    graph = defaultdict(list)
    for start, to, cost in currencies:
        graph[start].append(to, cost)
