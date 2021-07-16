def linearsearch(values, item):
    for i in range(len(values)):
        if values[i] == item:
            return i

    return -1


values = [1, 4, 2, 6, 8, 10, 12, 16, 77, 43, 55, 100, 98]
item = 77
result = linearsearch(values, item)
if (result == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", result)
