def intersection(arrays):
    """
    YOUR CODE HERE
    """
    cache = {}
    result = []
    
    for integer in arrays[0]:
        cache[integer] = 0
    
    for array in arrays:
        for integer in array:
            if integer in cache:
                cache[integer] += 1
    
    for item in cache:
        if cache[item] == len(arrays):
            result.append(item)
            
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
