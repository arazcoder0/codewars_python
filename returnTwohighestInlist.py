def two_highest(arg1):
    result = []
    min = 0
    max = 0
    for x in arg1:
        if x >= max:
            max = x
    for x in arg1:
        if x > min and x < max:
            min = x
    if max: 
        result.append(max)
    if min: 
        result.append(min)
        
    return result
    pass