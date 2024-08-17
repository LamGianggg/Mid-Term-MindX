def count_swap(arr):
    swap_count = 0
    
    a = {}
    position = 0
    for x in arr:
        a[x] = position
        position += 1

    new_arr = sorted(a.items())

    i = 0
    while i < len(arr):
        if new_arr[i][1] == i:
            i += 1
            continue
        
        y = new_arr[i][1]
        new_arr[i], new_arr[y] = new_arr[y], new_arr[i]
        
        swap_count += 1
    
    return swap_count

print(count_swap([3,2,6,1]))