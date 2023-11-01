def bubble_sort(arr):
    index_len = len(arr) -1

    for i in range(index_len):
        for j in range(0, index_len - i):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j +1], arr[j]
    return arr


test_arr = [109, 23, 4, 56, 67, 78, 3]
print(bubble_sort(test_arr))