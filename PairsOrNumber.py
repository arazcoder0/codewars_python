def get_larger_numbers(a, b):
    res = []
    for i,x in enumerate(a):
        if x > b[i]:
            res.append(x)
        else:
            res.append(b[i])
        
    return res
    pass