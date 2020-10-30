def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache= {}
    if length > 1:
        for i in range(0 , length):
            if weights[i] in cache:
                if weights[i] + weights[i] == limit:
                    print( (cache[weights[i]], i))
                    return (i,cache[weights[i]])
            
            
            if weights[i] not in cache:
                if limit - weights[i] in cache:
                    cache[weights[i]] = i

                    inorder = sorted((cache[weights[i]], cache[limit - weights[i]]), reverse=True)
                    return (inorder[0], inorder[1])

                cache[weights[i]] = i

    return None
