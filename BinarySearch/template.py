def binary_search(arr) -> bool:
    search_space = None  # placeholder

    def condition(idx) -> bool:
        pass
    # depending on search space [0,n], [1,n]
    left, right = min(search_space), max(search_space)
    while left < right:
        mid = left + (right - left)//2
        if condition(mid):
            right = mid
        else:
            left = mid+1

    return left
