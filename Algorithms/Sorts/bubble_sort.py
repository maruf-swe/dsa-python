# Bubble sort in Python

def bubbleSort(array):
    length = len(array)

    for i in range(length - 1):
        flag = False
        #  Last i elements are already in place
        for j in range(length - i - 1):

            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                flag = True

        if flag == False:
            break


data = [10, 22, 3, 4, 5]

bubbleSort(data)
print('Sorted Array in Ascending Order:')
print(data)

