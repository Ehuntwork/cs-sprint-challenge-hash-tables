def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = [] 
    cache = {}

    for x in a:
        if x < 0:
            negX = x * -1
            if negX in cache and cache[negX] == False:
                cache[negX] == True
                result.append(negX)
            if negX not in cache:
                cache[negX] = True

        if x not in cache and x > 0:
            cache[x] = False
        
        if x in cache and cache[x] == True:
            result.append(x)
        
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
