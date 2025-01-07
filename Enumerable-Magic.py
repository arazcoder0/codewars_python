def any_(list, function):
    for item in list:
        if function(item):
            return True
    return False 
    pass