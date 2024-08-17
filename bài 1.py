def find_mode(arr):    
    a = {}
    for i in arr:
        if i in a:
            a[i] += 1
        else:
            a[i] = 1

    b = max(a.values())

    c = []
    for key, value in a.items():
        if value == b:
            c.append(key)

    d = max(c)

    return d