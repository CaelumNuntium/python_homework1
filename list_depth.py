def list_depth(a):
    if not isinstance(a, list):
        return 0
    else:
        depths = []
        for i in a:
            depths.append(list_depth(i))
        return sorted(depths)[-1] + 1


#test
print(list_depth([1, 2, [3, 4, [5, [6, 7], 6]], 7]))
print(list_depth([1, 2, 3]))
print(list_depth([1, [3, 2, [5]], 4]))
