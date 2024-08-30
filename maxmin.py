
array1 = [2, 4, 1, 0, 2, -1]
array2 = [20, 50, 12, 6, 14, 8]
array3 = [100, -100]


def max_min(arr):
    ordered_array = sorted(arr)
    return_arr = [ordered_array[0], ordered_array[-1]]
    return return_arr


print(max_min(array1))
print(max_min(array2))
print(max_min(array3))
