def solve(arr):
    return sorted(arr, key=lambda x: (-arr.count(x), x))

print(solve([2,3,5,3,7,9,5,3,7]))
