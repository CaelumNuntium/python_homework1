def find_ranges(a):
    s = sorted(a)
    m = s[0]
    res = []
    for i in range(len(s) - 1):
        if s[i + 1] - s[i] > 1:
            res.append([m, s[i]])
            m = s[i + 1]
    res.append([m, s[-1]])
    for i in range(len(res)):
        if res[i][0] == res[i][1]:
            res[i] = f"{res[i][0]}"
        else:
            res[i] = f"{res[i][0]}-{res[i][1]}"
    return res


#test
print(find_ranges([1, 2, 3, 4, 6, 8, 9, 10, 12, 13, 14, 16]))
print(find_ranges([1, 5, 8]))
print(find_ranges([1, 3, 4, 5, 9]))
print(find_ranges([1, 2, 3, 4, 6, 8, 9, 10]))
