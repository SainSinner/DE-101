def sorted_array(array):
    i = 0
    x = 1
    while x != len(array):
        if array[i] > array[x]:
            memory = array[i]
            array[i] = array[x]
            array[x] = memory
            i = 0
            x = 1
        else:
            i+=1
            x+=1
    answer = array
    return answer


nums = [5, 2, 9, 1, 5, 6]
print(sorted_array(nums))
