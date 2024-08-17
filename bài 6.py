def find_closest_distance(arr):
    new_arr = sorted(arr)
    c = []
    for i in range(len(arr) - 1):
        c.append(new_arr[i+1] - new_arr[i])
    return min(c)

print(find_closest_distance([1,3,5,6]))
