def binary_search(my_list, item):
    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = my_list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


my_list1 = [1, 3, 5, 7, 9, 11, 12, 14, 15, 17, 18]
print(binary_search(my_list1, 11))
print(binary_search(my_list1, 18))
