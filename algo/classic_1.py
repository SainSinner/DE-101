def is_palindrome(word):
    s = 0
    e = 0
    e = len(word) - 1
    while s < e:
        if word[s] == word[e]:
            s += 1
            e -= 1
        else:
            return False
    return True


# x=input()
x = "level"
print(is_palindrome(x))
