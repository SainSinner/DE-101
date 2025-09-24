# Пузырьковая сортировка

def sorted_array(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    answer = array
    return answer


nums = [5, 2, 9, 1, 5, 6]
print(sorted_array(nums))
