def my_sum(L):
    res = 0
    i = 0
    while i < len(L):
        res += L[i]   # add the list element, not the index
        i += 1        # increment i to avoid infinite loop
    return res