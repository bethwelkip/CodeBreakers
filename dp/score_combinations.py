from functools import lru_cache

@lru_cache(1000)
def combinations(score):
    '''
    final score: sc
    ore
    options: 2,3, 7
    '''
    res = set()
    def recurse(currScore, chosen):
        if currScore == 0:
            res.add(tuple(sorted(chosen)))
            return

        for option in [2,3,7]:
            if currScore >= option:
                recurse(currScore-option, chosen + [option])
    recurse(score, [])
    return res

def bottom_up_dp(score):
    arr = [score+1 for _ in range(score+1)]
    arr[0] = 0
    for opt in [2,3,7]:
        arr[opt] = 1
    for i in range(score+1):
        for opt in [2,3,7]:
            if i >= opt:
                arr[i] = min(arr[i], arr[i-opt]+1)
    return arr[-1]

def top_down_dp(score):
    pass
print(combinations(300))
print(bottom_up_dp(12))