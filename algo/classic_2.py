def two_sum(array, target):
    s = 0
    e = 1
    while array[s] + array[e] != target:
        if e < len(array) - 1:
            e+=1
        else:
            s+=1
            e=s+1
    answer = []
    answer.append(s)
    answer.append(e)
    return answer


nums = [15, 2, 11, 7]
target = 9
print(two_sum(nums, target))
