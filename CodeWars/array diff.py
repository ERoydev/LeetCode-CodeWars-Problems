def array_diff(a, b):
    difference = []

    for i in a:
        if i not in b:
            difference.append(i)
    return difference


print(array_diff([1, 2, 2], [1]))