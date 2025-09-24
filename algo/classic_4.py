def nswr_fnc(a):
    answer = []
    for i in range(a+1):
        if i % 2 == 0:
            answer.append(i)
    return answer

print(nswr_fnc(10))
