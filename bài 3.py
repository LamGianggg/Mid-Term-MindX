def has_sequence_with_sum(target_sum, arr):
    for i in range(len(arr)):
        tong = 0
        for j in range(i, len(arr)):
            tong += arr[j]
            if tong == target_sum:
                return True
    return False