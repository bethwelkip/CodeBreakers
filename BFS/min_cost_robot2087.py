import heapq
import typing


class Solution:
    def minCost(self, startPos, homePos: list, rowCosts: list, colCosts: list) -> int:
        x, y = homePos
        i, j = startPos
        costs = 0
        while i != x:
            if x > i:
                i += 1
            else:
                i -= 1

            costs += rowCosts[i]

        while j != y:
            if y > j:
                j += 1
            else:
                j -= 1

            costs += colCosts[j]
        return costs

        '''
        Below is Dijkstra's algo. It does not work(TLE)
        min_cost = 0
        m,n = len(rowCosts), len(colCosts)
        heap =[]
        heapq.heappush(heap, (0, tuple(startPos)))
        visited = set()
        
        
        while heap:
            cost, pos = heapq.heappop(heap)
            if pos in visited:
                continue
            visited.add((pos))
            if pos == tuple(homePos):
                return cost
            
            directions = [(1,0), (0,1), (-1, 0), (0, -1)]
            for (i,j) in directions:
                row,col = pos[0]+i, pos[1]+j
                if row >=0 and col >= 0 and row < m and col < n and (row, col) not in visited:
                    if (homePos[0]-startPos[0] > col - startPos[0]) and homePos[1]-startPos[1] > row - startPos[1]:
                        if i == 0:
                            heapq.heappush(heap, (cost + colCosts[col], (row, col)))
                        else:
                            heapq.heappush(heap, (cost + rowCosts[row], (row, col)))
                    
                        
         '''
