def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []

    for arr in range(0, len(arrays)):
        currentList = {}

        for arrItem in arrays[arr]:
              
            if arr == 0:
                currentList[arrItem] = arrItem

            if arr != 0:
                if arrItem not in currentList and arrItem in  previousList:
                    currentList[arrItem] = arrItem
                    if arr == len(arrays) - 1 : 
                        result.append(currentList[arrItem])

                     

        previousList = currentList


    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
