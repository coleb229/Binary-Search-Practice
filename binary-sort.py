test = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

def binary_search(list, item):
    low = 0
    high = len(list)-1
    operations = 1

    while low <= high:
        mid = (low + high)//2
        guess = list[mid]

        if guess == item:
            return mid, operations

        if guess > item:
            high = mid -1
        else:
            low = mid + 1
        
        operations += 1

    return None, operations

print(binary_search(test, 6))