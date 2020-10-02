cache = {}

def get_indices_of_item_weights(weights, length, limit):
    """
    Find two items in the weights list that add to limit.

    ...Loop through the length?

    Return  a tuple from containg numbers from largest to smallest.

    If none return none

    ...add all nums with first then add to cache and so on?
    """
    if length > 1:
        for i in range(0, length):
            for x in range(0, length):
                if i != x:
                    if weights[i] + weights[x] == limit:
                        if x < i:
                            return (i, x)
                        return (x , i)
    else:
        return None
