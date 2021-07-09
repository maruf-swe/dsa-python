# Python program for implementation of Insertion Sort

def insertionSort(elements):
    for i in range(1, len(elements)):
        temp = elements[i]
        j = i - 1
        while j >= 0 and temp < elements[j]:
            arr[j + 1] = elements[j]
            j -= 1

        elements[j + 1] = temp
    return elements


arr = [12, 11, 13, 5, 6]
print(insertionSort(arr))
