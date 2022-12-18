


def binary_search(list1, x):

    list1.sort()
    low = 0
    high = list1.index(list1[-1]) # or = len(list1)-1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if list1[mid] < x:
            low = mid + 1

        elif list1[mid] > x:
            high = mid - 1

        else:
            return f"{x} is in index {mid}"

    return f"{x} is not found in {list1}"



list1 = [ 5,14,3,7,1,13,12,6,2,4,8,10 ]
x = -1

result = binary_search(list1, x)
print(result)

